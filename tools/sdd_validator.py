from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, Iterable

ARTIFACT_KINDS = (
    "requirement",
    "specification",
    "architecture_decision",
    "delivery_unit",
    "contour_task",
    "execution_task",
)

APPROVAL_STATUSES = ("Draft", "Ready for Approval", "Approved")

PROJECT_STATUSES = (
    "Draft",
    "Ready for Approval",
    "Approved",
    "Ready for Decomposition",
    "Decomposed",
    "Ready for Implementation",
    "In Implementation",
    "In Review",
    "Ready for Integration Testing",
    "In Integration Testing",
    "Waiting for Fix",
    "Ready for Acceptance",
    "Accepted",
    "Ready for Release",
    "Released",
    "Done",
    "Blocked",
    "Cancelled",
)

READY_STATUS_INDEX = PROJECT_STATUSES.index("Ready for Implementation")

CONTOUR_CODES = ("BA", "SA", "AR", "FE", "BE", "DO", "QA")

ALLOWED_RELATIONS = {
    ("requirement", "requirement", "supersedes"),
    ("requirement", "specification", "refines"),
    ("requirement", "delivery_unit", "decomposes_into"),
    ("specification", "specification", "supersedes"),
    ("specification", "delivery_unit", "decomposes_into"),
    ("architecture_decision", "architecture_decision", "supersedes"),
    ("architecture_decision", "specification", "constrains"),
    ("delivery_unit", "delivery_unit", "depends_on"),
    ("delivery_unit", "contour_task", "decomposes_into"),
    ("contour_task", "contour_task", "depends_on"),
    ("contour_task", "execution_task", "decomposes_into"),
    ("contour_task", "specification", "depends_on"),
    ("contour_task", "architecture_decision", "depends_on"),
    ("execution_task", "execution_task", "depends_on"),
    ("execution_task", "specification", "implements"),
    ("execution_task", "architecture_decision", "implements"),
}

MOJIBAKE_MARKERS = ("Ã", "Â", "Ð", "Ñ", "â€", "â€™", "â€œ", "â€�", "�")

EXPECTED_TEMPLATE_FILES = (
    "requirement.md",
    "specification.md",
    "architecture_decision.md",
    "delivery_unit.md",
    "contour_task.md",
    "execution_task.md",
    "impact_assessment.md",
    "handoff.md",
)

EXPECTED_ISSUE_TEMPLATE_FILES = (
    "delivery-unit.md",
    "architecture-decision.md",
    "contour-task.md",
    "execution-task.md",
    "fix-after-integration.md",
    "config.yml",
)

EXPECTED_TOOL_FILES = (
    "sdd_validator.py",
    "validate_package.py",
    "validate_pr.py",
    "validate_repo.py",
)

EXPECTED_DOC_FILES = tuple(f"{index:02d}-{name}.md" for index, name in (
    (0, "template-overview"),
    (1, "communication-rules"),
    (2, "process-model"),
    (3, "role-model"),
    (4, "artifact-model"),
    (5, "link-model"),
    (6, "readiness-and-statuses"),
    (7, "delivery-unit-artifact-set"),
    (8, "canonical-ownership-map"),
    (9, "stage-document-index"),
    (10, "github-projection"),
    (11, "handoff-protocol"),
    (12, "pr-policy-and-branch-strategy"),
    (13, "impact-assessment"),
    (14, "validation-and-anti-drift"),
    (15, "runbooks"),
    (16, "telemetry"),
    (17, "lifecycle-cleanup"),
    (18, "baseline-reconciliation"),
))

TEXT_EXTENSIONS = {".md", ".json", ".yml", ".yaml", ".txt"}


def _read_json(path: Path) -> tuple[Any | None, str | None]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return None, f"{path}: invalid UTF-8: {exc}"
    except OSError as exc:
        return None, f"{path}: unable to read file: {exc}"

    try:
        return json.loads(text), None
    except json.JSONDecodeError as exc:
        return None, f"{path}: invalid JSON: {exc}"


def _artifact_map(package: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {artifact["artifact_id"]: artifact for artifact in package.get("artifacts", [])}


def _link_key(source_kind: str, source_id: str, target_kind: str, target_id: str, relation: str) -> tuple[str, str, str, str, str]:
    return (source_kind, source_id, target_kind, target_id, relation)


def _relation_key(source_kind: str, target_kind: str, relation: str) -> tuple[str, str, str]:
    return (source_kind, target_kind, relation)


def _status_index(value: str) -> int:
    try:
        return PROJECT_STATUSES.index(value)
    except ValueError:
        return -1


def _is_ready(value: str) -> bool:
    return _status_index(value) >= READY_STATUS_INDEX


def iter_text_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS and ".git" not in path.parts:
            yield path


def validate_text_encoding(root: Path) -> list[str]:
    errors: list[str] = []
    for path in iter_text_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path}: invalid UTF-8: {exc}")
            continue
        except OSError as exc:
            errors.append(f"{path}: unable to read file: {exc}")
            continue

        if any(marker in text for marker in MOJIBAKE_MARKERS):
            errors.append(f"{path}: suspected mojibake or encoding corruption")
    return errors


def validate_schema_alignment(root: Path) -> list[str]:
    errors: list[str] = []
    canonical_path = root / "schemas" / "canonical-artifact-model.schema.json"
    link_path = root / "schemas" / "typed-link-model.schema.json"

    canonical, error = _read_json(canonical_path)
    if error:
        return [error]
    link_schema, error = _read_json(link_path)
    if error:
        return [error]

    if canonical["$defs"]["artifact"]["properties"]["artifact_kind"]["enum"] != list(ARTIFACT_KINDS):
        errors.append("canonical-artifact-model.schema.json: artifact kind enum is out of sync")

    if canonical["$defs"]["project_status"]["enum"] != list(PROJECT_STATUSES):
        errors.append("canonical-artifact-model.schema.json: project status enum is out of sync")

    if canonical["$defs"]["link"]["properties"]["relation"]["enum"] != [
        "supersedes",
        "refines",
        "decomposes_into",
        "constrains",
        "depends_on",
        "implements",
    ]:
        errors.append("canonical-artifact-model.schema.json: relation enum is out of sync")

    actual_relations: set[tuple[str, str, str]] = set()
    for item in link_schema.get("oneOf", []):
        properties = item.get("properties", {})
        actual_relations.add(
            (
                properties.get("source_kind", {}).get("const", ""),
                properties.get("target_kind", {}).get("const", ""),
                properties.get("relation", {}).get("const", ""),
            )
        )

    if actual_relations != ALLOWED_RELATIONS:
        errors.append("typed-link-model.schema.json: allowed relation matrix is out of sync")

    return errors


def validate_repo_layout(root: Path) -> list[str]:
    errors: list[str] = []
    for name in EXPECTED_DOC_FILES:
        if not (root / "docs" / name).is_file():
            errors.append(f"missing canonical document: docs/{name}")

    for name in EXPECTED_TEMPLATE_FILES:
        if not (root / "templates" / name).is_file():
            errors.append(f"missing template file: templates/{name}")

    for name in EXPECTED_ISSUE_TEMPLATE_FILES:
        if not (root / ".github" / "ISSUE_TEMPLATE" / name).is_file():
            errors.append(f"missing GitHub issue template: .github/ISSUE_TEMPLATE/{name}")

    if not (root / ".github" / "pull_request_template.md").is_file():
        errors.append("missing GitHub PR template: .github/pull_request_template.md")

    if not (root / ".github" / "workflows" / "validate.yml").is_file():
        errors.append("missing GitHub workflow: .github/workflows/validate.yml")

    example_manifests = list((root / "examples").glob("*/manifest.json"))
    if not example_manifests:
        errors.append("missing example package manifests under examples/*/manifest.json")
    if not (root / "examples" / "sample-traceability-graph.md").is_file():
        errors.append("missing sample traceability graph: examples/sample-traceability-graph.md")

    for name in EXPECTED_TOOL_FILES:
        if not (root / "tools" / name).is_file():
            errors.append(f"missing validator entrypoint: tools/{name}")

    return errors


def validate_requirement(artifact: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    content = artifact["content"]
    if not str(content.get("statement", "")).strip():
        errors.append(f"{artifact['artifact_id']}: requirement statement is required")
    if not content.get("success_criteria"):
        errors.append(f"{artifact['artifact_id']}: requirement success_criteria is required")
    return errors


def validate_specification(artifact: dict[str, Any], artifacts: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    content = artifact["content"]
    refs = content.get("based_on_requirement_ids", [])
    if not refs:
        errors.append(f"{artifact['artifact_id']}: specification must reference at least one requirement")
    for ref in refs:
        target = artifacts.get(ref)
        if not target or target["artifact_kind"] != "requirement":
            errors.append(f"{artifact['artifact_id']}: invalid requirement reference {ref}")
    return errors


def validate_architecture_decision(artifact: dict[str, Any], artifacts: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    content = artifact["content"]
    refs = content.get("constrains_specification_ids", [])
    if not refs:
        errors.append(f"{artifact['artifact_id']}: architecture decision must constrain at least one specification")
    for ref in refs:
        target = artifacts.get(ref)
        if not target or target["artifact_kind"] != "specification":
            errors.append(f"{artifact['artifact_id']}: invalid specification reference {ref}")
    return errors


def _validate_common_artifact_fields(artifact: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if artifact.get("approval_status") not in APPROVAL_STATUSES:
        errors.append(f"{artifact['artifact_id']}: invalid approval_status")
    if artifact.get("project_status") not in PROJECT_STATUSES:
        errors.append(f"{artifact['artifact_id']}: invalid project_status")
    if not str(artifact.get("title", "")).strip():
        errors.append(f"{artifact['artifact_id']}: title is required")
    return errors


def validate_links(package: dict[str, Any], artifacts: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen: set[tuple[str, str, str, str, str]] = set()
    for link in package.get("links", []):
        key = _link_key(
            link.get("source_kind", ""),
            link.get("source_id", ""),
            link.get("target_kind", ""),
            link.get("target_id", ""),
            link.get("relation", ""),
        )
        if key in seen:
            errors.append(f"duplicate link: {key}")
            continue
        seen.add(key)

        relation_key = _relation_key(
            link.get("source_kind", ""),
            link.get("target_kind", ""),
            link.get("relation", ""),
        )
        if relation_key not in ALLOWED_RELATIONS:
            errors.append(f"invalid typed link: {key}")
            continue

        source = artifacts.get(link["source_id"])
        target = artifacts.get(link["target_id"])
        if not source:
            errors.append(f"missing source artifact for link: {key}")
            continue
        if not target:
            errors.append(f"missing target artifact for link: {key}")
            continue
        if source["artifact_kind"] != link["source_kind"]:
            errors.append(f"source kind mismatch for link: {key}")
        if target["artifact_kind"] != link["target_kind"]:
            errors.append(f"target kind mismatch for link: {key}")

    return errors


def validate_delivery_unit(artifact: dict[str, Any], artifacts: dict[str, dict[str, Any]], link_set: set[tuple[str, str, str, str, str]]) -> list[str]:
    errors = _validate_common_artifact_fields(artifact)
    content = artifact["content"]

    if content.get("delivery_unit_type") not in ("user_facing", "internal_enabler"):
        errors.append(f"{artifact['artifact_id']}: invalid delivery_unit_type")
    if content.get("acceptance_scope") not in ("user", "system"):
        errors.append(f"{artifact['artifact_id']}: invalid acceptance_scope")

    if content.get("delivery_unit_type") == "user_facing" and content.get("acceptance_scope") != "user":
        errors.append(f"{artifact['artifact_id']}: user_facing delivery units must use user acceptance scope")
    if content.get("delivery_unit_type") == "internal_enabler" and content.get("acceptance_scope") != "system":
        errors.append(f"{artifact['artifact_id']}: internal_enabler delivery units must use system acceptance scope")

    req_refs = content.get("parent_requirement_ids", [])
    spec_refs = content.get("specification_ids", [])
    contour_refs = content.get("participating_contours", [])
    adr_refs = content.get("architecture_decision_ids", [])

    if not req_refs:
        errors.append(f"{artifact['artifact_id']}: delivery unit must reference at least one requirement")
    if not spec_refs:
        errors.append(f"{artifact['artifact_id']}: delivery unit must reference at least one specification")
    if not contour_refs:
        errors.append(f"{artifact['artifact_id']}: delivery unit must declare participating contours")

    status = content.get("architecture_decision_status")
    if status not in ("required", "not_required", "deferred"):
        errors.append(f"{artifact['artifact_id']}: invalid architecture_decision_status")
    elif status == "required" and not adr_refs:
        errors.append(f"{artifact['artifact_id']}: architecture_decision_status=required needs architecture_decision_ids")
    elif status == "not_required" and not str(content.get("architecture_decision_rationale", "")).strip():
        errors.append(f"{artifact['artifact_id']}: architecture_decision_rationale is required when status=not_required")
    elif status == "deferred":
        errors.append(f"{artifact['artifact_id']}: architecture_decision_status=deferred is not implementation-ready")

    if not _is_ready(artifact["project_status"]):
        errors.append(f"{artifact['artifact_id']}: delivery unit is not ready for implementation")

    for ref in req_refs:
        target = artifacts.get(ref)
        if not target or target["artifact_kind"] != "requirement":
            errors.append(f"{artifact['artifact_id']}: invalid parent_requirement_id {ref}")
        elif _link_key("requirement", ref, "delivery_unit", artifact["artifact_id"], "decomposes_into") not in link_set:
            errors.append(f"{artifact['artifact_id']}: missing requirement -> delivery_unit link for {ref}")

    for ref in spec_refs:
        target = artifacts.get(ref)
        if not target or target["artifact_kind"] != "specification":
            errors.append(f"{artifact['artifact_id']}: invalid specification_id {ref}")
        elif _link_key("specification", ref, "delivery_unit", artifact["artifact_id"], "decomposes_into") not in link_set:
            errors.append(f"{artifact['artifact_id']}: missing specification -> delivery_unit link for {ref}")

    for contour in contour_refs:
        if contour not in CONTOUR_CODES:
            errors.append(f"{artifact['artifact_id']}: invalid contour code {contour}")

    for ref in adr_refs:
        target = artifacts.get(ref)
        if target and target["artifact_kind"] != "architecture_decision":
            errors.append(f"{artifact['artifact_id']}: invalid architecture_decision_id {ref}")

    return errors


def validate_contour_task(artifact: dict[str, Any], artifacts: dict[str, dict[str, Any]], link_set: set[tuple[str, str, str, str, str]]) -> list[str]:
    errors = _validate_common_artifact_fields(artifact)
    content = artifact["content"]

    if content.get("contour_code") not in CONTOUR_CODES:
        errors.append(f"{artifact['artifact_id']}: invalid contour_code")

    parent_id = content.get("delivery_unit_id")
    parent = artifacts.get(parent_id)
    if not parent or parent["artifact_kind"] != "delivery_unit":
        errors.append(f"{artifact['artifact_id']}: invalid delivery_unit_id {parent_id}")
    elif _link_key("delivery_unit", parent_id, "contour_task", artifact["artifact_id"], "decomposes_into") not in link_set:
        errors.append(f"{artifact['artifact_id']}: missing delivery_unit -> contour_task link")

    spec_refs = content.get("specification_ids", [])
    if not spec_refs:
        errors.append(f"{artifact['artifact_id']}: contour task must reference at least one specification")
    for ref in spec_refs:
        target = artifacts.get(ref)
        if not target or target["artifact_kind"] != "specification":
            errors.append(f"{artifact['artifact_id']}: invalid specification_id {ref}")
        elif _link_key("contour_task", artifact["artifact_id"], "specification", ref, "depends_on") not in link_set:
            errors.append(f"{artifact['artifact_id']}: missing contour_task -> specification dependency for {ref}")

    for ref in content.get("architecture_decision_ids", []):
        target = artifacts.get(ref)
        if target and target["artifact_kind"] != "architecture_decision":
            errors.append(f"{artifact['artifact_id']}: invalid architecture_decision_id {ref}")
        elif target and _link_key("contour_task", artifact["artifact_id"], "architecture_decision", ref, "depends_on") not in link_set:
            errors.append(f"{artifact['artifact_id']}: missing contour_task -> architecture_decision dependency for {ref}")

    if not _is_ready(artifact["project_status"]):
        errors.append(f"{artifact['artifact_id']}: contour task is not ready for implementation")

    if parent and content.get("contour_code") not in parent["content"].get("participating_contours", []):
        errors.append(f"{artifact['artifact_id']}: contour code is not declared by the parent delivery unit")

    return errors


def validate_execution_task(artifact: dict[str, Any], artifacts: dict[str, dict[str, Any]], link_set: set[tuple[str, str, str, str, str]]) -> list[str]:
    errors = _validate_common_artifact_fields(artifact)
    content = artifact["content"]

    parent_id = content.get("contour_task_id")
    parent = artifacts.get(parent_id)
    if not parent or parent["artifact_kind"] != "contour_task":
        errors.append(f"{artifact['artifact_id']}: invalid contour_task_id {parent_id}")
    elif _link_key("contour_task", parent_id, "execution_task", artifact["artifact_id"], "decomposes_into") not in link_set:
        errors.append(f"{artifact['artifact_id']}: missing contour_task -> execution_task link")

    impl_refs = content.get("implementation_refs", [])
    if not impl_refs:
        errors.append(f"{artifact['artifact_id']}: execution task must implement at least one specification or architecture decision")
    for ref in impl_refs:
        target = artifacts.get(ref)
        if not target or target["artifact_kind"] not in ("specification", "architecture_decision"):
            errors.append(f"{artifact['artifact_id']}: invalid implementation ref {ref}")
        elif _link_key("execution_task", artifact["artifact_id"], target["artifact_kind"], ref, "implements") not in link_set:
            errors.append(f"{artifact['artifact_id']}: missing execution_task -> {target['artifact_kind']} implements link for {ref}")

    for ref in content.get("dependencies", []):
        target = artifacts.get(ref)
        if not target or target["artifact_kind"] != "execution_task":
            errors.append(f"{artifact['artifact_id']}: execution task dependencies may only point to execution tasks")
        elif _link_key("execution_task", artifact["artifact_id"], "execution_task", ref, "depends_on") not in link_set:
            errors.append(f"{artifact['artifact_id']}: missing execution_task -> execution_task dependency for {ref}")

    if not _is_ready(artifact["project_status"]):
        errors.append(f"{artifact['artifact_id']}: execution task is not ready for implementation")

    return errors


def validate_package_data(package: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not str(package.get("package_id", "")).strip():
        errors.append("package_id is required")
    if not str(package.get("package_name", "")).strip():
        errors.append("package_name is required")
    if not str(package.get("package_version", "")).strip():
        errors.append("package_version is required")

    artifacts_list = package.get("artifacts")
    if not isinstance(artifacts_list, list) or not artifacts_list:
        return errors + ["artifacts array is required and must not be empty"]

    artifacts = _artifact_map(package)
    if len(artifacts) != len(artifacts_list):
        errors.append("artifact ids must be unique")

    required_kinds = {"requirement", "specification", "delivery_unit", "contour_task", "execution_task"}
    present_kinds = {artifact.get("artifact_kind") for artifact in artifacts_list}
    missing_kinds = required_kinds - present_kinds
    if missing_kinds:
        errors.append(f"missing required artifact kinds: {sorted(missing_kinds)}")

    for artifact in artifacts_list:
        if artifact.get("artifact_kind") not in ARTIFACT_KINDS:
            errors.append(f"{artifact.get('artifact_id', '<unknown>')}: unknown artifact kind")
            continue

        if artifact["artifact_kind"] == "requirement":
            errors.extend(_validate_common_artifact_fields(artifact))
            errors.extend(validate_requirement(artifact))
        elif artifact["artifact_kind"] == "specification":
            errors.extend(_validate_common_artifact_fields(artifact))
            errors.extend(validate_specification(artifact, artifacts))
        elif artifact["artifact_kind"] == "architecture_decision":
            errors.extend(_validate_common_artifact_fields(artifact))
            errors.extend(validate_architecture_decision(artifact, artifacts))
        elif artifact["artifact_kind"] in ("delivery_unit", "contour_task", "execution_task"):
            errors.extend(_validate_common_artifact_fields(artifact))

    errors.extend(validate_links(package, artifacts))
    link_set = {
        _link_key(link["source_kind"], link["source_id"], link["target_kind"], link["target_id"], link["relation"])
        for link in package.get("links", [])
        if isinstance(link, dict)
    }

    for artifact in artifacts_list:
        if artifact["artifact_kind"] == "delivery_unit":
            errors.extend(validate_delivery_unit(artifact, artifacts, link_set))
        elif artifact["artifact_kind"] == "contour_task":
            errors.extend(validate_contour_task(artifact, artifacts, link_set))
        elif artifact["artifact_kind"] == "execution_task":
            errors.extend(validate_execution_task(artifact, artifacts, link_set))

    for artifact in artifacts_list:
        if artifact["artifact_kind"] == "delivery_unit" and artifact["content"].get("architecture_decision_status") == "required":
            if not artifact["content"].get("architecture_decision_ids"):
                errors.append(f"{artifact['artifact_id']}: required architecture decision references are missing")

    return errors


def validate_package_dir(package_dir: Path) -> list[str]:
    manifest = package_dir / "manifest.json"
    data, error = _read_json(manifest)
    if error:
        return [error]
    if not isinstance(data, dict):
        return [f"{manifest}: package manifest must be a JSON object"]
    return validate_package_data(data)


PR_TITLE_DENYLIST = {"wip", "todo", "tbd", "fix", "fixme", "temp", "update", "misc"}


def validate_pr(title: str, body: str) -> list[str]:
    errors: list[str] = []
    normalized_title = " ".join(title.split())
    if not normalized_title:
        errors.append("PR title is required")
    else:
        if len(normalized_title) < 12:
            errors.append("PR title is too short")
        if len(normalized_title) > 100:
            errors.append("PR title is too long")
        if normalized_title.endswith("."):
            errors.append("PR title should not end with a period")
        lowered = normalized_title.lower()
        if any(re.search(rf"\b{re.escape(token)}\b", lowered) for token in PR_TITLE_DENYLIST):
            errors.append("PR title contains a placeholder or low-signal token")

    body_text = body.strip()
    for heading in ("## Summary", "## Validation", "## Impact Assessment", "## Handoff"):
        if heading not in body_text:
            errors.append(f"PR body is missing required section: {heading}")

    if any(marker in body_text for marker in ("TODO", "TBD", "FIXME", "...")):
        errors.append("PR body contains placeholder text")

    return errors


def validate_repo(root: Path) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_schema_alignment(root))
    errors.extend(validate_repo_layout(root))
    errors.extend(validate_text_encoding(root))
    for manifest in sorted((root / "examples").glob("*/manifest.json")):
        errors.extend(validate_package_dir(manifest.parent))
    return errors


def main() -> int:
    root = Path(os.environ.get("REPO_ROOT", Path(__file__).resolve().parents[1]))
    errors = validate_repo(root)
    if errors:
        for error in errors:
            print(error)
        return 1
    return 0

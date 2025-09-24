from pathlib import Path


def test_add_contract_schema():
    openapi_path = Path("specs/002-change-function-of/contracts/openapi.yaml")
    assert openapi_path.exists(), "OpenAPI contract must exist"
    # Minimal check: file contains path for /api/add
    content = openapi_path.read_text()
    assert "/api/add" in content

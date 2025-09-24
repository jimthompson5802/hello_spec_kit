from pathlib import Path


def test_add_contract_schema():
    """Lightweight validation of the OpenAPI contract for `/api/add`.

    This test ensures the contract file exists and contains the minimal schema
    requirements expected by the feature: request requires `x` and `y`, the
    200 response contains `result` and `type`, and `type` enumerates `number` and `string`.
    """
    openapi_path = Path("specs/002-change-function-of/contracts/openapi.yaml")
    assert openapi_path.exists(), "OpenAPI contract must exist"

    content = openapi_path.read_text()
    assert "/api/add" in content

    # Check that request schema requires x and y
    assert "required: [x, y]" in content or "required:\n  - x\n  - y" in content

    # Check response 200 contains result and type
    assert "responses:" in content
    assert "'200'" in content or "200:" in content
    assert "result" in content
    assert "type:" in content

    # Ensure the `type` field enumerates allowed values
    assert (
        "enum: [number, string]" in content
        or "enum:\n  - number\n  - string" in content
    )

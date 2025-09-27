"""
Contract tests for POST /api/echo endpoint
Tests API contract compliance according to OpenAPI specification
"""

import pytest
import json


@pytest.mark.contract
class TestEchoContract:
    """Contract tests for /api/echo endpoint"""

    def test_echo_success_response_structure(self, client):
        """Test successful echo response matches contract schema"""
        # Arrange
        payload = {"text": "Hello World"}

        # Act
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 200
        data = response.get_json()

        # Verify response structure matches EchoResponse schema
        assert "result" in data
        assert "success" in data
        assert data["success"] is True
        assert data["result"] == "YOU ENTERED: Hello World"
        assert "error" not in data or data["error"] is None

    def test_echo_empty_input_error_response(self, client):
        """Test empty input returns 400 error as per contract"""
        # Arrange
        payload = {"text": ""}

        # Act
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 400
        data = response.get_json()

        # Verify error response structure
        assert "error" in data
        assert "success" in data
        assert data["success"] is False
        assert data["error"] == "Please enter text"
        assert "result" not in data or data["result"] is None

    def test_echo_missing_text_field_error_response(self, client):
        """Test missing text field returns 400 error as per contract"""
        # Arrange
        payload = {}

        # Act
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 400
        data = response.get_json()
        assert data["success"] is False
        assert "error" in data

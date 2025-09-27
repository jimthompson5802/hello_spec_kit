"""
Integration tests for Echo empty input error handling
Tests the complete user workflow when submitting empty input to Echo function
"""

import pytest
import json


@pytest.mark.integration
class TestEchoEmptyInputError:
    """Integration tests for Echo empty input error handling"""

    def test_echo_empty_string_error_workflow(self, client):
        """Test complete workflow when user submits empty string to Echo"""
        # Arrange - User attempts to submit empty text
        payload = {"text": ""}

        # Act - User submits empty text via /api/echo endpoint
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives clear error message
        assert response.status_code == 400
        data = response.get_json()

        # Verify error response structure matches spec
        assert data["success"] is False
        assert data["error"] == "Please enter text"
        assert data["result"] is None

    def test_echo_whitespace_only_error_workflow(self, client):
        """Test complete workflow when user submits whitespace-only text"""
        # Arrange - User attempts to submit only whitespace
        payload = {"text": "   "}

        # Act - User submits whitespace-only text via /api/echo endpoint
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives error message (whitespace treated as empty)
        assert response.status_code == 400
        data = response.get_json()

        assert data["success"] is False
        assert data["error"] == "Please enter text"
        assert data["result"] is None

    def test_echo_tabs_and_newlines_error_workflow(self, client):
        """Test complete workflow with tabs and newlines only"""
        # Arrange - User attempts to submit only tabs and newlines
        payload = {"text": "\t\n\r "}

        # Act - User submits whitespace characters via /api/echo endpoint
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives error message (all whitespace treated as empty)
        assert response.status_code == 400
        data = response.get_json()

        assert data["success"] is False
        assert data["error"] == "Please enter text"
        assert data["result"] is None

    def test_echo_missing_text_field_error_workflow(self, client):
        """Test complete workflow when text field is missing from request"""
        # Arrange - User submits request without text field
        payload = {}

        # Act - User submits request without required text field
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives validation error
        assert response.status_code == 400
        data = response.get_json()

        assert data["success"] is False
        assert "error" in data
        # Error message should indicate missing or invalid field

    def test_echo_null_text_field_error_workflow(self, client):
        """Test complete workflow when text field is null"""
        # Arrange - User submits request with null text field
        payload = {"text": None}

        # Act - User submits request with null text value
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives validation error
        assert response.status_code == 400
        data = response.get_json()

        assert data["success"] is False
        assert "error" in data

    def test_echo_invalid_content_type_error_workflow(self, client):
        """Test complete workflow with invalid content type"""
        # Arrange - User submits request with invalid content type
        payload = {"text": "Hello"}

        # Act - User submits request without JSON content type
        response = client.post("/api/echo", data=json.dumps(payload))

        # Assert - Should handle gracefully or return appropriate error
        # This tests the robustness of the endpoint
        assert response.status_code in [
            400,
            415,
        ]  # Bad Request or Unsupported Media Type

"""
Integration tests for Echo function basic flow
Tests the complete user workflow for the Echo functionality
"""

import pytest
import json


@pytest.mark.integration
class TestEchoBasicFlow:
    """Integration tests for Echo function basic flow"""

    def test_echo_complete_workflow_success(self, client):
        """Test complete Echo workflow: user enters text and gets echoed response"""
        # Arrange - User has text to echo
        user_input = "Hello World"
        payload = {"text": user_input}

        # Act - User submits text via /api/echo endpoint
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives properly formatted echoed text
        assert response.status_code == 200
        data = response.get_json()

        # Verify complete response structure
        assert data["success"] is True
        assert data["result"] == f"YOU ENTERED: {user_input}"
        assert data["error"] is None

    def test_echo_empty_text_workflow(self, client):
        """Test Echo workflow when user submits empty text"""
        # Arrange - User submits empty text
        payload = {"text": ""}

        # Act - User submits empty text via /api/echo endpoint
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives appropriate error message
        assert response.status_code == 400
        data = response.get_json()

        assert data["success"] is False
        assert data["error"] == "Please enter text"
        assert data["result"] is None

    def test_echo_whitespace_only_text_workflow(self, client):
        """Test Echo workflow when user submits whitespace-only text"""
        # Arrange - User submits whitespace-only text
        payload = {"text": "   "}

        # Act - User submits whitespace text via /api/echo endpoint
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Should be treated as empty input (based on spec requirements)
        assert response.status_code == 400
        data = response.get_json()

        assert data["success"] is False
        assert data["error"] == "Please enter text"
        assert data["result"] is None

    def test_echo_long_text_workflow(self, client):
        """Test Echo workflow with longer text input"""
        # Arrange - User has longer text to echo
        long_text = "This is a longer text input to test the Echo functionality with more substantial content."
        payload = {"text": long_text}

        # Act - User submits long text via /api/echo endpoint
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives properly formatted echoed long text
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == f"YOU ENTERED: {long_text}"
        assert data["error"] is None

    def test_echo_special_characters_workflow(self, client):
        """Test Echo workflow with special characters"""
        # Arrange - User enters text with special characters
        special_text = "Hello! @#$%^&*()_+-={}[]|\\:;\"'<>,.?/~`"
        payload = {"text": special_text}

        # Act - User submits text with special characters
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Special characters are properly echoed
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == f"YOU ENTERED: {special_text}"
        assert data["error"] is None

    def test_echo_unicode_characters_workflow(self, client):
        """Test Echo workflow with unicode characters"""
        # Arrange - User enters text with unicode characters
        unicode_text = "Hello 世界! 🌍 café naïve résumé"
        payload = {"text": unicode_text}

        # Act - User submits text with unicode characters
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Unicode characters are properly echoed
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == f"YOU ENTERED: {unicode_text}"
        assert data["error"] is None

"""
Integration tests for String concatenation flow
Tests the complete user workflow for string concatenation using the add functionality
"""

import pytest
import json


@pytest.mark.integration
class TestStringConcatenation:
    """Integration tests for String concatenation flow"""

    def test_string_concatenation_both_strings_workflow(self, client):
        """Test complete workflow when both inputs are strings"""
        # Arrange - User wants to concatenate two strings
        payload = {"x": "Hello", "y": "World"}

        # Act - User submits string concatenation request via /api/add endpoint
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives concatenated string result
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == "HelloWorld"  # Basic concatenation
        assert data["error"] is None

    def test_string_concatenation_with_space_workflow(self, client):
        """Test string concatenation with space handling"""
        # Arrange - User wants to concatenate strings with space
        payload = {"x": "Hello ", "y": "World"}

        # Act - User submits string concatenation request
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Space is preserved in concatenation
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == "Hello World"  # Space preserved
        assert data["error"] is None

    def test_string_concatenation_mixed_string_number_workflow(self, client):
        """Test workflow when one input is string, one is number"""
        # Arrange - User enters mixed string and number
        payload = {"x": "Result: ", "y": 42}

        # Act - User submits mixed type concatenation request
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Number is converted to string and concatenated
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == "Result: 42"
        assert data["error"] is None

    def test_string_concatenation_number_string_workflow(self, client):
        """Test workflow when first input is number, second is string"""
        # Arrange - User enters number then string
        payload = {"x": 100, "y": " percent"}

        # Act - User submits number + string request
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Number is converted to string and concatenated
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == "100 percent"
        assert data["error"] is None

    def test_string_concatenation_empty_strings_workflow(self, client):
        """Test workflow with empty strings"""
        # Arrange - User enters empty strings
        payload = {"x": "", "y": ""}

        # Act - User submits empty string concatenation request
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Empty strings concatenate to empty string
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == ""
        assert data["error"] is None

    def test_string_concatenation_special_characters_workflow(self, client):
        """Test workflow with special characters in strings"""
        # Arrange - User enters strings with special characters
        payload = {"x": "Hello!", "y": "@#$%"}

        # Act - User submits special character concatenation request
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Special characters are preserved in concatenation
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == "Hello!@#$%"
        assert data["error"] is None

    def test_string_concatenation_unicode_characters_workflow(self, client):
        """Test workflow with unicode characters in strings"""
        # Arrange - User enters strings with unicode characters
        payload = {"x": "Hello 世界", "y": " 🌍"}

        # Act - User submits unicode string concatenation request
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Unicode characters are preserved in concatenation
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == "Hello 世界 🌍"
        assert data["error"] is None

    def test_string_concatenation_long_strings_workflow(self, client):
        """Test workflow with long strings"""
        # Arrange - User enters long strings
        long_string_a = (
            "This is a very long string that should be concatenated properly " * 5
        )
        long_string_b = (
            "and this is another long string that should also work correctly."
        )
        payload = {"x": long_string_a, "y": long_string_b}

        # Act - User submits long string concatenation request
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Long strings are concatenated correctly
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == long_string_a + long_string_b
        assert data["error"] is None

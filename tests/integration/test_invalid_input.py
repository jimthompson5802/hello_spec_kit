"""
Integration tests for Invalid input error handling
Tests the complete user workflow when submitting invalid inputs to all endpoints
"""

import pytest
import json


@pytest.mark.integration
class TestInvalidInputError:
    """Integration tests for Invalid input error handling"""

    def test_echo_invalid_json_workflow(self, client):
        """Test Echo endpoint with invalid JSON"""
        # Arrange - User submits malformed JSON
        invalid_json = '{"text": "Hello"'  # Missing closing brace

        # Act - User submits invalid JSON to echo endpoint
        response = client.post(
            "/api/echo", data=invalid_json, content_type="application/json"
        )

        # Assert - User receives appropriate error for malformed JSON
        assert response.status_code == 400

    def test_add_invalid_parameter_types_workflow(self, client):
        """Test Add endpoint with invalid parameter types"""
        # Arrange - User submits non-numeric/string values
        payload = {"x": {"nested": "object"}, "y": ["array", "value"]}

        # Act - User submits complex objects to add endpoint
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives validation error
        assert response.status_code == 400
        data = response.get_json()
        assert data["success"] is False
        assert "error" in data

    def test_calculate_invalid_operation_workflow(self, client):
        """Test Calculate endpoint with invalid operation"""
        # Arrange - User submits unsupported operation
        payload = {"x": 10.0, "y": 5.0, "operation": "power"}

        # Act - User submits unsupported operation to calculate endpoint
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives error for unsupported operation
        assert response.status_code == 400
        data = response.get_json()
        assert data["success"] is False
        assert "error" in data
        assert (
            "operation" in data["error"].lower() or "invalid" in data["error"].lower()
        )

    def test_calculate_non_string_operation_workflow(self, client):
        """Test Calculate endpoint with non-string operation"""
        # Arrange - User submits numeric operation value
        payload = {"x": 10.0, "y": 5.0, "operation": 123}

        # Act - User submits numeric operation to calculate endpoint
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives validation error
        assert response.status_code == 400
        data = response.get_json()
        assert data["success"] is False
        assert "error" in data

    def test_echo_missing_content_type_workflow(self, client):
        """Test Echo endpoint without JSON content type"""
        # Arrange - User submits data without proper content type
        payload = {"text": "Hello"}

        # Act - User submits without JSON content type
        response = client.post("/api/echo", data=json.dumps(payload))

        # Assert - Should handle gracefully or return appropriate error
        assert response.status_code in [
            400,
            415,
        ]  # Bad Request or Unsupported Media Type

    def test_add_extremely_large_numbers_workflow(self, client):
        """Test Add endpoint with extremely large numbers"""
        # Arrange - User submits very large numbers
        payload = {"x": 1e308, "y": 1e308}  # Near float max

        # Act - User submits extremely large numbers
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Should handle gracefully (may overflow or return error)
        if response.status_code == 200:
            data = response.get_json()
            # If successful, result should be valid
            assert "result" in data
        else:
            # If error, should be appropriate error response
            assert response.status_code == 400
            data = response.get_json()
            assert data["success"] is False
            assert "error" in data

    def test_calculate_infinity_inputs_workflow(self, client):
        """Test Calculate endpoint with infinity values"""
        # Arrange - User submits infinity values (if supported by JSON)
        payload = {"x": float("inf"), "y": 5.0, "operation": "add"}

        # Act - User submits infinity value
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Should handle gracefully or return error
        if response.status_code == 200:
            data = response.get_json()
            assert "result" in data
        else:
            assert response.status_code == 400
            data = response.get_json()
            assert data["success"] is False
            assert "error" in data

    def test_echo_null_values_workflow(self, client):
        """Test Echo endpoint with null text value"""
        # Arrange - User submits null text
        payload = {"text": None}

        # Act - User submits null text value
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives validation error
        assert response.status_code == 400
        data = response.get_json()
        assert data["success"] is False
        assert "error" in data

    def test_endpoints_with_extra_fields_workflow(self, client):
        """Test endpoints with unexpected extra fields"""
        # Arrange - User submits valid data with extra fields
        echo_payload = {"text": "Hello", "extra": "field"}
        add_payload = {"x": 5, "y": 3, "unexpected": "data"}
        calc_payload = {"x": 10, "y": 5, "operation": "add", "extra": "field"}

        # Act & Assert - Echo endpoint with extra field
        response = client.post(
            "/api/echo", data=json.dumps(echo_payload), content_type="application/json"
        )
        # Should either ignore extra fields or return error gracefully
        assert response.status_code in [200, 400]

        # Act & Assert - Add endpoint with extra field
        response = client.post(
            "/api/add", data=json.dumps(add_payload), content_type="application/json"
        )
        assert response.status_code in [200, 400]

        # Act & Assert - Calculate endpoint with extra field
        response = client.post(
            "/api/calculate",
            data=json.dumps(calc_payload),
            content_type="application/json",
        )
        assert response.status_code in [200, 400]

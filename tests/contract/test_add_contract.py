"""
Contract tests for POST /api/add endpoint
Tests API contract compliance according to OpenAPI specification
"""

import pytest
import json


@pytest.mark.contract
class TestAddContract:
    """Contract tests for /api/add endpoint"""

    def test_add_success_response_structure(self, client):
        """Test successful add response matches contract schema"""
        # Arrange
        payload = {"x": 5.5, "y": 3.2}

        # Act
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 200
        data = response.get_json()

        # Verify response structure matches AddResponse schema
        assert "result" in data
        assert "success" in data
        assert data["success"] is True
        assert data["result"] == 8.7
        assert "error" not in data or data["error"] is None

    def test_add_integer_inputs(self, client):
        """Test add endpoint with integer inputs"""
        # Arrange
        payload = {"x": 10, "y": 20}

        # Act
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == 30

    def test_add_negative_numbers(self, client):
        """Test add endpoint with negative numbers"""
        # Arrange
        payload = {"x": -5.5, "y": 3.2}

        # Act
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == -2.3

    def test_add_missing_parameter_x_error(self, client):
        """Test missing parameter 'x' returns 400 error"""
        # Arrange
        payload = {"y": 5.0}

        # Act
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
        assert "success" in data
        assert data["success"] is False
        assert "result" not in data or data["result"] is None

    def test_add_missing_parameter_y_error(self, client):
        """Test missing parameter 'y' returns 400 error"""
        # Arrange
        payload = {"x": 5.0}

        # Act
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
        assert data["success"] is False
        assert "result" not in data or data["result"] is None

    def test_add_string_concatenation_mixed_x(self, client):
        """Test string concatenation when x is string and y is number"""
        # Arrange
        payload = {"x": "invalid", "y": 5.0}

        # Act
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == "invalid5.0"

    def test_add_string_concatenation_mixed_y(self, client):
        """Test string concatenation when x is number and y is string"""
        # Arrange
        payload = {"x": 5.0, "y": "invalid"}

        # Act
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == "5.0invalid"

    def test_add_string_concatenation_both_strings(self, client):
        """Test string concatenation when both parameters are strings"""
        # Arrange
        payload = {"x": "hello", "y": "world"}

        # Act
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == "helloworld"

    def test_add_numeric_strings(self, client):
        """Test numeric addition when both parameters are numeric strings"""
        # Arrange
        payload = {"x": "10", "y": "20"}

        # Act
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == 30.0

    def test_add_empty_payload_error(self, client):
        """Test empty payload returns 400 error"""
        # Arrange
        payload = {}

        # Act
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 400
        data = response.get_json()
        assert data["success"] is False
        assert "error" in data

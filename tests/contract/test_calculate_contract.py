"""
Contract tests for POST /api/calculate endpoint
Tests API contract compliance according to OpenAPI specification
"""

import pytest
import json


@pytest.mark.contract
class TestCalculateContract:
    """Contract tests for /api/calculate endpoint"""

    def test_calculate_add_success_response(self, client):
        """Test successful add calculation response matches contract schema"""
        # Arrange
        payload = {"x": 10.0, "y": 5.0, "operation": "add"}

        # Act
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 200
        data = response.get_json()

        # Verify response structure matches CalculateResponse schema
        assert "result" in data
        assert "success" in data
        assert data["success"] is True
        assert data["result"] == 15.0
        assert "error" not in data or data["error"] is None

    def test_calculate_subtract_success_response(self, client):
        """Test successful subtract calculation response"""
        # Arrange
        payload = {"x": 10.0, "y": 3.0, "operation": "subtract"}

        # Act
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == 7.0

    def test_calculate_multiply_success_response(self, client):
        """Test successful multiply calculation response"""
        # Arrange
        payload = {"x": 4.0, "y": 3.0, "operation": "multiply"}

        # Act
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == 12.0

    def test_calculate_divide_success_response(self, client):
        """Test successful divide calculation response"""
        # Arrange
        payload = {"x": 15.0, "y": 3.0, "operation": "divide"}

        # Act
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == 5.0

    def test_calculate_divide_by_zero_error(self, client):
        """Test divide by zero returns appropriate error"""
        # Arrange
        payload = {"x": 10.0, "y": 0.0, "operation": "divide"}

        # Act
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - could be 200 with error message or 400, depending on implementation
        data = response.get_json()
        if response.status_code == 200:
            # Business error returned as success response with error field
            assert data["success"] is False
            assert "error" in data
            assert "zero" in data["error"].lower() or "divide" in data["error"].lower()
            assert data["result"] is None
        else:
            # HTTP error response
            assert response.status_code == 400
            assert data["success"] is False
            assert "error" in data

    def test_calculate_invalid_operation_error(self, client):
        """Test invalid operation returns 400 error"""
        # Arrange
        payload = {"x": 5.0, "y": 3.0, "operation": "invalid"}

        # Act
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 400
        data = response.get_json()
        assert data["success"] is False
        assert "error" in data

    def test_calculate_missing_parameter_a_error(self, client):
        """Test missing parameter 'x' returns 400 error"""
        # Arrange
        payload = {"y": 5.0, "operation": "add"}

        # Act
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 400
        data = response.get_json()
        assert data["success"] is False
        assert "error" in data

    def test_calculate_missing_parameter_b_error(self, client):
        """Test missing parameter 'y' returns 400 error"""
        # Arrange
        payload = {"x": 5.0, "operation": "add"}

        # Act
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 400
        data = response.get_json()
        assert data["success"] is False
        assert "error" in data

    def test_calculate_missing_operation_error(self, client):
        """Test missing operation parameter returns 400 error"""
        # Arrange
        payload = {"x": 5.0, "y": 3.0}

        # Act
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert
        assert response.status_code == 400
        data = response.get_json()
        assert data["success"] is False
        assert "error" in data

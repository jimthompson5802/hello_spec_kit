"""
Integration tests for Division by zero error handling
Tests the complete user workflow when attempting division by zero
"""

import pytest
import json


@pytest.mark.integration
class TestDivisionByZeroError:
    """Integration tests for Division by zero error handling"""

    def test_division_by_zero_workflow(self, client):
        """Test complete workflow when user attempts division by zero"""
        # Arrange - User attempts to divide by zero
        payload = {"x": 10.0, "y": 0.0, "operation": "divide"}

        # Act - User submits division by zero request via /api/calculate endpoint
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives appropriate error handling
        data = response.get_json()

        # Could be 200 with error message or 400 depending on implementation
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

    def test_division_by_zero_negative_dividend_workflow(self, client):
        """Test division by zero with negative dividend"""
        # Arrange - User attempts to divide negative number by zero
        payload = {"x": -15.5, "y": 0.0, "operation": "divide"}

        # Act - User submits negative division by zero request
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Error handling works for negative numbers too
        data = response.get_json()

        if response.status_code == 200:
            assert data["success"] is False
            assert "error" in data
            assert "zero" in data["error"].lower() or "divide" in data["error"].lower()
            assert data["result"] is None
        else:
            assert response.status_code == 400
            assert data["success"] is False
            assert "error" in data

    def test_division_by_zero_large_dividend_workflow(self, client):
        """Test division by zero with large dividend"""
        # Arrange - User attempts to divide large number by zero
        payload = {"x": 1000000.0, "y": 0.0, "operation": "divide"}

        # Act - User submits large number division by zero request
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Error handling works for large numbers too
        data = response.get_json()

        if response.status_code == 200:
            assert data["success"] is False
            assert "error" in data
            assert "zero" in data["error"].lower() or "divide" in data["error"].lower()
            assert data["result"] is None
        else:
            assert response.status_code == 400
            assert data["success"] is False
            assert "error" in data

    def test_division_by_zero_fractional_dividend_workflow(self, client):
        """Test division by zero with fractional dividend"""
        # Arrange - User attempts to divide fractional number by zero
        payload = {"x": 0.5, "y": 0.0, "operation": "divide"}

        # Act - User submits fractional division by zero request
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Error handling works for fractional numbers
        data = response.get_json()

        if response.status_code == 200:
            assert data["success"] is False
            assert "error" in data
            assert "zero" in data["error"].lower() or "divide" in data["error"].lower()
            assert data["result"] is None
        else:
            assert response.status_code == 400
            assert data["success"] is False
            assert "error" in data

    def test_division_by_zero_integer_inputs_workflow(self, client):
        """Test division by zero with integer inputs"""
        # Arrange - User attempts to divide integer by zero
        payload = {"x": 42, "y": 0, "operation": "divide"}

        # Act - User submits integer division by zero request
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Error handling works for integer inputs
        data = response.get_json()

        if response.status_code == 200:
            assert data["success"] is False
            assert "error" in data
            assert "zero" in data["error"].lower() or "divide" in data["error"].lower()
            assert data["result"] is None
        else:
            assert response.status_code == 400
            assert data["success"] is False
            assert "error" in data

    def test_zero_divided_by_zero_workflow(self, client):
        """Test special case of zero divided by zero"""
        # Arrange - User attempts to divide zero by zero
        payload = {"x": 0.0, "y": 0.0, "operation": "divide"}

        # Act - User submits zero divided by zero request
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - This is undefined mathematically, should return error
        data = response.get_json()

        if response.status_code == 200:
            assert data["success"] is False
            assert "error" in data
            # Could be "division by zero" or "undefined" error
            error_msg = data["error"].lower()
            assert (
                "zero" in error_msg
                or "undefined" in error_msg
                or "invalid" in error_msg
                or "indeterminate" in error_msg
            )
            assert data["result"] is None
        else:
            assert response.status_code == 400
            assert data["success"] is False
            assert "error" in data

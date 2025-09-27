"""
Integration tests for Calculator function basic flow
Tests the complete user workflow for the Calculator functionality
"""

import pytest
import json


@pytest.mark.integration
class TestCalculatorBasicFlow:
    """Integration tests for Calculator function basic flow"""

    def test_calculator_add_workflow_success(self, client):
        """Test complete Calculator Add workflow: user enters numbers and gets sum"""
        # Arrange - User wants to add two numbers
        payload = {"x": 10.5, "y": 5.3, "operation": "add"}

        # Act - User submits addition request via /api/calculate endpoint
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives correct sum
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == 15.8
        assert data["error"] is None

    def test_calculator_subtract_workflow_success(self, client):
        """Test complete Calculator Subtract workflow"""
        # Arrange - User wants to subtract two numbers
        payload = {"x": 20.0, "y": 8.5, "operation": "subtract"}

        # Act - User submits subtraction request via /api/calculate endpoint
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives correct difference
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == 11.5
        assert data["error"] is None

    def test_calculator_multiply_workflow_success(self, client):
        """Test complete Calculator Multiply workflow"""
        # Arrange - User wants to multiply two numbers
        payload = {"x": 7.0, "y": 3.0, "operation": "multiply"}

        # Act - User submits multiplication request via /api/calculate endpoint
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives correct product
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == 21.0
        assert data["error"] is None

    def test_calculator_divide_workflow_success(self, client):
        """Test complete Calculator Divide workflow"""
        # Arrange - User wants to divide two numbers
        payload = {"x": 15.0, "y": 3.0, "operation": "divide"}

        # Act - User submits division request via /api/calculate endpoint
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - User receives correct quotient
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == 5.0
        assert data["error"] is None

    def test_calculator_integer_inputs_workflow(self, client):
        """Test Calculator workflow with integer inputs"""
        # Arrange - User enters integer values
        payload = {"x": 100, "y": 25, "operation": "divide"}

        # Act - User submits request with integer inputs
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Calculator handles integers correctly
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == 4.0
        assert data["error"] is None

    def test_calculator_negative_numbers_workflow(self, client):
        """Test Calculator workflow with negative numbers"""
        # Arrange - User enters negative numbers
        payload = {"x": -10.5, "y": 5.0, "operation": "add"}

        # Act - User submits request with negative numbers
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Calculator handles negative numbers correctly
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == -5.5
        assert data["error"] is None

    def test_calculator_zero_values_workflow(self, client):
        """Test Calculator workflow with zero values"""
        # Arrange - User enters zero as one operand
        payload = {"x": 0.0, "y": 10.0, "operation": "multiply"}

        # Act - User submits request with zero value
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Calculator handles zero correctly
        assert response.status_code == 200
        data = response.get_json()

        assert data["success"] is True
        assert data["result"] == 0.0
        assert data["error"] is None

    def test_calculator_divide_by_zero_workflow(self, client):
        """Test Calculator workflow when user attempts to divide by zero"""
        # Arrange - User attempts division by zero
        payload = {"x": 10.0, "y": 0.0, "operation": "divide"}

        # Act - User submits division by zero request
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

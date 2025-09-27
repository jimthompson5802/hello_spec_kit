"""
Integration tests for Interface mode switching
Tests the complete user workflow for switching between Echo and Compute modes
Note: This focuses on the backend API behavior that supports mode switching
"""

import pytest
import json


@pytest.mark.integration
class TestModeSwitching:
    """Integration tests for Interface mode switching"""

    def test_echo_mode_functionality_workflow(self, client):
        """Test complete workflow for Echo mode functionality"""
        # Arrange - User is in Echo mode and wants to echo text
        payload = {"text": "Testing Echo Mode"}

        # Act - User uses Echo functionality via /api/echo endpoint
        response = client.post(
            "/api/echo", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Echo mode works correctly
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == "YOU ENTERED: Testing Echo Mode"
        assert data["error"] is None

    def test_compute_mode_add_functionality_workflow(self, client):
        """Test complete workflow for Compute mode add functionality"""
        # Arrange - User is in Compute mode and wants to add numbers
        payload = {"x": 15.5, "y": 10.3}

        # Act - User uses Add functionality via /api/add endpoint
        response = client.post(
            "/api/add", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Compute mode add works correctly
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == 25.8
        assert data["error"] is None

    def test_compute_mode_calculate_functionality_workflow(self, client):
        """Test complete workflow for Compute mode calculate functionality"""
        # Arrange - User is in Compute mode and wants to perform calculation
        payload = {"x": 20.0, "y": 4.0, "operation": "multiply"}

        # Act - User uses Calculate functionality via /api/calculate endpoint
        response = client.post(
            "/api/calculate", data=json.dumps(payload), content_type="application/json"
        )

        # Assert - Compute mode calculate works correctly
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == 80.0
        assert data["error"] is None

    def test_mode_switching_sequence_workflow(self, client):
        """Test workflow when user switches between modes in sequence"""
        # Simulate user switching from Echo to Compute to Echo mode

        # Phase 1: User starts with Echo mode
        echo_payload = {"text": "First Echo"}
        response = client.post(
            "/api/echo", data=json.dumps(echo_payload), content_type="application/json"
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == "YOU ENTERED: First Echo"

        # Phase 2: User switches to Compute mode (Add)
        add_payload = {"x": 5, "y": 7}
        response = client.post(
            "/api/add", data=json.dumps(add_payload), content_type="application/json"
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == 12

        # Phase 3: User continues with Compute mode (Calculate)
        calc_payload = {"x": 100, "y": 10, "operation": "divide"}
        response = client.post(
            "/api/calculate",
            data=json.dumps(calc_payload),
            content_type="application/json",
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == 10.0

        # Phase 4: User switches back to Echo mode
        echo_payload2 = {"text": "Back to Echo"}
        response = client.post(
            "/api/echo", data=json.dumps(echo_payload2), content_type="application/json"
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert data["result"] == "YOU ENTERED: Back to Echo"

    def test_concurrent_mode_usage_workflow(self, client):
        """Test workflow simulating concurrent mode usage (stateless behavior)"""
        # This tests that the backend is stateless and can handle mixed requests

        # Simulate rapid switching between modes (as if multiple users or quick UI switches)
        requests_and_expectations = [
            ("echo", {"text": "Test 1"}, "YOU ENTERED: Test 1"),
            ("add", {"x": 10, "y": 5}, 15),
            ("echo", {"text": "Test 2"}, "YOU ENTERED: Test 2"),
            ("calculate", {"x": 8, "y": 2, "operation": "subtract"}, 6),
            ("add", {"x": 3.5, "y": 1.5}, 5.0),
            ("echo", {"text": "Final Test"}, "YOU ENTERED: Final Test"),
        ]

        for mode, payload, expected_result in requests_and_expectations:
            if mode == "echo":
                endpoint = "/api/echo"
            elif mode == "add":
                endpoint = "/api/add"
            elif mode == "calculate":
                endpoint = "/api/calculate"
            else:
                raise ValueError(f"Unknown mode: {mode}")

            response = client.post(
                endpoint, data=json.dumps(payload), content_type="application/json"
            )

            assert response.status_code == 200
            data = response.get_json()
            assert data["success"] is True
            assert data["result"] == expected_result
            assert data["error"] is None

    def test_mode_specific_error_handling_workflow(self, client):
        """Test error handling is consistent across modes"""
        # Test Echo mode error handling
        echo_error_payload = {"text": ""}
        response = client.post(
            "/api/echo",
            data=json.dumps(echo_error_payload),
            content_type="application/json",
        )
        assert response.status_code == 400
        data = response.get_json()
        assert data["success"] is False
        assert "error" in data

        # Test Add mode error handling
        add_error_payload = {"x": "invalid"}  # Missing 'b' and invalid type
        response = client.post(
            "/api/add",
            data=json.dumps(add_error_payload),
            content_type="application/json",
        )
        assert response.status_code == 400
        data = response.get_json()
        assert data["success"] is False
        assert "error" in data

        # Test Calculate mode error handling
        calc_error_payload = {"x": 10, "y": 0, "operation": "divide"}
        response = client.post(
            "/api/calculate",
            data=json.dumps(calc_error_payload),
            content_type="application/json",
        )
        data = response.get_json()
        # Division by zero should be handled gracefully
        if response.status_code == 200:
            assert data["success"] is False
            assert "error" in data
        else:
            assert response.status_code == 400
            assert data["success"] is False
            assert "error" in data

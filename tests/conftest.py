"""Test configuration for MEP estimation pipeline."""
import pytest
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture
def sample_quantities():
    """Sample quantity data for testing."""
    return [
        {"item": "conduit 1 inch PVC", "type": "length", "value": 100, "unit": "ft"},
        {"item": "electrical box", "type": "count", "value": 50, "unit": "each"},
        {"item": "conduit support", "type": "count", "value": 80, "unit": "each"},
    ]

@pytest.fixture
def sample_cost_result():
    """Sample cost result for testing."""
    return {
        "work_id": "ELEC-001",
        "resource_id": "PVC-CONDUIT-1IN",
        "unit_cost": 2.50,
        "total_cost": 250.00,
        "confidence": 0.95,
    }
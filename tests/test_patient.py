"""Tests for the Patient model."""

from inflammation.models import Patient
import numpy.testing as npt
import pytest

def test_create_patient():
    name = 'Alice'
    w = 50
    h = 1.8
    p = Patient(name=name, weight=w, height=h)

    assert p.name == name
    assert p.weight == w
    assert p.height == h

def test_compute_bmi():
    name = 'Maria'
    w = 60
    h = 1.6
    p = Patient(name=name, weight=w, height=h)
    bmi = 23.4375
    
    npt.assert_almost_equal(p.get_body_mass_index(), bmi)

@pytest.mark.parametrize("name, weight, height, expected", [
    ("Alice",  80, 1.7,  True),   # BMI ≈ 27.7 → overweight
    ("Bob",    60, 1.8,  False),  # BMI ≈ 18.5 → not overweight
    ("Carol",  68, 1.65, False),   # BMI ≈ 25.0 → not overweight (boundary)
    ("David",  67, 1.65, False),  # BMI ≈ 24.6 → not overweight
])
def test_is_overweight(name, weight, height, expected):
    """Test that is_overweight returns the correct boolean for various BMI values."""
    patient = Patient(name=name, weight=weight, height=height)
    assert patient.is_overweight() == expected
"""Tests for the Patient model."""

from inflammation.models import Patient
import numpy.testing as npt

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
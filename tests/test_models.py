"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_max


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""

    test_input = np.array([[0, 0], [0, 0], [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2], [3, 4], [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_max_integers():
    """Tests that the max function works for an array of negative integers."""
    test_input = np.array([[1, -2], [3, -4], [5, -6]])
    test_result = np.array([5, -2])

    # Need to use Numpy testing functions to find max value in axis=0 of the array
    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_max_string():
    """Tests for TypeError when parsing strings."""
    with pytest.raises(TypeError):
        error_expected = daily_max(["Hello", "there"])


def test_daily_mean_real_numbers():
    """Test that mean function works for an array of real numbers."""

    test_input = np.array([[1.5, 1.445], [3.6, 8.5], [5.4, -5.334]])
    test_result = np.array([3.5, 1.5370000000000001])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


@pytest.mark.parametrize(
    "test_input, test_result",
    [([[0, 0], [0, 0], [0, 0]], [0, 0]), ([[1, 2], [3, 4], [5, 6]], [3, 4])],
)
def test_daily_mean(test_input, test_result):
    """Test that mean function works for both zeroes and integers."""
    npt.assert_array_equal(daily_mean(test_input), test_result)


@pytest.mark.parametrize(
    "test_input, test_result",
    [([[0, 0], [0, 0], [0, 0]], [0, 0]), ([[1, -2], [3, -4], [5, -6]], [5, -2])],
)
def test_daily_max(test_input, test_result):
    """Test that "max" function works for both zeroes and integers."""
    npt.assert_array_equal(daily_max(test_input), test_result)

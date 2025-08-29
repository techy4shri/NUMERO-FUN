# flake8: noqa: E501
"""
Tests for the calculator module
"""

from numero_fun.calculator import (
    letter_to_number,
    letter_to_chaldean,
    letter_to_pythagorean,
    get_sum,
    get_pythagorean_sum,
    calculate_number,
)


def test_letter_to_number():
    assert letter_to_number("a") == 1
    assert letter_to_number("g") == 7
    assert letter_to_number("j") == 1
    assert letter_to_number("z") == 8
    assert letter_to_number(" ") == 0
    assert letter_to_number("!") == 0


def test_get_sum():
    assert get_sum(123) == 6
    assert get_sum(999) == 27
    assert get_sum(456) == 15
    assert get_sum(0) == 0
    assert get_sum(100345) == 13


def test_calculate_number():
    assert calculate_number("john") == 2  # j(1)+o(6)+h(8)+n(5)=20 -> 2+0=2
    assert calculate_number("doe") == 6  # d(4)+o(6)+e(5)=15 -> 1+5=6
    assert calculate_number("john doe") == 8
    assert calculate_number("JOHN") == 2  # Should work with uppercase too


def test_chaldean_numerology():
    assert (
        calculate_number("john", "chaldean") == 9
    )  # j(1)+o(7)+h(5)+n(5)=18 -> 1+8=9 -> 9
    assert calculate_number("doe", "chaldean") == 7  # d(4)+o(7)+e(5)=16 -> 1+6=7


def test_pythagorean_numerology():
    assert calculate_number("anna", "pythagorean") == 3  # Preserves master number
    assert (
        calculate_number("john", "pythagorean") == 2
    )  # j(1)+o(6)+h(8)+n(5)=20 -> 2+0=2

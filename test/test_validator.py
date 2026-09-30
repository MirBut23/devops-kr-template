"""Regression tests for email, phone and the instructor's SNILS validator."""

import pytest

from validator import validate_email, validate_phone, validate_snils


@pytest.mark.parametrize("email, expected", [
    ("test@example.com", True), ("invalid", False),
    ("name+tag@example.org", True), ("name@", False),
])
def test_validate_email(email: str, expected: bool) -> None:
    assert validate_email(email) is expected


@pytest.mark.parametrize("phone, expected", [
    ("+79991234567", True), ("79991234567", True),
    ("7 999-123-45-67", True), ("89991234567", False),
    ("+7999123", False), ("", False), ("+799912345678", False),
    ("+7abcdefghij", False),
])
def test_validate_phone(phone: str, expected: bool) -> None:
    assert validate_phone(phone) is expected


@pytest.mark.parametrize("snils, expected", [
    ("11223344595", True), ("001-001-999 65", True),
    ("001-001-999 32", False),  # Weighted sum is 65, not 32.
    ("123", False), ("123456789012", False),
    ("abcdefghijk", False), ("11223344500", False),
])
def test_validate_snils(snils: str, expected: bool) -> None:
    assert validate_snils(snils) is expected

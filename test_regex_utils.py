"""Tests for regex_utils."""

import regex_utils as ru


def test_is_email():
    assert ru.is_email("user@example.com")
    assert ru.is_email("first.last+tag@sub.domain.co")
    assert not ru.is_email("no-at-sign.com")
    assert not ru.is_email("user@nodot")
    assert not ru.is_email("@example.com")


def test_is_ipv4():
    assert ru.is_ipv4("0.0.0.0")
    assert ru.is_ipv4("192.168.1.1")
    assert ru.is_ipv4("255.255.255.255")
    assert not ru.is_ipv4("256.1.1.1")
    assert not ru.is_ipv4("1.2.3")
    assert not ru.is_ipv4("1.2.3.4.5")


def test_is_hex_color():
    assert ru.is_hex_color("#fff")
    assert ru.is_hex_color("#FFFFFF")
    assert ru.is_hex_color("#1a2b3c")
    assert not ru.is_hex_color("fff")
    assert not ru.is_hex_color("#ggg")
    assert not ru.is_hex_color("#12345")


def test_is_us_phone():
    # Accepted formats
    assert ru.is_us_phone("(555) 123-4567")
    assert ru.is_us_phone("555-123-4567")
    assert ru.is_us_phone("555.123.4567")
    assert ru.is_us_phone("5551234567")
    assert ru.is_us_phone("+1 555 123 4567")
    assert ru.is_us_phone("1-555-123-4567")
    # Rejected
    assert not ru.is_us_phone("123-4567")        # missing area code
    assert not ru.is_us_phone("555-123-456")     # too few digits
    assert not ru.is_us_phone("555-123-45678")   # too many digits
    assert not ru.is_us_phone("abc-def-ghij")    # non-numeric

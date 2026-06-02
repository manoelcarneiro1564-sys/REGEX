"""Tests for regex_utils.

Written as ``unittest.TestCase`` classes so the suite is discoverable by the
standard library runner (``python -m unittest discover``) as well as by
``pytest``. Plain ``def test_*`` functions are *not* collected by unittest, so
using ``TestCase`` keeps both runners working without extra dependencies.
"""

import unittest

import regex_utils as ru


class IsEmailTests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(ru.is_email("user@example.com"))
        self.assertTrue(ru.is_email("first.last+tag@sub.domain.co"))

    def test_invalid(self):
        self.assertFalse(ru.is_email("no-at-sign.com"))
        self.assertFalse(ru.is_email("user@nodot"))
        self.assertFalse(ru.is_email("@example.com"))


class IsIpv4Tests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(ru.is_ipv4("0.0.0.0"))
        self.assertTrue(ru.is_ipv4("192.168.1.1"))
        self.assertTrue(ru.is_ipv4("255.255.255.255"))

    def test_invalid(self):
        self.assertFalse(ru.is_ipv4("256.1.1.1"))
        self.assertFalse(ru.is_ipv4("1.2.3"))
        self.assertFalse(ru.is_ipv4("1.2.3.4.5"))


class IsHexColorTests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(ru.is_hex_color("#fff"))
        self.assertTrue(ru.is_hex_color("#FFFFFF"))
        self.assertTrue(ru.is_hex_color("#1a2b3c"))

    def test_invalid(self):
        self.assertFalse(ru.is_hex_color("fff"))
        self.assertFalse(ru.is_hex_color("#ggg"))
        self.assertFalse(ru.is_hex_color("#12345"))


class IsUsPhoneTests(unittest.TestCase):
    def test_accepted_formats(self):
        self.assertTrue(ru.is_us_phone("(555) 123-4567"))
        self.assertTrue(ru.is_us_phone("555-123-4567"))
        self.assertTrue(ru.is_us_phone("555.123.4567"))
        self.assertTrue(ru.is_us_phone("5551234567"))
        self.assertTrue(ru.is_us_phone("+1 555 123 4567"))
        self.assertTrue(ru.is_us_phone("1-555-123-4567"))

    def test_rejected(self):
        self.assertFalse(ru.is_us_phone("123-4567"))      # missing area code
        self.assertFalse(ru.is_us_phone("555-123-456"))   # too few digits
        self.assertFalse(ru.is_us_phone("555-123-45678"))  # too many digits
        self.assertFalse(ru.is_us_phone("abc-def-ghij"))  # non-numeric


if __name__ == "__main__":
    unittest.main()

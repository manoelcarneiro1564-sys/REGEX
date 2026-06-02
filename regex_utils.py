"""A small collection of regex-based validation and extraction helpers.

Each helper compiles its pattern once at import time and exposes a simple,
well-documented function. Patterns aim to be practical rather than fully
RFC-exhaustive.
"""

import re

# --- Patterns -------------------------------------------------------------

_EMAIL_RE = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

_IPV4_RE = re.compile(
    r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
    r"(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$"
)

_HEX_COLOR_RE = re.compile(r"^#(?:[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$")

_US_PHONE_RE = re.compile(
    r"^(?:\+?1[\s.-]?)?"          # optional country code: +1, 1, with sep
    r"(?:\(\d{3}\)|\d{3})"        # area code, optionally parenthesized
    r"[\s.-]?"                    # optional separator
    r"\d{3}"                      # exchange
    r"[\s.-]?"                    # optional separator
    r"\d{4}$"                     # subscriber number
)


# --- Helpers --------------------------------------------------------------

def is_email(value: str) -> bool:
    """Return True if ``value`` looks like a valid email address."""
    return bool(_EMAIL_RE.match(value))


def is_ipv4(value: str) -> bool:
    """Return True if ``value`` is a dotted-quad IPv4 address (0-255 octets)."""
    return bool(_IPV4_RE.match(value))


def is_hex_color(value: str) -> bool:
    """Return True if ``value`` is a #RGB or #RRGGBB hex color."""
    return bool(_HEX_COLOR_RE.match(value))


def is_us_phone(value: str) -> bool:
    """Return True if ``value`` is a US phone number.

    Accepts common formats such as ``(555) 123-4567``, ``555-123-4567``,
    ``555.123.4567``, ``5551234567`` and an optional ``+1`` / ``1`` country
    code prefix.
    """
    return bool(_US_PHONE_RE.match(value))


def is_slug(value: str) -> bool:
    """Return True if ``value`` is a URL slug (lowercase, hyphen-separated).

    TODO: implement slug validation (e.g. ``my-blog-post-1``): lowercase
    letters, digits and single hyphens, no leading/trailing hyphen.
    """
    raise NotImplementedError

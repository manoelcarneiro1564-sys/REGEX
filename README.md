# REGEX

A small collection of practical regex-based validation helpers in Python.

## Available helpers

| Function | Description |
| --- | --- |
| `is_email(value)` | Validate an email address. |
| `is_ipv4(value)` | Validate a dotted-quad IPv4 address (octets 0–255). |
| `is_hex_color(value)` | Validate a `#RGB` or `#RRGGBB` hex color. |
| `is_us_phone(value)` | Validate a US phone number in common formats. |
| `is_slug(value)` | Validate a URL slug. *(not yet implemented — see TODO)* |

## Usage

```python
import regex_utils as ru

ru.is_email("user@example.com")      # True
ru.is_us_phone("(555) 123-4567")     # True
ru.is_ipv4("256.1.1.1")              # False
```

## Running the tests

```bash
python -m pytest          # if pytest is installed
# or, without pytest:
python -m unittest discover -p "test_*.py"
```

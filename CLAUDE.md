# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) and other AI
assistants when working with code in this repository.

## Overview

**REGEX** is a small, dependency-free Python library of practical
regex-based **validation helpers**. Each helper takes a string and returns a
`bool` indicating whether the input matches a given format (email, IPv4,
hex color, US phone number, URL slug). Patterns aim to be *practical* rather
than fully RFC-exhaustive.

The codebase is intentionally tiny and has no external runtime dependencies —
it uses only the Python standard library (`re`).

## Project structure

```
.
├── regex_utils.py        # The library: compiled patterns + validation helpers
├── test_regex_utils.py   # Tests (runnable with pytest or unittest)
└── README.md             # User-facing overview, helper table, usage examples
```

There is no package manifest (`pyproject.toml` / `setup.py`), no build step,
and no configured linter/formatter. The module is imported directly by file
name (`import regex_utils`), so code and tests must sit in the same directory
(or on `sys.path`).

## Common commands

```bash
# Run the full test suite (preferred)
python -m pytest

# Run tests without pytest installed (stdlib only)
python -m unittest discover -p "test_*.py"

# Run a single test function
python -m pytest test_regex_utils.py::test_is_email

# Quick manual smoke check
python -c "import regex_utils as ru; print(ru.is_email('user@example.com'))"
```

There are no install, build, or lint commands — the project is pure standard
library. Requires Python 3 (developed/tested against CPython 3.11).

## Architecture & conventions

The design pattern in `regex_utils.py` is deliberately uniform; **follow it
when adding new helpers**:

1. **Compile patterns once at import time** as module-level constants named
   `_<NAME>_RE` (leading underscore = private). Group these in the
   `# --- Patterns ---` section near the top of the file.
2. **Use verbose, multi-line raw-string patterns with inline comments** for
   anything non-trivial (see `_US_PHONE_RE`), so the regex stays readable.
3. **Expose a thin public function** `is_<thing>(value: str) -> bool` in the
   `# --- Helpers ---` section that returns `bool(_<NAME>_RE.match(value))`.
4. **Anchor patterns** with `^...$` so the *entire* string must match, and
   pair them with `.match()` (the helpers rely on full-string anchoring, not
   on `.fullmatch()`).
5. **Write a one-line docstring** (imperative/descriptive) for every public
   helper. Document accepted/rejected formats when they are non-obvious.

### Style notes
- Type hints on all public functions (`value: str -> bool`).
- Public API is snake_case `is_*` predicates; internal patterns are
  `_UPPER_SNAKE_RE`.
- Keep validators practical, not exhaustively RFC-compliant — but make the
  trade-off explicit in the docstring.

## Testing conventions

- Tests live in `test_regex_utils.py` and import the module as
  `import regex_utils as ru`.
- One `test_<helper>` function per helper, using plain `assert` statements
  (works under both pytest and unittest discovery — no test classes needed).
- **Every test covers both accepted and rejected inputs.** When adding or
  changing a helper, add positive *and* negative cases, including boundary
  values (e.g. IPv4 octet `255` vs `256`, phone digit-count edges).

## Known TODO

- `is_slug(value)` is declared but **not implemented** — it currently raises
  `NotImplementedError`. The intended behavior (per its docstring) is to
  validate URL slugs like `my-blog-post-1`: lowercase letters, digits, and
  single hyphens, with no leading or trailing hyphen. The README marks it as
  *"not yet implemented"*. If you implement it, also add tests and update the
  README's helper table.

## Development workflow

### Branching
- Active development for the current task is on `claude/claude-md-docs-eso0U`.
- Create feature branches for new work; never push directly to the default
  branch without explicit permission.

### Commits
- Use clear, descriptive, imperative-mood messages (e.g. "Implement is_slug
  validator", not "added stuff").
- Keep commits focused and logically scoped. When you change a helper, update
  its tests and the README in the same change.

### Pull requests
- Do **not** open a pull request unless the user explicitly asks for one.

## Notes for AI assistants

- **Keep this file truthful.** It must always reflect the real state of the
  repository. If you add, remove, or change helpers, update the relevant
  sections (structure, TODO, commands) in the same change.
- **Don't fabricate.** Do not document commands, files, or APIs that do not
  exist. Verify against the actual tree before writing.
- **Match the existing pattern** described in *Architecture & conventions*
  rather than introducing new idioms.
- **Avoid build/dependency creep.** This project is intentionally
  zero-dependency standard-library Python; don't add packaging or third-party
  deps without a clear reason and the user's agreement.

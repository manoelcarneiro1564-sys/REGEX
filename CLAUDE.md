# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) and other AI
assistants when working with code in this repository.

## ⚠️ Current repository state

**This repository is currently empty.** As of the last update to this file
(2026-06-02), the `REGEX` repository contains no source files, no commits on
its history other than documentation bootstrap, no build configuration, and
no defined toolchain. There is no codebase to analyze yet.

> **Action required for future assistants:** The sections below are a
> *bootstrap template*, not a description of existing code. As soon as real
> code is added, **replace the placeholder sections with an accurate
> description of the actual project** — language, structure, build/test
> commands, and conventions. Do not leave stale or aspirational content in
> this file; it should always reflect the true state of the repository.

## What this project appears to be

The repository is named **`REGEX`**. Based only on the name, it is likely
intended to be a project related to **regular expressions** — for example a
regex engine, a regex utility/library, a learning/playground project, or a
collection of regex patterns. This is an inference from the name only and
**has not been confirmed by any code**. Confirm the actual intent with the
repository owner or the first real commit before relying on it.

## Getting started (once code exists)

When the first real code lands, the assistant should:

1. **Identify the language and toolchain.** Look for manifest/config files
   that reveal the ecosystem, e.g.:
   - `package.json` → Node.js / JavaScript / TypeScript
   - `pyproject.toml`, `setup.py`, `requirements.txt` → Python
   - `Cargo.toml` → Rust
   - `go.mod` → Go
   - `pom.xml`, `build.gradle` → Java / JVM
2. **Discover the build, test, and lint commands** from those manifests (e.g.
   `npm test`, `pytest`, `cargo test`, `go test ./...`) and record them in the
   "Common commands" section below.
3. **Map the directory structure** (source dir, tests dir, entry points) and
   document it in the "Project structure" section.
4. **Update this file** so it accurately describes the above.

## Common commands

_None defined yet — the repository has no build system or tests._

Populate this section once a toolchain exists. Suggested layout:

```
# Install dependencies
<command>

# Build
<command>

# Run tests
<command>

# Run a single test
<command>

# Lint / format
<command>
```

## Project structure

_No structure yet — the repository is empty._

Document the directory layout and the responsibility of each top-level
directory here once code is added.

## Development workflow

### Branching

- All AI-assisted development for this task is done on the branch
  `claude/claude-md-docs-elDGy`.
- Never push directly to the default branch without explicit permission.
- Create feature branches off the default branch for new work.

### Commits

- Use clear, descriptive, imperative-mood commit messages
  (e.g. "Add regex tokenizer", not "added stuff").
- Keep commits focused and logically scoped.

### Pull requests

- Do **not** open a pull request unless the user explicitly asks for one.

## Conventions for AI assistants

- **Keep this file truthful.** It must always reflect the real state of the
  repository. If you add code, update the relevant sections in the same change.
- **Don't fabricate.** Do not document commands, files, or architecture that do
  not exist. Verify against the actual tree before writing.
- **Match the surrounding code** once it exists: follow the established
  formatting, naming, and idioms rather than imposing new ones.
- **Prefer the project's own tooling** (its declared formatter, linter, and test
  runner) over ad-hoc alternatives.

## Notes

- This file was generated to bootstrap documentation for an otherwise empty
  repository. Revisit and rewrite it once the project has real content.

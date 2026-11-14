# Contributing to cdx-tray

Run the checks before and after a change:

```bash
cargo test --locked
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Compatibility with CDX

The tray reads `cdx tray status --json` from CDX Manager. `SCHEMA_MAJOR` in `src/snapshot.rs` is
the snapshot major this build understands; a newer major shows an update hint instead of failing.
Every release records that major in `checksums/release-archives.json`, and `cdx tray install` only
installs a tray that reads the installed CDX major.

## README and documentation

The README keeps one short shape, shared with cdx-manager and logics-manager: title and badges,
the one-line promise, "Get started in a minute", "What you can do" (a table), and "Documentation"
(the docs index and the closing licence line). Detail goes in `docs/`, never in the README.
`tests/test_readme_structure.py` enforces the shape.

## Workflow

Work is tracked with Logics in `logics/` (see `LOGICS.md`).

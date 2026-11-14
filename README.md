<img src="assets/icons/CDXLight-ok@2x.png" alt="CDX tray icon" width="48" align="left" />

# cdx-tray

<br clear="left"/>

[![CI](https://github.com/AlexAgo83/cdx-tray/actions/workflows/ci.yml/badge.svg)](https://github.com/AlexAgo83/cdx-tray/actions/workflows/ci.yml) [![License](https://img.shields.io/badge/license-MIT-4C8BF5)](LICENSE) ![Rust](https://img.shields.io/badge/Rust-2021-DEA584?logo=rust&logoColor=white)

**Your AI coding quota, one glance away.** cdx-tray is the optional system tray companion of
[CDX Manager](https://github.com/AlexAgo83/cdx-manager): one icon that says whether your Codex and
Claude sessions still have capacity, and a native menu to see each session and open a terminal.

It never talks to a provider. It reads the snapshot `cdx tray status --json` already produces, so
it shows exactly what `cdx status` knows, including how old each number is.

## Get started in a minute

Install CDX Manager first, then let it fetch and verify the companion for your platform:

```bash
npm install -g cdx-manager
cdx tray install
```

`cdx tray install` downloads the release that matches your machine, checks it against the
checksum ledger published with it, and refuses anything nothing vouches for. Building from source
and local testing are covered in [local testing](docs/tray-local-testing.md).

## What you can do

| Need | How | Detail |
| --- | --- | --- |
| See at a glance whether any session can take work | The tray icon (ok, low, critical, unknown) | [Local testing](docs/tray-local-testing.md) |
| See every session's capacity and reset time | Open the menu | [Local testing](docs/tray-local-testing.md) |
| Open a session's terminal | Click its menu row | [Local testing](docs/tray-local-testing.md) |
| Know when CDX outgrew this tray | An update hint for a newer snapshot schema | [Compatibility](#documentation) |

## Documentation

- [Local testing](docs/tray-local-testing.md): build, run and check the companion on each platform.
- [Runtime and transport boundary](docs/adr-005-runtime-and-transport-boundary.md): why a native icon and menu, how it talks to CDX, how macOS builds are signed.
- Compatibility: each release records in `checksums/release-archives.json` the CDX snapshot schema major it reads; `cdx tray install` only pairs a CDX with a tray that reads its major. A new major in CDX announces itself here and triggers this repository's CI.

Contributions are welcome through pull requests. cdx-tray is [MIT licensed](LICENSE).

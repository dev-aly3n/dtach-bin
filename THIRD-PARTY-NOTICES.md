# Third-party notices

This package redistributes the **dtach** source code, compiled into
binaries that are shipped inside the wheels.

## dtach

- **Project**: dtach — a simple program that emulates the detach feature
  of `screen`, without the rest of `screen`.
- **Author**: Ned T. Crigler
- **Copyright**: © 2004–2016 Ned T. Crigler
- **Upstream**: https://github.com/crigler/dtach (mirror) and
  https://dtach.sourceforge.net/
- **License**: GNU General Public License version 2 (GPL-2.0-only).
  The verbatim license text is in [LICENSE](LICENSE).
- **Vendored version**: 0.9 (tagged `v0.9` upstream, SHA `7acac92`).
  Source tarball is at `vendor/dtach-0.9.tar.gz`; its SHA-256 is
  recorded in `vendor/dtach-0.9.tar.gz.sha256`.

The wheels in this distribution contain **unmodified** dtach 0.9 source
compiled for the target platform plus a thin Python helper module
(`src/dtach_bin/__init__.py`) authored separately under the same GPL-2.0
license for license-compatibility.

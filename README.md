# dtach-bin

Precompiled [`dtach`](https://github.com/crigler/dtach) binary shipped as
Python wheels for Linux and macOS. Install via pip / pipx and the `dtach`
binary lands on PATH automatically — no compiler, no package manager
required.

This package exists primarily so that [aipager](https://github.com/dev-aly3n/aipager)
and other Python projects can declare `dtach` as a runtime dependency and
have it installed transparently. The pattern is the same one used by
[`nodejs-bin`](https://pypi.org/project/nodejs-bin/),
[`cmake`](https://pypi.org/project/cmake/), and
[`ninja`](https://pypi.org/project/ninja/).

## Install

```sh
pip install dtach-bin
```

or, in any tool that wraps pip (pipx, uv, poetry, hatch, etc.).

## Use

After install, just call `dtach` normally:

```sh
dtach -n /tmp/my-session.sock bash
```

Or, from Python, ask for the absolute path:

```python
import dtach_bin
print(dtach_bin.path())  # → '/.../bin/dtach'
```

## Supported platforms

Pre-built wheels are published for:

| OS    | Architecture |
|-------|--------------|
| Linux | x86_64 (manylinux2014) |
| Linux | aarch64 (manylinux2014) |
| macOS | x86_64 (macOS 11+) |
| macOS | arm64 (macOS 11+) |

Other platforms can build from sdist if a working `cc` + `make` toolchain
is available — dtach is plain POSIX C using only libc and termios.

## License

dtach itself is GPL-2.0-only (© 2004–2016 Ned T. Crigler). This package
redistributes the unmodified dtach source plus a thin Python helper, and
is therefore also licensed under GPL-2.0-only — see [LICENSE](LICENSE)
for the full text.

Programs that invoke `dtach` as a separate process (via subprocess /
exec) are not derivative works of dtach — see the
[FSF GPL FAQ on mere aggregation](https://www.gnu.org/licenses/gpl-faq.html#MereAggregation).
So depending on `dtach-bin` from an MIT/Apache/BSD-licensed project is
fine. See [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) for upstream
credits.

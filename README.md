# dtach-bin

Precompiled [`dtach`](https://github.com/crigler/dtach) binary shipped as
Python wheels for Linux and macOS. Install via pip / pipx and the `dtach`
binary lands on PATH automatically — no compiler, no system package
manager required.

This package exists so that Python projects can declare `dtach` as a
runtime dependency the same way they declare any other Python package —
and have it work across Linux x86_64, Linux aarch64, macOS Intel, and
macOS Apple Silicon out of the box. The packaging pattern is the same
one used by
[`nodejs-bin`](https://pypi.org/project/nodejs-bin/) (ships Node.js),
[`cmake`](https://pypi.org/project/cmake/) (ships CMake), and
[`ninja`](https://pypi.org/project/ninja/) (ships the Ninja build tool).

## Install

```sh
pip install dtach-bin
```

— or in anything that wraps pip: `pipx`, `uv`, `poetry`, `hatch`, etc.

## Use

After install, call `dtach` normally:

```sh
dtach -n /tmp/my-session.sock bash      # create a detached session
dtach -a /tmp/my-session.sock            # reattach to it
```

From Python, ask for the absolute path of the bundled binary:

```python
import dtach_bin
print(dtach_bin.path())  # → '/.../venv/bin/dtach'
```

`dtach_bin.path()` returns the binary in the active venv first (so it
works even with `pipx` and `uv tool install` layouts where the venv's
`bin/` isn't on the calling shell's PATH), falling back to a `PATH`
lookup. Useful when a host process needs to invoke dtach via
`subprocess` and can't rely on a particular shell PATH being set.

## Supported platforms

Pre-built wheels are published for:

| OS    | Architecture | Wheel tag |
|-------|--------------|-----------|
| Linux | x86_64       | `manylinux2014_x86_64` (glibc ≥ 2.17) |
| Linux | aarch64      | `manylinux2014_aarch64` |
| macOS | x86_64       | `macosx_11_0_x86_64` (macOS 11 Big Sur or later) |
| macOS | arm64        | `macosx_11_0_arm64` |

If pip can't find a wheel for your platform (FreeBSD, Linux musl,
exotic arches, etc.) it falls back to the sdist and builds from source
— see [Building from source](#building-from-source). dtach is plain
POSIX C using only libc and termios, so the build works anywhere a
`cc` + `make` toolchain is available.

## How it works

The wheel is **not** a Python C extension. It's a regular pure-Python
package whose only Python content is the `dtach_bin/__init__.py` helper
module, plus the compiled `dtach` binary placed in the wheel's
[`scripts` data location](https://packaging.python.org/en/latest/specifications/binary-distribution-format/#installing-a-wheel-distribution-1-0).
At install time, `pip` lays the binary down at `<prefix>/bin/dtach`,
which is on PATH for any tool that runs inside that environment.

Each platform wheel is built inside the standard
[`pypa/manylinux2014`](https://github.com/pypa/manylinux) container (on
Linux) or against `MACOSX_DEPLOYMENT_TARGET=11.0` (on macOS), then
re-tagged from `cp310-cp310-<platform>` to `py3-none-<platform>` — the
binary doesn't depend on the Python version, so any Python 3 can
install it.

The full CI pipeline lives in
[`.github/workflows/build-wheels.yml`](.github/workflows/build-wheels.yml):
checkout → verify the vendored source SHA-256 → compile dtach inside
the target environment → bundle into a wheel → upload to PyPI via
[Trusted Publisher OIDC](https://docs.pypi.org/trusted-publishers/) (no
API tokens stored anywhere).

## Building from source

To build a wheel locally — useful when contributing or when no
pre-built wheel exists for your platform:

```sh
git clone https://github.com/dev-aly3n/dtach-bin && cd dtach-bin

# Compile dtach into the package's binary slot
tar -xzf vendor/dtach-0.9.tar.gz -C /tmp
( cd /tmp/dtach-0.9 && ./configure && make )
cp /tmp/dtach-0.9/dtach src/dtach_bin/_bin/dtach
chmod +x src/dtach_bin/_bin/dtach

# Build the wheel
python3 -m build --wheel
ls dist/
```

The vendored source tarball is the upstream `crigler/dtach` v0.9
release; its SHA-256 is committed at
`vendor/dtach-0.9.tar.gz.sha256` and verified in CI before every
build.

## License

dtach itself is **GPL-2.0-only** (© 2004–2016 Ned T. Crigler). This
package redistributes the unmodified dtach source plus a thin Python
helper, and is therefore also licensed under GPL-2.0-only — see
[LICENSE](LICENSE) for the full text.

**You can depend on `dtach-bin` from a non-GPL project.** Programs that
invoke `dtach` as a separate process (via subprocess / exec) are not
derivative works of dtach — see the
[FSF GPL FAQ on mere aggregation](https://www.gnu.org/licenses/gpl-faq.html#MereAggregation).
This is the same arrangement that lets Debian and Homebrew ship dtach
alongside non-GPL software. See
[THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) for upstream credits.

## Reporting issues

For build problems specific to this package, open an issue at
[github.com/dev-aly3n/dtach-bin/issues](https://github.com/dev-aly3n/dtach-bin/issues).

For dtach bugs or behavior questions, see upstream:
[github.com/crigler/dtach](https://github.com/crigler/dtach).

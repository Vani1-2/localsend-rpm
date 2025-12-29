
# LocalSend (Unofficial Fedora/RPM Package)


[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**This is an unofficial RPM packaging script for [LocalSend](https://localsend.org).**

LocalSend is a free, open-source application that allows you to securely share files and messages with nearby devices over your local network without an internet connection.

> **⚠️ Note:** This repository contains the **RPM spec files** used to repackage the official generic Linux binaries provided by the upstream developers. It is not affiliated with the LocalSend team.

## This package is no longer on copr 

However you can still use this repo to build an `.rpm` package by following
the local build instructions


## How It Works

Since LocalSend is built with Flutter and does not currently provide official RPM builds, this package:

1. Downloads the official "Generic Linux" tarball release from the [LocalSend GitHub](https://github.com/localsend/localsend).
2. Extracts the pre-compiled binaries.
3. Installs them to `/usr/lib64/localsend`.
4. Sets up the desktop entry, icons, and executable wrapper so it integrates seamlessly with your desktop environment (GNOME, KDE, etc.).

## Building Locally

If you want to build the RPM yourself instead of using COPR:

```bash
# 1. Install build tools
sudo dnf install rpm-build rpmdevtools

# 2. Clone this repo
git clone https://github.com/Vani1-2/localsend-copr.git
cd localsend-copr

# 3. Download sources & Build
spectool -g -R localsend.spec
rpmbuild -ba localsend.spec

```

## 🤝 Contributing

If the package is out of date or broken:

1. Open an issue in this repository.
2. Or submit a Pull Request bumping the `Version:` in `localsend.spec`.

## Credits

* **Original Application:** [LocalSend](https://localsend.org) by [Tien Do Nam](https://github.com/Tienisto).
* **Packaging:** Maintained by [Vani1-2](https://github.com/Vani1-2).

This package is distributed under the **Apache 2.0 License**, same as the upstream project.

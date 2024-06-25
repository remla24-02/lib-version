# lib-version

A version-aware library that can can be asked for the version of the library.
This Python package provides the library version for the [phishing detection app](https://github.com/remla24-02/app) of team 2 of the REMLA course taught at the TU Delft in 2024. The package is available on [PyPI](https://pypi.org/project/lib_version_remla24_team02/).

## Installation

To install the library, run:

``` console
pip install lib_version_remla24_team02
```

## How to use

To get the latest version of the library, use:

``` console
VersionUtil.get_version()
```

## Versioning

When a bug fix/patch is pushed to main, the patch version is automatically increased.

For minor and major versions, you can push a Git tag like ```v.0.1.0``` and a workflow will be triggered, which will release the new version.

Pre-release version such as ```v.0.1.0.dev1``` are also supported.

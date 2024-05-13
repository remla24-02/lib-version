# lib-version

A version-aware library that can can be asked for the version of the library.

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
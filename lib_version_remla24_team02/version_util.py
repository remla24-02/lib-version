from importlib import metadata


PACKAGE_NAME = "lib_version_remla24_team02"


class VersionUtil:
    """
    Return the current version of the library from meta-data.
    """
    @staticmethod
    def get_version():
        try:
            library_version = metadata.version(PACKAGE_NAME)
        except metadata.PackageNotFoundError:
            library_version = "Package not found"

        return library_version

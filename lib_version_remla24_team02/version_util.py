import subprocess


class VersionUtil:
    @staticmethod
    def get_version():
        try:
            # Get the latest Git tag
            latest_git_tag = subprocess.check_output(['git', 'describe', '--tags']).decode().strip()

            if latest_git_tag.startswith('v'):
                lib_version = latest_git_tag[1:]
            else:
                lib_version = latest_git_tag
        except subprocess.CalledProcessError:
            lib_version = 'No tags available or git repository not found.'

        return lib_version

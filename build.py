import os
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    username = "tessil"
    channel = "stable"
    upload_remote = "https://api.bintray.com/conan/tessil/tsl"
    stable_branch_pattern = "release/*"
    upload_only_when_stable = True

    builder = ConanMultiPackager(username=username,
                                 channel=channel,
                                 upload=upload_remote,
                                 stable_branch_pattern=stable_branch_pattern,
                                 upload_only_when_stable=upload_only_when_stable)
    builder.add_common_builds()
    builder.builds = [builder.builds[0]]
    builder.run()

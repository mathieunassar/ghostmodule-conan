from cpt.packager import ConanMultiPackager
import os

if __name__ == "__main__":
    builder = ConanMultiPackager(upload_dependencies="all", build_policy="missing")
    builder.add_common_builds()
    builder.run()

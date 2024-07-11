#!/usr/bin/python3
""" Fabric script that creates .tgz of webstatic """


from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successfully created, None on failure.
    """
    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Name of the archive
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Path to the archive
    archive_path = "versions/{}".format(archive_name)

    # Compress the web_static folder into a .tgz archive
    result = local("tar -cvzf {} web_static".format(archive_path))

    # Check if tar command executed successfully
    if result.failed:
        return None
    else:
        return archive_path

#!/usr/bin/python3
"""deploy .tgz to webservers """


from fabric.api import env, put, run
import os

env.hosts = ['54.84.14.15', '35.153.33.126']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    
    Args:
        archive_path (str): The path of the archive to be distributed.
    
    Returns:
        bool: True if all operations were successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract archive filename and folder name without extension
        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.replace('.tgz', '')

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the /data/web_static/releases/ folder
        run("sudo mkdir -p /data/web_static/releases/{}/".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_filename, folder_name))
        run("sudo rm /tmp/{}".format(archive_filename))

        # Move the contents of the uncompressed folder to the right location
        run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(folder_name, folder_name))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(folder_name))

        # Delete the existing symbolic link
        run("sudo rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".format(folder_name))

        return True

    except:
        return False

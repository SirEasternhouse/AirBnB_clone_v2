#!/usr/bin/python3
""" creates and distributes an archive to your web servers, using function deploy"""


from fabric.api import env, put, run, local
from datetime import datetime
import os


env.hosts = ['54.84.14.15', '35.153.33.126']
env.user = 'ubuntu'


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successfully created, None on failure.
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    result = local("tar -cvzf {} web_static".format(archive_path))
    if result.failed:
        return None
    return archive_path

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
        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.replace('.tgz', '')

        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}/".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_filename, folder_name))
        run("sudo rm /tmp/{}".format(archive_filename))
        run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(folder_name, folder_name))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(folder_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".format(folder_name))
        return True
    except:
        return False

def deploy():
    """
    Creates and distributes an archive to web servers.

    Returns:
        bool: True if the deployment was successful, False otherwise.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

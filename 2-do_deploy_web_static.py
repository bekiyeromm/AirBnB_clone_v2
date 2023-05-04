#!/usr/bin/python3
"""
Fabric script to deploy web_static archive to web servers
"""


from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ['52.91.178.133', '54.160.69.6']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    name = os.path.splitext(filename)[0]

    try:
        """ Upload the archive to the /tmp/ directory of the web server"""
        put(archive_path, '/tmp/')

        """ Create the directory to uncompress the archive"""
        run('mkdir -p /data/web_static/releases/{}/'.format(name))

        """ Uncompress the archive to the folder"""
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(filename, name))

        """ Delete the archive from the web server"""
        run('rm /tmp/{}'.format(filename))

        """ Move the files to the new folder and remove the old folder"""
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(name, name))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(name))

        """ Delete the symbolic link /data/web_static/current from the web"""
        run('rm -rf /data/web_static/current')

        """ Create a new the symbolic link /data/web_static/current"""
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(name))

        print('New version deployed!')
        return True

    except Exception:
        return False

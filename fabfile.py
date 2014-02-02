"""
    deploy
    ~~~~~~

    Deploying with Fabric (Latest Version)

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""
import os
from fabric.api import *


# -----------------------------------------------------------
# Just modify the following config to get your script running

#: the user you want to use for remote servers
env.user = 'root'
#: the servers
env.hosts = ['server1.remote', 'server2.remote']
#: the place where you want to put your app
ROOT = '/web'
#: temporary directory used to handle tarballs
TMP = '/tmp'
# -----------------------------------------------------------


#: Your app root directory name
DIRNAME = os.path.basename(os.path.abspath(os.path.dirname(__file__)))
#: Your app tarball name
TARNAME = local('python setup.py --fullname', capture=True).strip()
#: Your app tarball path
TARPATH = os.path.join(TMP, TARNAME)


def pack():
    """Pack your source code
    """
    #: source code parent directory
    parent = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    tar_cmd = 'cd %s && tar zcf %s.tar.gz %s' % (parent, TARPATH, DIRNAME)
    local(tar_cmd, capture=False)


def bootstrap():
    """Init your remote servers
    """
    # upload requirement.txt
    put('requirement.txt', os.path.join(TMP, 'requirement.txt'))
    with cd(TMP):
        run('pip install -r requirement.txt')
    # cleaning
    run('rm %s' % os.path.join(TMP, 'requirement.txt'))


def deploy():
    """Deploying
    """
    # upload to remote server tmp folder
    put('%s.tar.gz' % TARPATH, '%s.tar.gz' % TARPATH)
    # create you destination deploy place
    run('mkdir -p ' + ROOT)
    with cd(ROOT):
        run('tar zxf %s.tar.gz' % TARPATH)

    # cleaning
    local('rm %s.tar.gz' % TARPATH)
    run('rm %s.tar.gz' % TARPATH)


def install():
    """Use this if you are deploying a new app

       Usage:
       $> fab install
    """
    pack()
    bootstrap()
    deploy()
    
    with cd(os.path.join(ROOT, DIRNAME)):
        # fire the application up
        # if you are upgrading, just ignore the rebind error
        run('supervisord -c supervisord.conf')


def upgrade():
    """Use this if you are upgrading one existing app

       Usage:
       $> fab upgrade
    """
    pack()
    bootstrap()
    deploy()

    with cd(os.path.join(ROOT, DIRNAME)):
        # upgrade
        run('supervisorctl reload')
        run('supervisorctl restart all')

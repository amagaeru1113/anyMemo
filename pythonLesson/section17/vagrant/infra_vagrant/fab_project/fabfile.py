from fabric.api import *
from fabric.colors import *
from fabric.contrib.files import *


WEB_DIR = '/root/work'


env.hosts = ['root@172.16.200.101:22']
env.passwords = {'root@172.16.200.101:22': 'root'}
env.roledefs = {
    'common': ['root@172.16.200.101:22'],
    'web': ['root@172.16.200.101:22'],
}


@task
@roles('common')
def install_packages():
    run('apt-get install -y software-properties-common')
    run('add-apt-repository universe')
    run('apt-get update')
    run('apt-get install -y python-setuptools')
    run('easy_install pip')

@task
@roles('web')
def deploy_web():
    run('apt-get install -y supervisor')
    run('apt-get install -y gunicorn')
    run('pip install Flask==0.12.2')

    if not exists(WEB_DIR):
        run('mkdir {}'.format(WEB_DIR))

    put('roles/web/files/hello.py',
        '/root/work/hello.py')
    put('roles/web/files/app.conf',
        '/etc/supervisor/conf.d/app.conf')
    run('service supervisor restart')

@task
def deploy_dev_server():
    install_packages()
    deploy_web()
    print(green('success'))


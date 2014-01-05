import os, sys

from fabric.api import local, lcd, task
from fabric.colors import green

cellar_path = '/usr/local/Cellar'
mysql_home = '/Applications/MAMP/Library/bin'

@task
def install():
    setup_java_dir()
    install_maven()
    install_tomcat()
    install_ricedb()

def setup_java_dir():
    local('sudo mkdir /java')
    local('sudo chown `whoami` /java')
    local('mkdir /java/tools')

def install_maven():
    local('brew install maven')
    local('cp m2.zip ~/')

    with(lcd('~/')):
        local('unzip -q m2.zip')

    local('rm ~/m2.zip')
    add_environment_var('M2_HOME', get_mvn_home())
    # we don't set the m2_home/bin to path since brew took care of that

def install_tomcat():
    local('brew install tomcat')
    local('cp mysql-connector-java-5.1.26.tar.gz /tmp')
    with(lcd('/tmp')):
        local('tar -xzf mysql-connector-java-5.1.26.tar.gz')

    catalina_home = get_catalina_home()
    local('cp /tmp/mysql-connector-java-5.1.26/mysql-connector-java-5.1.26-bin.jar %s/lib' % catalina_home)
    local('rm -rf /tmp/mysql-connector-java-5.1.26')
    add_environment_var('CATALINA_HOME', catalina_home)

def install_ricedb():
    local('cp -r rice /java/')
    with(lcd('/java/rice/db/impex/master')):
        # validate that maven can connect to mysql
        local('mvn validate -Pdb,mysql -Dimpex.dba.password=root')
        local('mvn clean install -Pdb,mysql -Dimpex.dba.password=root')


def get_tomcat_version():
    return local('ls %s/tomcat' % cellar_path, capture=True)

def get_catalina_home():
    return '%s/tomcat/%s/libexec' % (cellar_path, get_tomcat_version())

def get_mvn_version():
    return local('ls %s/maven' % cellar_path, capture=True)

def get_mvn_home():
    return '%s/maven/%s/libexec' % (cellar_path, get_mvn_version())

def add_environment_var(variable, value):
    local_user = local('whoami', capture=True)
    shrc_filename = '/Users/' + local_user + '/.zshrc'
    shell_rc = open(shrc_filename, "a")
    shell_rc.write("\nexport %s=%s" % (variable, value) )
    shell_rc.close()

@task
def uninstall():
    local('sudo rm -rf /java')
    local('brew remove maven')
    local('rm -rf ~/.m2')
    print(green('Removed Maven successfully'))

    catalina_home = get_catalina_home()
    local('rm %s/lib/mysql-connector-java-5.1.26-bin.jar' % catalina_home)
    local('brew remove tomcat')

    local("%s/mysql -u root -proot -e \"DROP USER 'RICE'@'localhost'\"" % mysql_home)
    local(mysql_home + "/mysql -u root -proot -e \"DROP USER 'RICE'@'%'\"")
    local("%s/mysql -u root -proot -e \"DROP DATABASE rice\"" % mysql_home)
    print(green('Removed Tomcat successfully'))
    print(green('Remove M2_HOME from ~/.zshrc by hand'))



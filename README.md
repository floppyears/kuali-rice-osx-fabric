### Kuali Installation via Fabric

This fabric script is inspired by the kuali rice installfest docs and the kuali
rice install wiki page. The credit for all the hard work goes to them. I didn't
want to go through a word doc or a bunch of wiki instructions to setup a kuali
rice environment in my OSX system.

## Getting Started

1. Install Mysql (I suggest and this fabric script expects MAMP):
    http://www.mamp.info/en/index.html

2. At the command line run the install task:
    fab install


## Uninstall kuali environment

1. At the command line run the uninstall task:
    fab uninstall

2. Comment out the new environment variables:
    M2_HOME
    CATALINA_HOME

## Assumptions

I wrote this fabric for the needs of my environment. It is meant for development
and not a production environment.

* Use brew to install packages: tomcat, maven
* Mysql installed via mamp
* No /java directory present
* No rice db or user present in mysql server

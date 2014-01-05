### Kuali Installation via Fabric

This fabric script is inspired by the kuali rice installfest docs and the kuali
rice install wiki page. The credit for all the hard work goes to them. I didn't
want to go through a word doc or a bunch of wiki instructions to setup a kuali
rice environment in my OSX system.

## Getting Started

1. Install Mysql (I suggest and this fabric script expects MAMP):
    http://www.mamp.info/en/index.html

2. (Optional) Download and copy the m2.zip file from the installfest instructions:
    https://drive.google.com/a/kuali.org/folderview?id=0B7RCL4ARSiGEZmNmUEVGS3BPbUk&usp=sharing

3. At the command line run the install task:
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

## Credits

This is just a simple fabric script. If I had more time, I would write a kuali-rice
brew formula. All the hard work was done by the kuali-rice developers, installfest 
folks and people who work on the docs.

    https://wiki.kuali.org/display/KULRICE/Kuali+Days+2013+-+Install+Fest+Workshop
    http://site.kuali.org/rice/2.3.2/reference/html/IG.html

The included rice directory is included for easier of setup as it was included in 
the installfeset zip file.

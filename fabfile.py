#fabfile to generate and publish a Pelican blog as a user page to GitHub
#Mitchell Stanton-Cook 2013 
#m.stantoncook@gmail.com

import os
from   fabric.api import task


def get_fab_script_location():
    """
    Return directory containing fabfile which corresponds to Pelican local base
    """
    return os.path.dirname(os.path.realpath(__file__))

def parse_config():
    """
    Very simple parser to get the remote repo info
    """
    with open(os.path.join(get_fab_script_location(), "config.dat")) as fin:
        lines = fin.readlines()
    return lines[0].split('=')[-1].strip()
    

@task
def generate():
    """
    Execute the Pelican Makefile
    """
    loc = get_fab_script_location()
    os.chdir(loc)
    os.system("python get_publications.py") 
    os.system("mkdir output")
    os.system("make html")
    os.system("cp CNAME output")
    return loc

@task
def publish():
    """
    Publish the site/blog to GitHub
    """
    loc = generate()
    uname = parse_config()
    os.chdir(loc)
    os.system("ghp-import output")
    os.system("git push git@github.com:username/username.github.io.git gh-pages:master".replace("username", uname))
    return loc


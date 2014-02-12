Beatson Lab Website
===================

Quickstart
----------

**Get up and going in 10 steps!**

1) Install git!

2) Make sure you have python 2.7.* installed::
    
    $ python --version


3) Install virtualenv burrito::
    
    $ curl -s https://raw.github.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL


4) Make a virtualenv:: 

    $ mkvirtualenv pelican


5) Activate virtualenv::
    
    workon pelican


6) Install autoenv::

    $ pip install autoenv


7) Build a REPO directory and clone::
    
    $ mkdir ~/REPOS
    $ cd !$
    $ git clone git@github.com:BeatsonLab-MicrobialGenomics/BeatsonLab-MicrobialGenomics.github.io.git
    $ cd BeatsonLab-MicrobialGenomics.github.io
    $ git remote update
    $ git pull --all


8) Install the requirements::

    $ pip install -r requirements.txt


9) Read the docs/play around (look at content/\*.rst for examples) also see:
   http://docs.getpelican.com/en/3.1.1/


10) Publish updates/posts::
    
    $ cd ~/REPOS/BeatsonLab-MicrobialGenomics.github.io
    $ fab publish


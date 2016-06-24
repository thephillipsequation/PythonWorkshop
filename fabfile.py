import sys
import os
from fabric.api import env, local, sudo, require, run, put, settings, cd, lcd

def _ensure_virtualenv():
    if "VIRTUAL_ENV" not in os.environ:
        sys.stderr.write("$VIRTUAL_ENV not found. Make sure to activate virtualenv first\n\n")
        sys.exit(-1)
    env.virtualenv = os.environ["VIRTUAL_ENV"]


def install_deps():
    _ensure_virtualenv()
    local('pip install -q -r dependencies/dependencies.txt' % env)

def run_tests():
    _ensure_virtualenv()
    local('python code/test/unittest_helloworld.py')

def run_pep8():
    _ensure_virtualenv()
    local('pep8 code')

def run_pylint():
    _ensure_virtualenv()
    local('pylint code')

def pre_commit():
    _ensure_virtualenv()
    install_deps()
    run_pep8()
    run_pylint()
    run_tests()
    

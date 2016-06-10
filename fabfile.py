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
    local('python code/unittest_helloworld.py')


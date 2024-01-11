# this script will pull the lastest version from repo https://github.com/trickest/cve
# it will check which file has been updated and it will convert the file to json format
# then it will update the current git repo
# this script will be ran on github action

import os
import json
import git
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

# get the current working directory
cwd = os.getcwd()

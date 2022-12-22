# import requests
# import sys
# print("Hello world")
# r = requests.get('http://example.com')
#
# sys.exit(1)


import datajoint as dj
import os
from pathlib import Path

# set dirs
base_dir = Path("/home/jovyan/work")
# base_dir = Path("/root/spyglass/base_dir")
#base_dir = Path('/Users/dorota/dandi_repos/spyglass_base_dir') # change this to your desired directory
if (base_dir).exists() is False:
    os.mkdir(base_dir)
raw_dir = base_dir / 'raw'
if (raw_dir).exists() is False:
    os.mkdir(raw_dir)
analysis_dir = base_dir / 'analysis'
if (analysis_dir).exists() is False:
    os.mkdir(analysis_dir)
recording_dir = base_dir / 'recording'
if (recording_dir).exists() is False:
    os.mkdir(recording_dir)
sorting_dir = base_dir / 'sorting'
if (sorting_dir).exists() is False:
    os.mkdir(sorting_dir)
waveforms_dir = base_dir / 'waveforms'
if (waveforms_dir).exists() is False:
    os.mkdir(waveforms_dir)
tmp_dir = base_dir / 'tmp'
if (tmp_dir).exists() is False:
    os.mkdir(tmp_dir)

# set dj config
#dj.config['database.host'] = "10.22.0.2" #"172.17.0.2"
dj.config['database.host'] = 'localhost'
dj.config['database.user'] = 'root'
dj.config['database.password'] = 'tutorial'
dj.config['database.port'] = 3306
dj.config['stores'] = {
  'raw': {
    'protocol': 'file',
    'location': str(raw_dir),
    'stage': str(raw_dir)
  },
  'analysis': {
    'protocol': 'file',
    'location': str(analysis_dir),
    'stage': str(analysis_dir)
  }
}

# set env vars
os.environ['SPYGLASS_BASE_DIR'] = str(base_dir)
os.environ['SPYGLASS_RECORDING_DIR'] = str(recording_dir)
os.environ['SPYGLASS_SORTING_DIR'] = str(sorting_dir)
os.environ['SPYGLASS_WAVEFORMS_DIR'] = str(waveforms_dir)
os.environ['SPYGLASS_TEMP_DIR'] = str(tmp_dir)
#os.environ['KACHERY_CLOUD_DIR'] = '/Users/dorota/dandi_repos/spyglass_base_dir/.kachery-cloud'

os.environ['DJ_SUPPORT_FILEPATH_MANAGEMENT'] = 'TRUE'

dj.config["enable_python_native_blobs"] = True

import numpy as np

import spyglass.common
# import datajoint as dj

# ignore datajoint+jupyter async warnings
import warnings
warnings.simplefilter('ignore', category=DeprecationWarning)
warnings.simplefilter('ignore', category=ResourceWarning)
warnings.simplefilter('ignore', category=UserWarning)


print("hello 1")

# from spyglass.common import Session, Nwbfile

print("hello 2")
# import ipdb; ipdb.set_trace()
print(dir(nd.__class__))
spyglass.common.SpikeSorting()

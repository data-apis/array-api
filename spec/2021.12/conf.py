import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[2] / "src"))

from array_api_stubs import _2021_12 as stubs_mod
from _array_api_conf import *

release = "2021.12"
sys.modules["array_api"] = stubs_mod

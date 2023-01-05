import sys

from array_api_stubs import _draft as stubs_mod
from _array_api_conf import *

release = "DRAFT"
sys.modules["array_api"] = stubs_mod

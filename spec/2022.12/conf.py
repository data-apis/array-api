import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[2] / "src"))

from array_api_stubs import _2022_12 as stubs_mod
from _array_api_conf import *

release = "2022.12"

nav_title = html_theme_options.get("nav_title") + " v{}".format(release)
html_theme_options.update({"nav_title": nav_title})
sys.modules["array_api"] = stubs_mod

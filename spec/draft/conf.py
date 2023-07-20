import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[2] / "src"))

from array_api_stubs import _draft as stubs_mod
from _array_api_conf import *

release = "DRAFT"

nav_title = html_theme_options.get("nav_title") + " {}".format(release)
html_theme_options.update({"nav_title": nav_title})
sys.modules["array_api"] = stubs_mod

"""Function stubs and API documentation for the array API standard."""

from .array_object import *
from .constants import *
from .creation_functions import *
from .data_type_functions import *
import array_api.data_types as dtype
from .elementwise_functions import *
from .indexing_functions import *
from .linear_algebra_functions import *
from .manipulation_functions import *
from .searching_functions import *
from .set_functions import *
from .sorting_functions import *
from .statistical_functions import *
from .utility_functions import *
from . import linalg
from . import fft


__array_api_version__: str = "YYYY.MM"
"""
String representing the version of the array API specification which the conforming implementation adheres to.
"""

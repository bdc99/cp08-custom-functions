# you can import other python files and access their functions.
#   BUT the file needs to be in the same folder, or the directory/system path.
#   note that to do this, the python file can't have any space, and can't start with numbers.
# See sections 11.9 through 11.11 for more details
import example_no_spaces

#must reference module
example_no_spaces.multiply2Numbers(2,4)

# you can give the module an nickname:
import example_no_spaces as ens

ens.multiply2Numbers(2,4)

# or import the function directly:
from example_no_spaces import multiply2Numbers

multiply2Numbers(2,4)

# or import every single function in that module:
# this is considered bad practice, because you don't know what you're importing, and it might have name conflicts with other
# existing functions
from example_no_spaces import *
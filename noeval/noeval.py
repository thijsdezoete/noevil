def no_eval(*args, **kwargs):
    pass

def eval(*args, **kwargs):
    pass

import sys

# Get rid of the evil
del sys.modules['__builtin__'].eval
sys.modules['__builtin__'].eval = no_eval

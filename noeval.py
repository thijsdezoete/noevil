def no_eval(*args, **kwargs):
    pass

def eval(*args, **kwargs):
    pass
import sys
sys.modules['__builtin__'].eval = no_eval

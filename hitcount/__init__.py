VERSION = (1, 3, 5)

# The pure-creative fork of upstream develop, which carries migration fixes that
# PyPI's 1.3.5 lacks. The local segment keeps the two distinguishable: without
# it the fork reports the same version as the release it differs from, and pip
# has no reason to prefer it.
__version__ = '1.3.5+pure.1'

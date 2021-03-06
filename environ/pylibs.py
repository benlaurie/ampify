# No Copyright (-) 2010 The Ampify Authors. This file is under the
# Public Domain license that can be found in the root LICENSE file.

import sys

from os.path import dirname, join as join_path, realpath

AMPIFY_ROOT = dirname(dirname(realpath(__file__)))
PYUTIL_PATH = join_path(AMPIFY_ROOT, 'src')
THIRD_PARTY_LIBS_PATH = join_path(AMPIFY_ROOT, 'third_party', 'pylibs')

if PYUTIL_PATH not in sys.path:
    sys.path.insert(0, PYUTIL_PATH)

if THIRD_PARTY_LIBS_PATH not in sys.path:
    sys.path.insert(0, THIRD_PARTY_LIBS_PATH)

try:
    import optcomplete
except ImportError:
    print
    print "You need to checkout the third_party/pylibs submodule."
    print
    print "Run the following command from inside %s" % AMPIFY_ROOT
    print
    print "    git submodule update --init third_party/pylibs"
    print
    sys.exit(1)

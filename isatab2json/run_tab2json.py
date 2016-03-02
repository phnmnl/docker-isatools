import sys
import os
src_dir = sys.argv[1]
target_dir = sys.argv[2]
try:
    from isatools.convert import isatab2json
except ImportError as e:
    raise RuntimeError("Could not import isatools package")
isatab2json.convert(src_dir, target_dir)

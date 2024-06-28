import pyuac
if not pyuac.isUserAdmin():
    try:
        pyuac.runAsAdmin(False)
        sys.exit(0)
    except Exception:
        sys.exit(1)


import os
import sys


if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    dir = os.path.dirname(dir)
    os.chdir(dir)
    sys.path.append(dir)
    from july3rd.j3m import j3_main
    j3_main()

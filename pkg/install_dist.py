#-*- coding: utf-8 -*-
import os, sys
import subprocess


for dp, dn, filenames in os.walk("dist"):
    for f in filenames:
        if str(f).lower().endswith(".whl"):
            subprocess.run(["python", "-m", "pip", "uninstall", "actions_pyhon_cpp_compiler"])
            subprocess.run(["python", "-m", "pip", "install", os.path.join(dp, f)])
            sys.exit(0)
raise RuntimeError("Can't find whl file in dist folder!")

#!/usr/bin/env python

"""
 Copyright (C) 2001 Andrei Kulakov <ak@silmarill.org>
 Licence: GPL [see http://www.gnu.org/copyleft/gpl.html]
"""

import os, sys, shutil

share = "/usr/local/share/random_vim_tip"
if not os.path.exists(share):
    os.mkdir(share)
shutil.copy("random_vim_tip.py", "/usr/local/bin/")
shutil.copy("tips", share)
shutil.copy("vim_commands", share)

print """random_vim_tip.py installed to /usr/local/bin/. Edit it if you want to
set how often it should run."""

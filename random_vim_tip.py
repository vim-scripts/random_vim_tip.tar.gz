#!/usr/bin/env python

"""
 Copyright (C) 2001 Andrei Kulakov <ak@silmarill.org>
 Licence: GPL [see http://www.gnu.org/copyleft/gpl.html]
"""

import os, sys, pickle, random

__version__ = "0.7"

x = 1           # Display a tip once for every X runs.
editor = "vim"

prog_dir = os.path.expanduser("~/.random_vim_tip")
share = os.path.expanduser("/usr/local/share/random_vim_tip")
tips_f = os.path.join(share, "tips")
cmds_f = os.path.join(share, "vim_commands")
data_f = os.path.join(prog_dir, "data")

def init():
    """Initialization - returns tips, cmds lists, count and X."""
    if not os.path.exists(prog_dir):
        os.mkdir(prog_dir)
    count = 0       # How many times script was run after displaying a tip.
    if os.path.exists(data_f):
        count = pickle.load(open(data_f))
    count += 1
    tips = pickle.load(open(tips_f))
    cmds = pickle.load(open(cmds_f))
    return tips, cmds, count, x

if __name__ == "__main__":
    tips, cmds, count, x = init()
    if count >= x:
        all = tips + cmds
        text = random.choice(all)
        print text
        raw_input("--Enter---")
        count = 0
    pickle.dump(count, open(data_f, "w"), 1)
    args = " " + " ".join(sys.argv[1:])
    os.system(editor + args)

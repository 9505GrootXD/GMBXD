# GROOT MUSIC NETWORK
# G-Network Music Projects
# Copyright (C) 2022 By @Groot_Network
# Copy Rights @RJbr0 , @MyNameIsGROOT
# Don't Any Value In This Repo If You Edit Your Github Will Get Banned 😌

import glob
from os.path import dirname, isfile


def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*/*.py")

    all_modules = [
        (((f.replace(work_dir, "")).replace("/", "."))[:-3])
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]

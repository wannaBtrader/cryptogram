import json
import os

from cryptogram.utils import do


CONFIG = None


def loadConfig():
    global CONFIG
    fname = os.path.expanduser(f"~/.cryptogram.json")
    with open(fname, "rb") as jin:
        CONFIG = json.load(jin)
    return CONFIG


class Processor:
    def config(self, config):
        pass

    def run(self):
        pass

    def notify(self, **kw):
        ncfg = CONFIG["notifications"]
        for one in ncfg:
            cmd = one.format(**kw)
            do(cmd)

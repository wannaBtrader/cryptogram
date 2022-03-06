import logging
import os
import threading

import click
from cryptogram import base
from cryptogram import bybit
from cryptogram import binance
from cryptogram.interfaces import HOME
from cryptogram.utils import setupLogging, install_hook

CONFIG = None
EXCHANGES = {"bybit": bybit.ByBit, "binance": binance.Binance}


def process(exchanges):
    threads = []
    for ecfg in exchanges:
        klass = EXCHANGES[ecfg["type"]]
        prc = klass()
        prc.config(ecfg)
        thr = threading.Thread(target=prc.run)
        thr.start()
        threads.append(thr)


@click.command()
@click.option("--quiet", "-q", default=False, is_flag=True)
@click.option("--verbose", "-v", default=False, is_flag=True)
def cli(quiet, verbose):
    os.chdir(HOME)
    install_hook()

    level = logging.INFO
    if quiet:
        level = logging.ERROR
    elif verbose:
        level = logging.DEBUG

    setupLogging("log/main.log", stdout=True, level=level)

    cfg = base.loadConfig()
    process(cfg["exchanges"])

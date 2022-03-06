import logging
import pprint
import subprocess
import sys
import traceback

from logging import Formatter


LOG = logging.getLogger(__name__)
IGNORE = {"__builtins__"}
LIMIT = 2048


def getLocals(tb):
    if tb is None:
        return ""

    while tb.tb_next:
        tb = tb.tb_next

    res = []
    prnt = res.append
    prnt("============")
    prnt("Locals dump")
    prnt("------------")
    for k, v in tb.tb_frame.f_locals.items():
        if k in IGNORE:
            continue
        prnt(k + ":")
        try:
            fmted = pprint.pformat(v)
        except Exception as exc:
            text = repr(exc)[: LIMIT - 20]
            fmted = "EXCEPTION: %r" % text
        if len(fmted) > LIMIT:
            fmted = fmted[:LIMIT] + "(MORE..., total len:%s)" % len(fmted)
        prnt(fmted)
        prnt("")
    prnt("============")
    return "\n".join(res)


orig_formatException = Formatter.formatException


def Formatter_formatException(self, exc_info):
    """add locals to logging.exception()"""
    res = orig_formatException(self, exc_info)
    locls = getLocals(exc_info[2])
    return res + "\n" + locls


def install_hook():
    """Poor mans sentry, print function locals on an exception."""

    def excepthook(typ, value, tb):
        """sys.excepthook replacement."""
        traceback.print_exception(typ, value, tb)

        res = getLocals(tb)
        print(res, file=sys.stderr)

    sys.excepthook = excepthook
    Formatter.formatException = Formatter_formatException


def setupLogging(filename, stdout=False, level=logging.INFO, thread=False):
    if thread:
        fmtstr = "(%(threadName)s) %(asctime)s %(levelname)s %(message)s"
    else:
        fmtstr = "%(asctime)s %(levelname)s %(message)s"
    logging.basicConfig(
        level=level,
        format=fmtstr,
        filename=filename,
    )
    root = logging.getLogger()
    added = []
    if stdout:
        hdlr = logging.StreamHandler(sys.stdout)
        fmt = logging.Formatter(fmtstr)
        hdlr.setFormatter(fmt)
        root.addHandler(hdlr)
        added.append(hdlr)

    return added


def tearDownLogging(added=()):
    root = logging.getLogger()
    if not added:
        added = list(root.handlers)
    for hdlr in added:
        root.removeHandler(hdlr)


def do(
    cmd,
    cwd=None,
    captureOutput=True,
    ignoreErrors=False,
    noErrorLogging=False,
    env=None,
):
    LOG.debug("Command: %s", cmd)
    if captureOutput:
        stdout = stderr = subprocess.PIPE
    else:
        stdout = stderr = None
    p = subprocess.Popen(
        cmd, stdout=stdout, stderr=stderr, shell=True, cwd=cwd, close_fds=True, env=env
    )
    stdout, stderr = p.communicate()
    if stdout is None:
        stdout = "See output above"
    else:
        stdout = stdout.decode("utf-8")
    if stderr is None:
        stderr = "See output above"
    else:
        stderr = stderr.decode("utf-8")
    if p.returncode != 0 and not ignoreErrors:
        if not noErrorLogging:
            LOG.error("An error occurred while running command: %s" % cmd)
            LOG.error("Error Output: \n%s" % stderr)
        raise ValueError(
            "Shell Process had non-zero error code: {}. \n"
            "Stdout: {}\n"
            "StdErr: {}".format(p.returncode, stdout, stderr)
        )
    LOG.debug("Output: \n%s" % stdout)

    return stdout

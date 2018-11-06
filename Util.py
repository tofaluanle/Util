# @auther 宋疆疆 
# @since 2017/9/12.
import os
import subprocess
import sys

TAG = 'util'


def cprint(msg, end='\n'):
    print('[ ' + TAG + ' ] ' + msg, end=end)
    sys.stdout.flush()


def error(msg, end='\n'):
    print('[ ' + TAG + ' ][ ERR ] ' + msg, end=end)
    sys.stdout.flush()


def execCmd(args, path=None):
    if path:
        cprint('Path: ' + path)
    else:
        cprint('Path: ' + os.getcwd())
    cprint('Exec: ' + ' '.join(args))

    if sys.platform == 'win32':
        shell = True
    else:
        shell = False

    if path:
        obj = subprocess.Popen(args, cwd=path, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)
    else:
        obj = subprocess.Popen(args, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)

    return obj


def execCmdSimle(args, path=None):
    obj = execCmd(args, path)

    obj.wait()
    ret = obj.returncode
    if ret != 0:
        msg = 'Fail: ' + str(ret)
        raise Exception(msg)

    cprint('Success ')


def execCmdWait(args, path=None):
    obj = execCmd(args, path)

    obj.wait()
    return obj


def supplementSpace(s, tarLen):
    oriLen = len(s)
    for i in range(tarLen - oriLen):
        s = ' ' + s
    return s

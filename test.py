# @author 宋疆疆
# @since 2018/11/6.

# @author 宋疆疆
# @since 2018/11/7.
import os
import sys

sys.path.append('C:\WorkSpace\PyCharm\DependStatus')

import Common
from util import Util

root = sys.argv[1] + '/'


def printParent(map):
    d = dict()
    for deep in sorted(map.keys(), reverse=True):
        modules = map[deep]
        for module in modules:
            while module.parent is not None and module.parent.aId != name:
                if d.get(module.aId) is None:
                    d[module.aId] = list()
                d[module.aId].append(module.parent.aId)
                module = module.parent
    for aId, pAIds in d.items():
        pAIds = list(set(pAIds))
        print(Util.supplementSpace(aId, 16, True) + ' [ ', end='')
        for pAId in pAIds:
            print(pAId, end=', ')
        print(' ] ')


# modules = Common.getMock()
modules = Common.get()
name = 'ziroom-main'

module = modules[name]
Common.optimise(module.sub)

Common.collectParent(module)

map = dict()
map[0] = list()
Common.collectLeaf(module, map, 0)

printParent(map)

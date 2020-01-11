import re
import typing
from collections import namedtuple
from typing import Tuple


class Doc:
    mapping = {
        "参数:": "params",
        "调用示例:": "demonstrate",
        "输出:": "output",
        "用途": "explanation"
    }

    def __init__(self, node: namedtuple):
        """ 解析节点 """

        self.node = node
        self.params = ""
        self.name = ""
        self.output = ""
        self.explanation = ""
        self.demonstrate = ""

        self._next_()

    def _next_(self):
        for x in self.node.doc:
            for key in self.mapping.keys():
                if key in x:
                    value = re.sub(f"{key}(.*)", lambda x: x.group(1), x)
                    print(self.mapping[key], value)
                else:
                    continue
        else:
            print("循环结束")

        self.name = self.node.name

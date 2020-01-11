import re
import typing
from collections import namedtuple


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

    def _next_(self) -> None:
        for x in self.node.doc:
            for key in self.mapping.keys():
                if key in x:
                    value = re.sub(f"{key}(.*)", lambda x: x.group(1), x)
                    setattr(self, self.mapping[key], value)
                else:
                    continue
        self.name = self.node.name

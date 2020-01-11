import re
import sys
import typing
from collections import namedtuple

from QAManual.c import mapping


class Doc:
    mapping = {
        "en": {
            "参数:": "params",
            "调用示例:": "demonstrate",
            "输出:": "output",
            "用途": "explanation"
        }
    }

    def __init__(self, node: namedtuple, language: str):
        """ parse node """

        self.node = node
        self.lng = language
        self.params = ""
        self.name = ""
        self.output = ""
        self.explanation = ""
        self.demonstrate = ""
        self._next_()

    @staticmethod
    def get_key(obj, value):
        for key, val in obj.items():
            if val == value:
                return key
        else:
            return None

    def _next_(self) -> None:
        for x in self.node.doc:
            for cval in mapping[self.lng]['level_pri'].values():
                if self.get_key(mapping[self.lng]['level_pri'], cval) in x:
                    value = re.sub(f"{self.get_key(mapping[self.lng]['level_pri'], cval)}(.*)", lambda x: x.group(1), x)
                    setattr(self,
                            self.get_key(mapping[self.lng]['level_pri'], cval).replace(":", ""),
                            value)
                else:
                    continue
        self.name = self.node.name

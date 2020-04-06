import re
from collections import namedtuple

from QAManual.bash_parser import ParamsParser
from QAManual.c import meaning, get_key


class Doc:
    def __init__(self, node: namedtuple, language: str):
        """ parse node """

        self.node = node
        self.lng = language
        self.params = ""
        self.name = ""
        self.output = ""
        self.explanation = ""
        self.demonstrate = ""
        self.return_type = ""
        self._next_()

    def _next_(self) -> None:
        if self.node.doc is None:
            print("当前不存在合法文档， 过滤")
            return
        else:
            print("当前函数名称", self.node.name)
        try:
            for x in self.node.doc:
                for cval in meaning[self.lng]['level_pri'].values():
                    if get_key(meaning[self.lng]['level_pri'], cval) in x:
                        value = re.sub(f"{get_key(meaning[self.lng]['level_pri'], cval)}(.*)", lambda x: x.group(1), x)
                        cb = get_key(meaning[self.lng]['level_pri'], cval).replace(":", "")
                        if cb.startswith("return"):
                            cb = "return_type"
                            value.replace(":", "")
                        setattr(self, cb, value)
                    else:
                        continue

        except TypeError:
            pass
        self.name = self.node.name
        self.param_formatter = ParamsParser(self.params, self.lng)

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
        self._next_()

    def _next_(self) -> None:
        for x in self.node.doc:
            for cval in meaning[self.lng]['level_pri'].values():
                if get_key(meaning[self.lng]['level_pri'], cval) in x:
                    value = re.sub(f"{get_key(meaning[self.lng]['level_pri'], cval)}(.*)", lambda x: x.group(1), x)
                    setattr(self,
                            get_key(meaning[self.lng]['level_pri'], cval).replace(":", ""),
                            value)
                else:
                    continue
        self.name = self.node.name
        self.param_formatter = ParamsParser(self.params, self.lng)

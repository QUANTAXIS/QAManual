"""
 内置基础解析器
"""
import inspect
import re
import typing
import types
from copy import deepcopy
from collections import namedtuple

from QAManual.c import meaning, get_key

doc_node = namedtuple("code_node", ["name", "code_source", "code_file", "doc"])


def spilt_doc(fnc: str):
    doc = fnc.split("\n")
    index = []
    t = 0
    for x in range(len(doc)):
        if doc[x] == "":
            index.append(x)
        t = x
    if t != len(doc):
        index.append(len(doc) - 1)
    result = []
    i = 0
    for temp in index:
        if temp == 0:
            continue
        result.append("\n".join(doc[i:temp]))
        i = temp
    return result


class Parser:

    def __init__(self, destination, origin_name=None, ):
        if inspect.isfunction(destination):
            self.type = "func"
        if inspect.isclass(destination):
            self.type = "class"
        self.union = destination
        self.name = self.union.__name__
        self.origin_name = origin_name

    @property
    def doc(self):
        if not self.union.__doc__ or "explanation" not in self.union.__doc__:
            return None
        return self.union.__doc__

    @property
    def code_source(self):
        try:
            return inspect.getsource(self.union)
        except OSError:
            return " "

    @property
    def code_file(self):
        p = inspect.getsourcefile(self.union)
        return p

    def parse(self):
        """override this method to perform parsing structure"""
        raise NotImplemented

    def get_node(self) -> doc_node or [doc_node]:
        """get structured data"""
        if self.type == "func":
            if self.origin_name:
                name = f"{self.origin_name}.{self.union.__name__}"
            else:
                name = self.union.__name__

            return doc_node(name=name, doc=self.parse(),
                            code_source=self.code_source,
                            code_file=self.code_file,
                            )
        elif self.type == "class":
            return self.parse()


class FunctionParser(Parser):

    def parse(self) -> typing.Mapping or None:
        if self.doc:
            return spilt_doc(self.doc)
        else:
            return None


class ClassParser(Parser):
    def parse(self):
        """  调用函数进行解析, 返回多个node """
        result = []

        for x in self.union.__dict__.values():
            if inspect.isfunction(x):
                result.append(FunctionParser(x, self.union.__name__).get_node())
            else:
                continue
        return result


class ParamsParser:
    """ format for parameters """

    def __init__(self, source: str, language: str):
        self.source = source
        self.lng = language
        self.name = set()
        self.attr = self._next_()

    def _next_(self):
        """ parse parameters and generate structure """
        rtemp = re.split("(\*\s\w+\s\->)", self.source)
        result = {}
        for ink in range(len(rtemp)):
            element = rtemp[ink]
            if re.match("\*\s\w+\s\->", element) is not None:
                next_element = rtemp[ink + 1]
                temp_element = deepcopy(next_element)
                self.attr_name = re.match("^\*\s(\w+)\s\->", element).group(1)
                for val in meaning[self.lng]['level_sec'].values():
                    key = get_key(meaning[self.lng]['level_sec'], val)
                    self.name.add(key)
                    for x in temp_element.split("\n"):
                        if val in x:
                            result.setdefault(self.attr_name, {})[key] = x.split(":")[1]

                    # if val in temp_element:
                    #
                    #     pattern = re.compile("^\n[\w\W]*.{0,1}" + f"{val}:" + r"[\s]?(.*?)\n")
                    #     print(pattern)
                    #     # Add a newline manually to ensure that the last line can be matched
                    #     c = pattern.match(temp_element + "\n")

            else:
                continue
        return result

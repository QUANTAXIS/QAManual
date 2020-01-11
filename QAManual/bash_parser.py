"""
 内置基础解析器
"""
import inspect
import typing
import types

from collections import namedtuple

doc_node = namedtuple("code_node", ["name", "code_source", "code_file", "doc"])


class Parser:

    def __init__(self, destination):
        if isinstance(destination, types.FunctionType):
            self.type = "func"
        if isinstance(destination, types.MethodType):
            self.type = "class_method"

        self.union = destination

    @property
    def doc(self):

        if len(self.union.__doc__) == 0:
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

    def get_node(self):
        """get structured data"""
        return doc_node(name=self.union.__name__, doc=self.parse(), code_source=self.code_source,
                        code_file=self.code_file)


class FunctionParser(Parser):

    def parse(self) -> typing.Mapping or None:
        return [x for x in self.doc.split("\n\n")]


class ClassParser(Parser):
    def parse(self):
        pass


class ParamsParser:
    """ format for parameters """

    def __init__(self, source):
        self.source = source

        self._next_()

    def _next_(self):
        """ parse parameters and generate structure """
        default = {
            "meaning": ""
        }
        for single_params in self.source.split("*"):
            pass



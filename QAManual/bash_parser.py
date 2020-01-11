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
        return "".join(inspect.getsourcelines(self.union)[0])

    @property
    def code_file(self):
        return inspect.getsourcefile(self.union)

    def parse(self):
        """
        重写此方法来执行解析结构
        :return:
        """
        raise NotImplemented

    def get_node(self):
        """
        获得结构化的数据"""
        return doc_node(name=self.union.__name__, doc=self.parse(), code_source=self.code_source,
                        code_file=self.code_file)


class FunctionParser(Parser):

    def parse(self) -> typing.Mapping or None:
        return [x for x in self.doc.split("\n\n")]


class ClassParser(Parser):
    """
    注意需要对子代方法进行解析
    """

    def parse(self):
        pass

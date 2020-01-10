"""
基础解析器
"""
import struct
import typing
import types


class DocParser:

    def __init__(self, destination):
        if isinstance(destination, types.FunctionType):
            self.type = "func"
        if isinstance(destination, types.MethodType):
            self.type = "class_method"

        self.union = destination

    @property
    def doc(self):
        self._doc = self.union.__doc__
        if len(self._doc) == 0:
            return None

    def _parse(self):
        raise NotImplemented

    def get_struct(self):
        """
        获得结构化的数据"""
        return self._parse()


class FunctionParser(DocParser):

    def _parse(self) -> struct.Struct or None:
        if not self.doc:
            return None
        

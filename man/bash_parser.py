"""
基础解析器
"""
import re
import inspect
import typing
import types

from collections import namedtuple

doc_node = namedtuple("code_node", ["code_source", "code_file", "doc"])


def QA_util_code_adjust_ctp(code, source):
    """
    用途:
        此函数用于在ctp和通达信之间来回转换

    参数:
        * code:
            含义: 合约代码
            类型: str
        * source:
            含义: 需要转换到的目标
            类型: str
            参数支持: ["pytdx", "ctp"]

    调用示例:
        import QUANTAXIS as QA
        symbol = QA.QA_util_code_adjust_ctp("AP2001", source="pytdx")
        code = QA.QA_util_code_adjust_ctp("AP2001", source="ctp")
        print("输出转换至代码到pytdx格式:", symbol)
        print("输出转换至代码到ctp格式:", code)

    输出:
        >> 输出转换至代码到pytdx格式: AP001
        >> 输出转换至代码到ctp格式: AP2001

    """
    if source == 'ctp':
        if len(re.search(r'[0-9]+', code)[0]) < 4:
            return re.search(r'[a-zA-z]+', code)[0] + '2' + re.search(r'[0-9]+', code)[0]
        else:
            return code.upper()
    else:
        if re.search(r'[a-zA-z]+', code)[0].upper() in ['RM', 'CJ', 'OI', 'CY', 'AP', 'SF', 'SA', 'UR', 'FG', 'LR',
                                                        'CF', 'WH', 'IPS', 'ZC', 'SPD', 'MA', 'TA', 'JR', 'SM', 'PM',
                                                        'RS', 'SR', 'RI']:
            return re.search(r'[a-zA-z]+', code)[0] + re.search(r'[0-9]+', code)[0][1:]
        else:
            return re.search(r'[a-zA-z]+', code)[0].lower() + re.search(r'[0-9]+', code)[0]


class DocParser:

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

    def _parse(self):
        """
        重写此方法来执行解析结构
        :return:
        """
        raise NotImplemented

    def get_node(self):
        """
        获得结构化的数据"""
        return doc_node(doc=self._parse(), code_source=self.code_source, code_file=self.code_file)


class FunctionParser(DocParser):

    def _parse(self) -> typing.Mapping or None:
        result = []
        content = ""
        for x in self.doc.split("\n"):
            if x == "":
                result.append(content)
                content = ""
            else:
                content += x
        return result


if __name__ == '__main__':
    a = FunctionParser(QA_util_code_adjust_ctp)
    p = a.get_node()
    print(p.code_file)

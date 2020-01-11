import re

from QAManual import FunctionParser
from QAManual import MarkdownWriter


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


parser = FunctionParser(QA_util_code_adjust_ctp)
writer = MarkdownWriter("Hello", parser.get_node())
writer.handle()

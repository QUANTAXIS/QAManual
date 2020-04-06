from datetime import datetime

from QAManual import FunctionParser, ClassParser
from QAManual import MarkdownWriter
from QUANTAXIS import QA_fetch_get_exchangerate_min


def QA_util_time_now():
    """
    explanation:
         获取下个月第一天的日期

    params:
        * dt ->:
            meaning:当天日期
            type: datetime
            optional: [null]

    return:
        datetime

    demonstrate:
        Not described

    output:
        Not described
    """
    return datetime.now()


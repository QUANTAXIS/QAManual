"""
写入markdown模块
注意你需要使用标记
"""
from man.doc_parse import Doc


class Writer:
    def __init__(self, filename, node):
        self.filename = filename
        self.node = node
        self.doc_result = Doc(node)

    def write(self, content):
        """重写此方法来构建提一个Md"""
        with open(self.filename, "a+", encoding="utf-8") as f:
            f.write(content)

    def search(self):
        """
        :return:
        """
        raise NotImplemented

    def code_writer(self):
        """ 写入代码对象 """
        raise NotImplemented

    def name_writer(self):
        """ 函数名写入对象 """
        raise NotImplemented

    def params_writer(self):
        """ 参数写入 """
        raise NotImplemented

    def output_writer(self):
        """ 输出写入 """
        raise NotImplemented

    def demonstrate_writer(self):
        """ 运行示例 """
        raise NotImplemented


class MarkdownWriter(Writer):
    """
    markdown 文档写入器
    """

    def params_writer(self):
        pass


class RstWriter(Writer):
    """
    rst 写入器
    """

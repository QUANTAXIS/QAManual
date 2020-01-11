"""
写入markdown模块
注意你需要使用标记
"""
from QAManual.doc_parse import Doc


class Writer:
    def __init__(self, filename, node):
        self.filename = filename + ".md"
        self.node = node
        self.doc_result = Doc(node)

    def write(self, content):
        """基础写入方法"""
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

    def explanation_writer(self):
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

    def handle(self):
        """ 标准处理方法 """


class MarkdownWriter(Writer):
    """
    markdown 文档写入器
    """

    def name_writer(self):
        self.write("##### " + self.doc_result.name + "\n")

    def code_writer(self):
        self.write("```python\n" + self.node.code_source + "\n```")

    def explanation_writer(self):
        self.write(">  " + self.doc_result.explanation + "\n")

    def output_writer(self):
        self.write("输出示例" + "\n" + "```\n" + self.doc_result.output + "\n```" + "\n")

    def demonstrate_writer(self):
        self.write("**运行示例**" + "\n" + "```\n" + self.doc_result.demonstrate + "\n```" + "\n")

    def params_writer(self):
        pass

    def handle(self, code=False):
        self.name_writer()
        self.explanation_writer()
        self.demonstrate_writer()
        self.output_writer()
        if code:
            self.code_writer()


class RstWriter(Writer):
    """
    rst 写入器
    """

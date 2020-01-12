"""
写入markdown模块
注意你需要使用标记
"""
import os
import re
import sys

from QAManual.bash_parser import ParamsParser
from QAManual.doc_parse import Doc
from QAManual.c import meaning


class Writer:
    exc = ""

    def __init__(self, node, cwd=os.getcwd(), path=None, language="zh"):
        self.cwd = cwd
        self.node = node
        self.doc_result = Doc(node, language)
        self.params = ParamsParser(self.doc_result.params, language)
        # source code file path
        code_filepath = self.node.code_file
        file_name = code_filepath.replace(cwd, "")
        if not path:
            """ if the specified output path is passed in """
            destination_dir = os.path.join(cwd, "doc_output")
        else:
            """如果传入了指定文件夹路径"""
            if os.path.exists(path):
                """ 绝对路径 """
                destination_dir = path
            else:
                """ 相对路径 """
                destination_dir = os.path.join(cwd, path)
        # create folder
        if not os.path.exists(destination_dir):
            os.mkdir(destination_dir)
        self.filename = os.path.join(destination_dir, re.sub(r"[/\\]+(.*)", lambda x: x.group(1), file_name)).replace(
            ".py", ".md")
        self.lng = language

    def write(self, content):
        """basic writing method"""
        with open(self.filename, "a+", encoding="utf-8") as f:
            f.write(content)

    def search(self):
        raise NotImplemented

    def code_writer(self):
        """ write code object """
        raise NotImplemented

    def explanation_writer(self):
        raise NotImplemented

    def name_writer(self):
        """ function name write method"""
        raise NotImplemented

    def params_writer(self):
        """ parameter writing method """
        raise NotImplemented

    def output_writer(self):
        """ output writing method """
        raise NotImplemented

    def demonstrate_writer(self):
        """ example write method """
        raise NotImplemented

    def trim(self, docstring):
        """ unindent doc"""
        if not docstring:
            return ''
        lines = docstring.expandtabs().splitlines()
        indent = sys.maxsize
        for line in lines[1:]:
            stripped = line.lstrip()
            if stripped:
                indent = min(indent, len(line) - len(stripped))
        trimmed = [lines[0].strip()]
        if indent < sys.maxsize:
            length = len(lines[1:])
            for ind in range(len(lines[1:])):
                content = lines[1:][ind]
                trimmed.append(content[indent:] + "\n") if ind != length - 1 else trimmed.append(content[indent:])
        while trimmed and not trimmed[-1]:
            trimmed.pop()
        while trimmed and not trimmed[0]:
            trimmed.pop(0)
        return ''.join(trimmed)

    def handle(self):
        """ standard processing method """


class MarkdownWriter(Writer):
    """
    markdown document writer
    """

    def name_writer(self):
        self.write("##### " + self.doc_result.name + "\n")

    def code_writer(self):
        self.write("```python\n" + self.node.code_source + "\n```")

    def explanation_writer(self):
        self.write("> ".join([x + "\n" for x in self.trim(self.doc_result.explanation).split("\n")]) + "\n" + "\n")

    def output_writer(self):
        self.write(
            f"{meaning[self.lng]['level_mean']['output']}" + "\n" + "```\n" + self.trim(
                self.doc_result.output) + "\n```" + "\n")

    def demonstrate_writer(self):
        self.write(f"**{meaning[self.lng]['level_mean']['demonstrate']}**" + "\n" + "```\n" + self.trim(
            self.doc_result.demonstrate) + "\n```" + "\n")

    def params_writer(self):
        length = len(self.params.name)

        def generate_header():
            """ generate doc header of the markdown table"""
            return "| Attr | " + " |".join(self.params.name) + "| \n" + "|" + "|".join(
                [":----:" for x in range(length + 1)]) + "|\n"

        header = "**Attr Table**\n\n" + generate_header()
        body = ""
        for key, value in self.params.attr.items():
            body += ("|" + key)
            for x in self.params.name:
                body += "|" + str(self.params.attr[key].get(x, None))
            body += "|\n"
        end = "\n" + header + body + "\n"
        self.write(end)

    def path_writer(self):
        self.write(f"{meaning[self.lng]['level_mean']['path']}: `{self.node.code_file}`" + "\n")

    def handle(self, code=False):
        self.name_writer()
        self.path_writer()
        self.explanation_writer()
        self.params_writer()
        self.demonstrate_writer()
        self.output_writer()
        if code:
            self.code_writer()


class RstWriter(Writer):
    """
    rst document writer
    """

"""
命令行搜索程序
"""
import argparse
import os
import sys
import types
import inspect
from .writer import MarkdownWriter
from .bash_parser import FunctionParser

parser = argparse.ArgumentParser(description="Let's go! Man~")
parser.add_argument('-init', '--init', help='project initialization command, ;'
                                            'qaman --init .')
parser.add_argument('-o', '--output', help='output the address of the generated document;'
                                           'qaman -init . -o /home/somewheve/au .')
parser.add_argument("-s", '--search', help="Enter keywords, query API, use with project parameters")
parser.add_argument("-path", '--abspath', help="add absolute search path")
parser.add_argument("-p", '--project',
                    help="Incoming project nouns, functions and functions for querying specified projects in projects ")


class QAMan:

    @classmethod
    def search(cls, args):
        """
        search command
        """

    @classmethod
    def init(cls, args):
        env = {}
        for key, value in locals().items():
            env[key] = value
        cwd = os.getcwd()
        if args.init == ".":
            file_path = os.path.join(cwd, "__init__.py")
        else:
            file_path = os.path.join(args.abspath, "__init__.py")
        if not os.path.exists(file_path):
            print("\n--->当前路径不存在__init__.py文件,请切换到项目根目录下面执行此命令,或者通过-path参数直接添加 \n--->程序终止!!!\n")
            return
        with open(file_path, "r+") as f:
            d = types.ModuleType("object")
            d.__file__ = f.name
            exec(compile(f.read(), f.name, 'exec'), d.__dict__)
        for k, v in d.__dict__.items():
            if k in env.keys():
                continue
            else:
                if inspect.isfunction(v):
                    """ Processing function """
                    parse = FunctionParser(v)
                    writer = MarkdownWriter(parse.get_node(), cwd, path=args.output, language="zh")
                    writer.handle()
                elif inspect.isclass(v):
                    """ Processing class """
                else:
                    continue
        print("\n--->执行成功 !!\n")


def main():
    args = parser.parse_args()
    if args.init is not None:
        """ processing initialization commands """
        QAMan.init(args)
    if args.search is not None:
        """ processing query commands """
        QAMan.search(args)

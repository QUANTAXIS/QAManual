"""
命令行搜索程序
"""
import argparse
import sys

parser = argparse.ArgumentParser(description="Let's go! Man~")
parser.add_argument('-init', '--init', help='project initialization command, ;'
                                            'qaman --init .')
parser.add_argument('-o', '--output', help='output the address of the generated document;'
                                           'qaman -init . -o /home/somewheve/au .')
parser.add_argument("-s", '--search', help="Enter keywords, query API, use with project parameters")
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
        if args.init == ".":
            print(dir())


def main():
    args = parser.parse_args()
    if args.init is not None:
        """ processing initialization commands """
        QAMan.init(args)
    if args.search is not None:
        """ processing query commands """
        QAMan.search(args)

def example_func(code, source):
    """
    explanation:
        此函数用于在ctp和通达信之间来回转换

    params:
        * code ->
            含义: 测试用例
            类型: str
            参数支持: []
        * source ->
            含义: 需要转换到的目标
            类型: List
            参数支持: ["pytdx", "ctp"]

    demonstrate:
        example_func("你好", "somewheve")

    output:
        >>somewheve --> 你好

    return:
        int
    """
    print(source, "-->", code)


def spilt_doc(fnc: str):
    doc = fnc.split("\n")
    index = []
    t = 0
    for x in range(len(doc)):
        if doc[x] == "":
            index.append(x)
        t = x
    if t != len(doc):
        index.append(len(doc) - 1)
    result = []
    i = 0
    for temp in index:
        if temp == 0:
            continue
        result.append("\n".join(doc[i:temp]))
        i = temp
    return result


if __name__ == '__main__':
    p = spilt_doc(example_func.__doc__)
    for x in p:
        print(x, end="\n\n")
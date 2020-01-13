def example_func(code, source):
    """
    QAMAN
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
    """
    print(source, "-->", code)

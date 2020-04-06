"""
需要支持中文和英文两种注解生成. 支持更多语言
"""

meaning = {
    "zh":
        {
            "level_pri":
                {
                    "params:": "参数",
                    "demonstrate:": "调用示例",
                    "output:": "输出",
                    "explanation:": "用途",
                    "return": "返回类型",
                },
            "level_sec":
                {
                    "meaning": "含义",
                    "type": "类型",
                    "optional": "参数支持"
                },
            "level_mean":
                {
                    "source_code": "源代码",
                    "explanation": "解释",
                    "output": "示例输出",
                    "demonstrate": "调用示例",
                    "path": "路径",
                    "return": "返回类型"
                }
        },
    "en":
        {
            "level_pri":
                {
                    "params:": "params",
                    "demonstrate:": "demonstrate",
                    "output:": "output",
                    "explanation:": "explanation",
                    "return": "return"
                },
            "level_sec":
                {
                    "meaning": "meaning",
                    "type": "type",
                    "optional": "optional"
                },
            "level_mean":
                {
                    "source_code": "Origin source",
                    "explanation": "Explanation",
                    "output": "Example output",
                    "demonstrate": "Call example",
                    "path": "Path",
                    "return": "Return Type"
                }
        },

}


def get_key(obj, value):
    for key, val in obj.items():
        if val == value:
            return key
    else:
        return None

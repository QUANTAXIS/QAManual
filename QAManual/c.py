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
                    "explanation:": "用途"
                },
            "level_sec":
                {
                    "meaning": "含义",
                    "type": "类型",
                    "optional_value": "参数支持"
                },
            "level_mean":
                {
                    "source_code": "源代码",
                    "explanation": "解释",
                    "output": "示例输出",
                    "demonstrate": "调用示例",
                    "path": "路径"
                }
        },
    "en":
        {
            "level_pri":
                {
                    "params:": "params",
                    "demonstrate:": "demonstrate",
                    "output:": "output",
                    "explanation:": "explanation"
                },
            "level_sec":
                {
                    "meaning": "meaning",
                    "type": "type",
                    "optional_value": "optional_value"
                },
            "level_mean":
                {
                    "source_code": "Origin source",
                    "explanation": "Explanation",
                    "output": "Example output",
                    "demonstrate": "Call example",
                    "path": "Path"
                }
        },

}


def get_key(obj, value):
    for key, val in obj.items():
        if val == value:
            return key
    else:
        return None

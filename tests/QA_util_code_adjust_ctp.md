##### QA_util_code_adjust_ctp
路径: `/home/somewheve/PycharmProjects/QAManual/tests/tests.py`

> 此函数用于在ctp和通达信之间来回转换



**Attr Table**

| Attr | optional_value |meaning |type|
|:----:|:----:|:----:|:----:|
|code|[]|合约代码|str|
|source|["pytdx", "ctp"]|需要转换到的目标|str|

**调用示例**

```
import QUANTAXIS as QA
symbol = QA.QA_util_code_adjust_ctp("AP2001", source="pytdx")
code = QA.QA_util_code_adjust_ctp(p"AP2001", source="ctp")
print("输出转换至代码到pytdx格式:", symbol)
print("输出转换至代码到ctp格式:", code)
```
示例输出
```
>> 输出转换至代码到pytdx格式: AP001
>> 输出转换至代码到ctp格式: AP2001
```

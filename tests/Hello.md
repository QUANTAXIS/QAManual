##### QA_util_code_adjust_ctp
>  
    :
        此函数用于在ctp和通达信之间来回转换
**运行示例**
```
    
        import QUANTAXIS as QA
        symbol = QA.QA "\n```" +_util_code_adjust_ctp("AP2001", source="pytdx")
        code = QA.QA_util_code_adjust_ctp("AP2001", source="ctp")
        print("输出转换至代码到pytdx格式:", symbol)
        print("输出转换至代码到ctp格式:", code)
```
输出示例
```
    
        >> 输出转换至代码到pytdx格式: AP001
        >> 输出转换至代码到ctp格式: AP2001
```

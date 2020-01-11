import threading
import datetime

from time import sleep

flag_svm = False


def loop_check(hour, minute=0, second=0, interval=1, func=None, callback=None, threaded=False, daemon=False, **kwargs):
    """
    指定时间执行一次， 接受参数回调
    注意只接受字典参数
    """

    def loop():
        init = True
        datetime_str = f"1990-10-1 {str(hour).rjust(2, '0')}:{str(minute).rjust(2, '0')}:{str(second).rjust(2, '0')}"
        des_time = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S").time()
        print("预期时间: ", des_time)
        while True:

            now = datetime.datetime.now().time()
            print("当前时间, ", now)
            if now.hour == des_time.hour and now.minute == des_time.minute and now.second == des_time.second and init:
                if func:
                    try:
                        result = list(func(**kwargs))
                    except TypeError:
                        result = None
                if result and callback:
                    callback(*result)
                init = False

            sleep(interval)
            if now.hour == 0 and minute == 0 and now.second == 0:
                init = True

    if not threaded:
        loop()
    else:
        p = threading.Thread(target=loop, daemon=daemon)
        p.start()


def next_using(func, **kwarg):
    old_minute = datetime.datetime.now().minute
    while True:
        now_minute = datetime.datetime.now().minute
        if now_minute != old_minute:
            """ 如果分钟不相等，那么说明进入新的一分钟"""
            # 执行函数
            func(**kwarg)
            # 更新时间记录的分钟
            old_minute = now_minute
        sleep(1)


def svm():
    global flag_svm
    flag_svm = True




def minute_using(c):
    global flag_svm
    ing = datetime.datetime.now()
    if ing.hour < 9 or (ing.hour == 9 and ing.minute < 15):
        return
    if not flag_svm:
        return
    # 处理


loop_check(hour=8, func=svm, threaded=True)
next_using(minute_using, c=1)

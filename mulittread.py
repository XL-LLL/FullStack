"""
<case1: 直接使用threading中的Thread类创建线程>
Date: 2024/5/15
Author: 猫猫不吃sakana
"""

from threading import Thread
import time
from time import sleep


# 自定义的函数，可以替换成其他任何函数
def task(threadName, number, letter):
    print(f"【线程开始】{threadName}")
    m = 0
    while m < number:
        sleep(1)
        m += 1
        current_time = time.strftime('%H:%M:%S', time.localtime())
        print(f"[{current_time}] {threadName} 输出 {letter}")
    print(f"【线程结束】{threadName}")


thread1 = Thread(target=task, args=("thread_1", 4, "a"))  # 线程1：执行任务打印4个a
thread2 = Thread(target=task, args=("thread_2", 4, "b"))  # 线程2：执行任务打印2个b

thread1.start()  # 线程1开始
thread2.start()  # 线程2开始

thread1.join()  # 等待线程1结束
thread2.join()  # 等待线程2结束
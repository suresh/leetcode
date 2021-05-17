#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#

# @lc code=start
import threading

class Foo:
    def __init__(self):
        self.event1 = threading.Event()
        self.event2 = threading.Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.event1.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        self.event1.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.event2.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        self.event2.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        
# @lc code=end


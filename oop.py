from threading import Thread

class MyThread(Thread):
    def __init__(self, text):
        Thread.__init__(self)
        self.text = text

    def text_to_decimal(self):
        return [ord(i) for i in self.text]

thr1 = MyThread(text="Hello, World!")
thr2 = MyThread(text="Hello, Python!")

thr1.start()
thr2.start()

thr1.join()
thr2.join()

decimal1 = thr1.text_to_decimal()
decimal2 = thr2.text_to_decimal()

print(decimal1)
print(decimal2)

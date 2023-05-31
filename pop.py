import threading

TEXT = "Hello, World!"
DECIMAL = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]

def text_to_decimal(text, return_val):
    return_val[0] = [ord(i) for i in text]

def decimal_to_text(decimal, return_val):
    return_val[0] = ''.join(map(chr, decimal))

return_val_1 = [None]
return_val_2 = [None]

thr1 = threading.Thread(target=text_to_decimal, args=(TEXT, return_val_1))
thr2 = threading.Thread(target=decimal_to_text, args=(DECIMAL, return_val_2))

thr1.start()
thr2.start()

thr1.join()
thr2.join()

print(return_val_1[0])
print(return_val_2[0])

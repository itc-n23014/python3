import time,sys

def zigzag():
    a = "*******"
    while True:
        for i in range(11):
            print(" " * i + a)
            time.sleep(0.1)
        for i in range(10, 0, -1):
            print(" " * i + a)
            time.sleep(0.1)

try:
    zigzag()
except KeyboardInterrupt:
    sys.exit()

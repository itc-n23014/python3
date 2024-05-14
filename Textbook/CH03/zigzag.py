import time,sys

def zigzag():
    a = "*******"
    while True:
        for indent in range(11):
            print(" " * indent + a)
            time.sleep(0.1)
        for indent in range(10, 0, -1):
            print(" " * indent + a)
            time.sleep(0.1)

try:
    zigzag()
except KeyboardInterrupt:
    sys.exit()

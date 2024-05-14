def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

number = int(input("数字を入力してください: "))
r = collatz(number)
print(r)
while r != 1:
    r = collatz(r)
    print(r)


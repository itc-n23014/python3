def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

number = int(input("数字を入力してください: "))
print(r:= collatz(number))
while r != 1:
    print(r := collatz(r))


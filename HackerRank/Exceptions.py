def excep(arr):
    for i in arr:
        try:
            print((int(i[0]))//(int(i[1])))
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:", e)


if __name__ == '__main__':
    n = int(input())
    holder = []
    for i in range(n):
        arr = list(map(str, input().split()))
        holder.append(arr)
    excep(holder)

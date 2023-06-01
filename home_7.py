
1
def binary_search(num, num_list):
    N = len(num_list)
    ResultOK = False
    First = 0
    Last = N-1
    while True:
        if First < Last:
            Middle = (First + Last) // 2
            if num == num_list[Middle]:
                First = Middle
                Last = First
                ResultOK = True
                Pos = Middle
            else:
                if num > num_list[Middle]:
                    First = Middle + 1
                Last = Middle - 1
        else:
            if ResultOK == True:
                print("Элемент найден", Pos)
                break
            else:
                print("Элемент не найден")
                break

num = int(input("Введите искомую цифру: "))
num_list = sorted([2,3,1,7,6,99,15,90])
binary_search(num, num_list)


2
def bubble_sort(a):
    N = len(a)
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            print(a)
a = [5,8,1,4,6,]
bubble_sort(a)
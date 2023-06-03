# spysok = [2, 4, 7, 12, 34, 1, 56, 78, 9]
"""b=0
for i in spysok:
    b += i

print(b)"""

# def calcSum(A):
#     if A==[]:
#         return 0
#     else:
#         summ = calcSum(A[1:])
#         summ += A[0]
#         return summ
#
# summ = calcSum(spysok)
# print(summ)

"""spysok = [1, -7, 9, 15, 25, -67, -98, -56, 65]
def calcSumNegative(A):
    if A == []:
        return 0
    else:
        count = calcSumNegative(A[1:])
        if A[0] < 0:
            count += 1
        return count

n = calcSumNegative(spysok)
print(n)"""

# def GetFibonacciList(n,l):
#     count = len(l)
#     if len(l)<2:
#         return []
#
#     num1 = l[count-2]
#     num2=l[count-1]
#
#     if(num1+num2)<n:
#         l = l+[num1+num2]
#         return GetFibonacciList(n, l)
#     else:
#         return l
# new = GetFibonacciList(10000, [0,1])
# print(new)

"""def power(x,y):
    if y>0:
        return x * power(x, y-1)
    else:
        return 1

res=power(3,4)
print(res)"""

# def GetMaxList(L):
#     if len(L) > 1:
#         Max = GetMaxList(L[1:])
#         if L[0] < Max:
#             return Max
#         else:
#             return L[0]
#
#     if len(L) == 1:
#         return L[0]
#
# spysok = [500,6000,40,53]
# res = GetMaxList(spysok)
# print(res)

spysok = input('Введіть числа через пробіл -> ').split()
spysok = [int(num) for num in spysok]

def GetMinList(L):
    if len(L) > 1:
        Min = GetMinList(L[1:])
        if L[0] > Min:
            return Min
        else:
            return L[0]

    if len(L) == 1:
        return L[0]

def calcPositive(A):
    if A == []:
        return 0
    else:
        count = calcPositive(A[1:])
        if A[0] > 0:
            count += 1
        return count


while True:
    a = input('Оберіть дію: \n1 - знайти мінімальне число \n2 - Порахувати позитивні числа \n-> ')
    if a == '1':
        print(GetMinList(spysok))
    elif a == '2':
        print(calcPositive(spysok))
    else:
        print('Така дія не передбачена')
        break











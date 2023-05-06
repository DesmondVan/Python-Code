import os

print("Văn Huỳnh Trung Hiếu 10AN")
print()
print("THỰC HÀNH-----------------")
print("Hiển thị nhiệm vụ 1 bài 23")
print()

dsLop = []
n = int(input("Nhập số học sinh trong lớp: "))
for i in range(n):
    name = input("Nhập họ tên học sinh thứ " + str(i+1) + " : ")
    dsLop.insert(0,name)
print("Danh sách học sinh đã nhập: ")
for name in dsLop:
    print(name)

os.system("pause")
os.system("cls")

print("Hiển thị nhiệm vụ 2 bài 23")
print()

A = []
n = int(input("Số phần tử trong danh sách A: "))

for i in range(n):
    num = int(input("Nhập số nguyên thứ " + str(i+1) + " : "))
    A.append(num)

for i in range(n):
    if A[i-1] < 0:
        A.remove(A[i-1])

print(A)

os.system("pause")
os.system("cls")

print("Hiển thị nhiệm vụ 3 bài 23")
print()

A=[]
p = [1,2,3]
pkq = -1

x = int(input("Xác định số phần tử trong dãy A: "))
for j in range(x):
    num = int(input("Nhập số thứ" + str(j+1) + " : "))
    A.append(num)
for j in range(x):
    if A[j] == p[0] and A[j+1] == p[1] and A[j+2] == p[2]:
        pkq = i

if pkq >= 0 :
    print("Tìm thấy mẫu ", p , " tại vị trí ", pkq)
else:
    print("Không tìm thấy mẫu ", p)

os.system("pause")
os.system("cls")


print("LUYỆN TẬP------------------")
print("Hiển thị luyện tập 1 bài 23")
print()

X = [1,2,2,3,4,5,5]
print(X)
X.insert(1,1)
X.insert(4,3)
X.insert(6,4)
print(X)

os.system("pause")
os.system("cls")

print("Hiển thị luyện tập 2 bài 23")
print()

A = []
a = int(input("Xác định số phần tử của dãy A: "))

for i in range(a):
    b = input("Nhập phần tử thứ " + str(i+1) + " : ")
    A.append(b)
print(A)
if len(A) % 2 != 0:
    for i in range(a):
        if i == (a+1)/2 - 1:
            del A[i]
else:
    for i in range(a):
        if i == a/2 - 1:
            A.remove(A[i])
            A.remove(A[i])
print(A)

os.system("pause")
os.system("cls")

print("VẬN DỤNG------------------")
print("Hiển thị vận dụng 1 bài 23")
print()


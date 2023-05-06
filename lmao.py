#import thư viện os để sử dụng dòng lệnh clear
import os

print("Văn Huỳnh Trung Hiếu 10AN")
print()

print("THỰC HÀNH")
print("Hiển thị nhiệm vụ 1 bài 22:")
print()

class_name_list = []

n = int(input("Nhập số học sinh: "))

for i in range(n):
    name = input("Nhập họ tên học sinh thứ tự " + str(i+1) + " : ")
    class_name_list.append(name)

print("[|| Danh sách học sinh đã nhập ||]")
for i in range(n):
    print(str(i+1) + ". " + class_name_list[i])

print(".")
print(".")
print(".")
os.system("pause")
os.system("cls")

print("THỰC HÀNH")
print("Hiển thị nhiệm vụ 2 bài 22:")
print()

num_list = []
S = 0

n = int(input("Dãy số có bao nhiêu số: "))

for i in range(n):
    num = int(input("Nhập số tự nhiên thứ " + str(i+1) + " trong dãy: "))
    num_list.append(num)
    S += num

print("Tổng các số trong dãy : " + str(S))
print("Trung bình cộng: " + str(S/n))
print("Dãy số đã nhập: ")
for i in range(n):
    print(num_list[i], end = " ")

print()
print(".")
print(".")
print(".")
os.system("pause")
os.system("cls")




print("LUYỆN TẬP")
print()
A = []
x = int(input("Danh sách A gồm bao nhiêu phần tử: "))
for i in range(x):
    y =  input("Nhập phần tử thứ " + str(i) + " : ")
    A.append(y)
del A[x-1]
print(A)
z = input("Nhập một phần tử cần thêm vào đầu danh sách: ")
A.insert(0,z)
print(A)

print(".")
print(".")
print(".")
os.system("pause")
os.system("cls")

print("VẬN DỤNG")
print()
A = []
max_num = 0
min_num = 1000000000000000000000

x = int(input("Dãy A gồm bao nhiêu phẩn tử: "))

for i in range(x):
    num = int(input("Nhập số thứ " + str(i+1) + " : "))
    A.append(num)
    if max_num < A[i] :
        max_num = A[i]
    if min_num > A[i] : 
        min_num = A[i]

print("Max : " + str(max_num))
print("Min : " + str(min_num))

print(".")
print(".")
print(".")
os.system("pause")
os.system("cls")
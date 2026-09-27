ten_ban_dau = ["  ha noi ", "DA NANG", " tp hcm"]
ten_da_sua = [ten.strip().title() for ten in ten_ban_dau]
print(ten_da_sua)

#b2------------------------
diem = [8.5, 6.0, 9.25, 7.0, 5.5]
max_diem = max(diem)
min_diem = min(diem)
print(f"Điểm cao nhất: {max_diem}, Điểm thấp nhất: {min_diem}")

diem_trung_binh = sum(diem) / len(diem)
print(f"Điểm trung bình: {diem_trung_binh:.2f}")

diem_nhỏ=[]
for i in diem:
    if i>7:
        diem_nhỏ.append(i)

print(diem_nhỏ)

ds_lap = ["VN", "VJ", "VN", "QH", "VJ", "VN"]
khong_lap = []
# for i in ds_lap:
#     if i not in khong_lap:
#         khong_lap.append(i)

# print(khong_lap)

for i in ds_lap:
    if khong_lap.count(i) < 1:
        khong_lap.append(i)

print(khong_lap)   

#Nhập 1 danh sách các số nguyên ,sau đó :
# tạo list mới chứa bình phương của các ptu,đếm có bao nhiêu số lớn hơn 50

print("Nhập số lượng các số nguyên:")
input_str = int(input())
numbers = []
print(f"phần 1...{input_str}")
for i in range(input_str):
    num = int(input())
    numbers.append(num)
print("Danh sách các số nguyên :", numbers)

squares = [x**2 for x in numbers]
print("Danh sách bình phương :", squares)

count = sum(1 for x in numbers if x > 50)
print(f"Số lượng bình phương lớn hơn 50: {count}")
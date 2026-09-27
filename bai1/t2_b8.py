tong_tich_luy=0
thang=1
while tong_tich_luy <= 50_000_000:
    tong_tich_luy += 12_000_000
    print(f"Tháng {thang}: Tổng tích lũy = {tong_tich_luy:,.0f}")
    thang += 1

dong_du_lieu = ["187", "203", "", "156", "loi", "241"]
tong_khach=0
bo_qua=0

# for i in dong_du_lieu:
#     try:
#         tong_khach += int(i)
#     except ValueError:
#         bo_qua += 1
#         print(f"Giá trị '{i}' không hợp lệ, bỏ qua.")
for i in dong_du_lieu:
    if not i.isdigit():
        bo_qua += 1
        continue

    tong_khach += int(i)


print(f"Tổng số khách: {tong_khach}")
print(f"Số giá trị không hợp lệ: {bo_qua}")

don = [("DH001", 12_000_000), ("DH002", 8_500_000),
       ("DH003", 21_000_000), ("DH004", 4_200_000)]

for ma, tien in don:
    if tien > 20_000_000:
        print(f"Tim thay: {ma} - {tien:,.0f}")
        break
else:
    print("Khong co don nao tren 20 trieu")

# tổng số chia hết cho 5 từ 10 đến 100
tong = 0
so_tn=10
while so_tn <= 100:
    tong += so_tn
    so_tn += 5

print(f"Tổng các số chia hết cho 5 từ 10 đến 100 là: {tong}") 
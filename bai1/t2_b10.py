ma = ["DH001","DH002","DH003","DH004","DH005"]
tien = [12_000_000, 8_500_000, 21_000_000, 4_200_000, 15_300_000]

if len(ma) != len(tien):
    print("Danh sách mã đơn hàng và tiền không khớp!")
    exit()
else:
    print("Danh sách mã đơn hàng và tiền khớp!")
tong_tien = sum(tien)
count = 0

for i in tien:
    if i > 10_000_000:
        count += 1

max_tien = max(tien)
index_max = tien.index(max_tien)

print("BAO CAO DON HANG")
print("-" * 34)

for m,t in zip(ma,tien):
    if t > 10_000_000:
        print(f"* {m:<10} {t:>20,} ")

    else:
        print(f"  {m:<10} {t:>20,}")

print(f"Tổng tiền: {tong_tien:,.0f}")
print(f"Trung bình: {tong_tien/len(tien):,.0f}")
print(f"Đơn trên 10 triệu: {count}")
print(f"Đơn có giá trị cao nhất: {ma[index_max]} ({max_tien:,.0f})")

don_nho=[m for m,t in zip(ma,tien) if t < 10_000_000]
print(f"Đơn có giá trị nhỏ hơn 10 triệu: {don_nho}")
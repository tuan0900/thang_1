danh_sach = ["Táo", "Cam", "Xoài"]

for i, x in enumerate(danh_sach, start=2):
    print(i, x)

for i in range(2, 10):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()

sum=0
for i in [12_000_000, 8_500_000, 21_000_000, 4_200_000]:
    sum += i
    print(type(i), i)

print("Tổng là:", f"{sum/len([12_000_000, 8_500_000, 21_000_000, 4_200_000]):,.0f}")  

chi_nhanh = ["Ha Noi", "Da Nang", "TP HCM", "Can Tho"]
doanh_thu = [12_000_000, 8_500_000, 21_000_000, 4_200_000]

for i, (cn, dt) in enumerate(zip(chi_nhanh, doanh_thu), start=1):
    print(f" {i}. {cn}: {dt:,.0f}")


#tính tổng 1!+2!+3!+...+10!
total = 0
dem = 1
for i in range(1,11):
    dem *= i
    total += dem
print("Tổng là:", f"{total:,}")
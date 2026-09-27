dong = "VN-1546|Ha Noi|187"

a=dong.split("|")
ma_chuyen = dong.split("|")[0]
ten_tinh = dong.split("|")[1]
so_khach = dong.split("|")[2]

print(f"Ma chuyen: {a}")
print(f"Ma chuyen: {ma_chuyen}, Ten tinh: {ten_tinh}, So khach: {so_khach}")

print(", ".join(["a", "b", "c"]))

print("VN-1546-54983-14285-2-4".replace("-", ""))

diadiem="TP HCM"

print(f"Dia diem: {diadiem.split()[0].title()} {diadiem.split()[1]}")

name = input("Nhap ten cua ban: ")
luong = float(input("Nhap luong cua ban: "))
ngay_cong = int(input("Nhap ngay cong cua ban: "))

print(f"Nhân Viên , {name}!")
print(f"Luong thuc nhan cua ban la: {luong*ngay_cong:,.0f}".replace(",", "."))
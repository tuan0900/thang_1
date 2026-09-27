dong = "NV002|  tran thi binh |Khai thac|24|320000|8"

ma_nv = dong.split("|")[0].strip()
ho_ten = dong.split("|")[1].strip()
bo_phan = dong.split("|")[2].strip()
luong_ngay = int(dong.split("|")[4])
so_ngay = int(dong.split("|")[3])
ngay_phep = int(dong.split("|")[5])

Tong_luong = luong_ngay * so_ngay

if Tong_luong >= 2000000:
    thue = Tong_luong * 0.1
else:
    thue = 0

thuc_nhan = Tong_luong - thue

print("=" * 40)
print(f"Ma NV      : {ma_nv}")
print(f"Ho ten     : {ho_ten.title()}")
print(f"Bộ Phận    : {bo_phan.strip().title()}")
print(f"Ngày Công  : {so_ngay}")
print(f"Tổng Lương : {Tong_luong:,.0f}")
print(f"Thuế       : {thue:,.0f}")
print(f"Thực Nhận  : {thuc_nhan:,.0f}")
print(f"Ngày Phép  : {ngay_phep}")
if ngay_phep < 5:
    print("[!] Sap het phep")

print("=" * 40)


fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for ma in ["VN-1546", "vn1546", "VJ-203"]:
    if ma.startswith("VN-") and len(ma) == 7:
        print(f"{ma} is a valid code.")
    else:
        print(f"{ma} is not a valid code.")
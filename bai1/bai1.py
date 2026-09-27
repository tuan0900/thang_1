# Bien la cai hop co ten de chua du lieu
ho_ten = "Ha Xuan Tuan"        # str   - chuoi ky tu
tuoi = 25                       # int   - so nguyen
luong_co_ban = 7500000.0        # float - so thuc
da_ky_hop_dong = True           # bool  - dung/sai

# Xem kieu du lieu cua mot bien
print(type(ho_ten))
print(type(tuoi))

# f-string: cach noi chuoi dung nhieu nhat
# print(f"{ho_ten} nam nay {tuoi} tuoi")
print(ho_ten + " nam nay " + str(tuoi) + " tuoi")

# Dinh dang so: dau phan cach nghin, khong lay so le
print(f"Luong co ban: {luong_co_ban:,.0f} dong")

# Ep kieu - chuyen tu kieu nay sang kieu khac
nam = int("2026")          # chuoi -> so nguyen
chuoi_nam = str(2026)      # so -> chuoi
diem = float("8.5")        # chuoi -> so thuc

print(nam + 1)
print(chuoi_nam + " la nam nay")
print(diem, da_ky_hop_dong)

so_khach = "187"
tong = int(so_khach) + 13
print(f"Tong so khach: {tong}")

for gia_tri in ["abc", 5, 5.0, True]:
    print(gia_tri, "->", type(gia_tri))


x=["Học","Công","Nghệ"]
y="".join(x)
print(y)
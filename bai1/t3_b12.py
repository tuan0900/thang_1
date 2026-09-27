nhan_vien = [
    {"ho_ten": "Nguyen Van An", "bo_phan": "Hanh chinh", "ngay_phep": 12},
    {"ho_ten": "Tran Thi Binh", "bo_phan": "Khai thac",  "ngay_phep": 8},
    {"ho_ten": "Le Van Cuong",  "bo_phan": "Hanh chinh", "ngay_phep": 15},
    {"ho_ten": "Pham Thi Dung", "bo_phan": "An ninh",    "ngay_phep": 3},
]

con_nhieu_phep = [nv for nv in nhan_vien if nv["ngay_phep"] > 10]
con_nhieu_phep.sort(key=lambda nv: nv["ngay_phep"], reverse=True)

for nv in con_nhieu_phep:
    print(f'{nv["ho_ten"]} - {nv["bo_phan"]} - {nv["ngay_phep"]} ngày phép')

dem={} 
for nv in nhan_vien:
    if nv["bo_phan"] in dem:
        dem[nv["bo_phan"]] += 1
    else:
        dem[nv["bo_phan"]] = 1

print("Số lượng nhân viên theo bộ phận:" ,dem)

dem2={}
for nv in nhan_vien:
    bp=nv["bo_phan"]
    dem2[bp]=dem2.get(bp,0)+nv["ngay_phep"]

print("Tổng số ngày phép theo bộ phận:" ,dem2)

nhan_vien.sort(key=lambda nv: nv["ngay_phep"],reverse=True)

for nv in nhan_vien:
    print(f'{nv["ho_ten"]} - {nv["ngay_phep"]}')

print("-"*50)
#b2
nhan_vien = [
    {"ho_ten": "Nguyen Van An",  "ngay_phep": 12},
    {"ho_ten": "Tran Thi Binh",  "ngay_phep": 8},
    {"ho_ten": "Le Van Cuong",   "ngay_phep": 15},
    {"ho_ten": "Pham Thi Dung",  "ngay_phep": 3},
    {"ho_ten": "Hoang Van Em",   "ngay_phep": 11},
]
for nv in nhan_vien:
    if nv["ngay_phep"] > 10:
        print(f'{nv["ho_ten"]} - {nv["ngay_phep"]} ngày phép')

print("-"*50)

#b3  Cho 5 đơn hàng dưới đây, làm một bảng tổng hợp theo chi nhánh: số đơn, doanh thu, tỷ trọng 
# phần trăm, sắp xếp giảm dần theo doanh thu, có dòng TỔNG ở cuối.
don_hang = [
    {"ma": "DH001", "chi_nhanh": "Ha Noi",  "thanh_tien": 12_000_000},
    {"ma": "DH002", "chi_nhanh": "Da Nang", "thanh_tien": 8_500_000},
    {"ma": "DH003", "chi_nhanh": "Ha Noi",  "thanh_tien": 21_000_000},
    {"ma": "DH004", "chi_nhanh": "TP HCM",  "thanh_tien": 4_200_000},
    {"ma": "DH005", "chi_nhanh": "Da Nang", "thanh_tien": 15_300_000},
    {"ma": "DH006", "chi_nhanh": "Thanh Hoa", "thanh_tien": 25_300_000},
    {"ma": "DH007", "chi_nhanh": "Thanh Hoa", "thanh_tien": 15_700_000}
]
chi_nhanh_summary = {}
doanh_thu_summary = {}
for dh in don_hang:
    chi_nhanh = dh["chi_nhanh"]
    chi_nhanh_summary[chi_nhanh]=chi_nhanh_summary.get(chi_nhanh,0)+1 
    doanh_thu_summary[chi_nhanh]=doanh_thu_summary.get(chi_nhanh,0)+dh["thanh_tien"]   

print(f"{'Chi nhanh':12s} {'So don':>7s} {'Doanh thu':>15s} {'Ty trong':>9s}")

for cn in sorted(doanh_thu_summary, key=lambda x: doanh_thu_summary[x], reverse=True):
    doanh_thu = doanh_thu_summary[cn]
    ty_trong = (doanh_thu / sum(doanh_thu_summary.values())) * 100
    print(f"{cn:12s} {chi_nhanh_summary[cn]:>7d} {doanh_thu:>15,.0f} {ty_trong:>8.2f}%")
print(f"{'Tổng':12s} {sum(chi_nhanh_summary.values()):>7d} {sum(doanh_thu_summary.values()):>15,.0f} {100:>8.2f}%")
# tiếp B3->tìm đơn hàng lớn nhất in mã cùng số tiền
dh_lon_nhat = max(don_hang, key=lambda x: x["thanh_tien"])
print(f"Đơn hàng lớn nhất: {dh_lon_nhat['ma']} - {dh_lon_nhat['thanh_tien']:,} VND")

for dh in don_hang:
    if dh["thanh_tien"] > 15_000_000:
        dh["xep_loai"] = "Lớn"
    elif dh["thanh_tien"] >= 8_000_000:
        dh["xep_loai"] = "Vừa"
    else:
        dh["xep_loai"] = "Nhỏ"
    print(f"{dh['ma']} - {dh['thanh_tien']:>12,.0f} VND - {dh["xep_loai"]}")



def dinh_dang_tien(so_tien):
    return f"{so_tien:,.0f} VND".replace(",", ".")

def bao_cao_theo_cot(danh_sach, cot_nhom,cot_tinh):
    """Nhom mot list dict theo mot cot va cong tong mot cot khac."""
    ket_qua = {}
    for dong in danh_sach:
        if cot_tinh not in dong or cot_nhom not in dong :
           continue
        dong_nhom = dong.get(cot_nhom)
        ket_qua[dong_nhom] = ket_qua.get(dong_nhom, 0) + 1
    return ket_qua

def bao_cao_thanh_tien(danh_sach, cot_nhom, cot_tinh):
    ket_qua = {}
    bo_qua=0
    for dong in danh_sach:
        if cot_tinh not in dong or cot_nhom not in dong :
             bo_qua = bo_qua + 1
             continue
        dong_nhom = dong.get(cot_nhom)
        ket_qua[dong_nhom] = ket_qua.get(dong_nhom, 0) + dong.get(cot_tinh, 0)
    return ket_qua,bo_qua


def in_bao_cao(theo_cot, thanh_tien):
    print(f"{'Chi Nhánh':12s} {'So don':>7s} {'Doanh thu':>15s} {'Ty trong':>9s}")
    print("-"*50)
    for cn in sorted(thanh_tien, key=lambda x: thanh_tien[x], reverse=True):
        so_don = theo_cot[cn]
        doanh_thu = thanh_tien[cn]
        ty_trong = doanh_thu / sum(thanh_tien.values()) * 100
        print(f"{cn:12s} {so_don:7d} {dinh_dang_tien(doanh_thu):>15s} {ty_trong:9.1f}%")

    print("-"*50)
    print(f"{'Tổng':12s} {sum(theo_cot.values()):>7d} {dinh_dang_tien(sum(thanh_tien.values())):>15s} {'100.0%':>9s}")

def kiem_chung(danh_sach, cot_nhom, cot_tinh):
    doanh_so,bo_qua=bao_cao_thanh_tien(danh_sach, cot_nhom, cot_tinh)
    doanh_thu_theo_nhom=sum(doanh_so.values())
    doanh_thu_theo_don_hang=sum(bg[cot_tinh] for bg in danh_sach if cot_tinh in bg and cot_nhom in bg)

    if doanh_thu_theo_don_hang != doanh_thu_theo_nhom:
        print(f"[LOI] Lech {abs(doanh_thu_theo_nhom - doanh_thu_theo_don_hang):,.0f}")
        return False    
    print("[OK] Tong khop")
    return True
don_hang = [
    {"ma": "DH001", "chi_nhanh": "Ha Noi",  "thanh_tien": 12_000_000},
    {"ma": "DH002", "chi_nhanh": "Da Nang", "thanh_tien": 8_500_000},
    {"ma": "DH003", "chi_nhanh": "Ha Noi",  "thanh_tien": 21_000_000},
    {"ma": "DH004", "chi_nhanh": "TP HCM",  "thanh_tien": 4_200_000},
    {"ma": "DH005", "chi_nhanh": "Da Nang", "thanh_tien": 15_300_000},
    {"ma": "DH006", "chi_nhanh": "Da Nang"}
]

ket_qua,bo_qua=bao_cao_thanh_tien(don_hang,"chi_nhanh","thanh_tien")
in_bao_cao(bao_cao_theo_cot(don_hang,"chi_nhanh","thanh_tien"),ket_qua)
print(f"Bo qua {bo_qua} ban ghi thieu cot")

don_hang_lon_nhat=max([dh for dh in don_hang if "thanh_tien" in dh],key= lambda x:x["thanh_tien"])
print(f'\nDon lon nhat: {don_hang_lon_nhat["ma"]} - {dinh_dang_tien(don_hang_lon_nhat["thanh_tien"])}')

kiem_chung(don_hang,"chi_nhanh","thanh_tien")


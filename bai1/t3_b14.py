#B1:Viết hàm tinh_thue_tncn(thu_nhap) trả về 10% nếu từ 2 triệu trở lên, ngược 
# lại trả 0. Bài 5 trong bộ 7 bài bắt buộc.
def tinh_thue_tncn(thu_nhap):
    if thu_nhap >= 2000000:
        return thu_nhap * 0.1
    else:
        return 0

def dinh_dang_tien(so_tien):
    return f"{so_tien:,.0f} VND"


def lam_sach_ten(chuoi):
    """Bo khoang trang thua, viet hoa chu dau moi tu."""
    return chuoi.strip().title()

def xep_loai_doanh_thu(dt, muc_dat=10_000_000, muc_vuot=20_000_000):
    """Xep loai doanh thu theo hai nguong co the doi duoc."""
    if dt > muc_vuot:
        return "Vuot chi tieu"
    if dt >= muc_dat:
        return "Dat chi tieu"
    return "Chua dat"

def loc_theo_bo_phan(danh_sach, bo_phan):
    """Tra ve list nhan vien thuoc mot bo phan."""
    return [nv for nv in danh_sach if nv["bo_phan"] == bo_phan]
for tn in [5_000_000, 2_000_000, 1_999_999]:
    print(f"{dinh_dang_tien(tn)} -> thue {dinh_dang_tien(tinh_thue_tncn(tn))}")

#B2: Viết hàm doc_so_an_toan(chuoi, mac_dinh=0): cố ép chuỗi thành số nguyên, nếu
#không được thì trả về giá trị mặc định thay vì làm chết chương trình.

def doc_so_an_toan(chuoi, mac_dinh=0):
    try:
        return int(str(chuoi).strip())
    except (ValueError, TypeError):
        return mac_dinh

#B3:Viết hàm bao_cao_theo_cot(danh_sach, cot_nhom, cot_tinh) nhóm một list dict theo
# một cột bất kỳ và cộng tổng một cột khác. Thử nhóm đơn hàng theo chi nhánh.
def bao_cao_theo_cot(danh_sach, cot_nhom, cot_tinh): 
    ket_qua = {}
    for dong in danh_sach:
        dong_nhom = dong.get(cot_nhom)
        ket_qua[dong_nhom] = ket_qua.get(dong_nhom, 0) + dong.get(cot_tinh, 0)
    return ket_qua

don_hang = [
    {"ma": "DH001", "chi_nhanh": "Ha Noi",  "thanh_tien": 12_000_000},
    {"ma": "DH002", "chi_nhanh": "Da Nang", "thanh_tien": 8_500_000},
    {"ma": "DH003", "chi_nhanh": "Ha Noi",  "thanh_tien": 21_000_000},
    {"ma": "DH004", "chi_nhanh": "TP HCM",  "thanh_tien": 4_200_000},
]

for bc in bao_cao_theo_cot(don_hang, "chi_nhanh", "thanh_tien").items():
    print(f"{bc[0]:10s}: {dinh_dang_tien(bc[1]):>14s}")

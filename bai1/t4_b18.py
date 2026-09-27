
def dinh_dang_tien(so):
    """Dinh dang so thanh kieu tien Viet Nam."""
    return f"{so:,.0f}".replace(",", ".")


def lam_sach_ten(chuoi):
    """Bo khoang trang thua, viet hoa chu dau moi tu."""
    return chuoi.strip().title()


def doc_so_an_toan(chuoi, mac_dinh=0):
    """Ep chuoi thanh so nguyen, that bai thi tra gia tri mac dinh."""
    try:
        return int(str(chuoi).strip())
    except (ValueError, TypeError):
        return mac_dinh


def ty_trong(phan, tong):
    """Tinh phan tram, tong bang 0 thi tra ve 0."""
    if tong == 0:
        return 0.0
    return phan / tong * 100


if __name__ == "__main__":
    print(dinh_dang_tien(1250000))
    print(lam_sach_ten("  nguyen van an "))
    print(doc_so_an_toan("abc", -1))
    print(f"{ty_trong(33, 61):.1f}%")

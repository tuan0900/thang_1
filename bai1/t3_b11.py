chuyen_bay=dict(ma = "VN-1546",
    diem_den ="Da Nang",
    so_khach = 187,
    tre_gio = False,)


for khoa, gia_tri in chuyen_bay.items():
    print(f"{khoa:10s}: {gia_tri}")


chuyen_bay["gio_bay"]="14:35"
chuyen_bay["so_khach"]=135
print(chuyen_bay)
print("Hang bay:",chuyen_bay.get("hang_bay", "Không có thông tin về hãng bay"))

# b2 : Cho gia_ve = {"VN-1546": 1_250_000, "VJ-203": 890_000, "QH-112": 1_050_000}. 
# Tính tổng giá vé và in các chuyến có giá trên 1 triệu
gia_ve = {"VN-1546": 1_250_000, "VJ-203": 890_000, "QH-112": 1_050_000}
tong_gia_ve = sum(gia_ve.values())
print(f"Tổng giá vé: {tong_gia_ve:,.0f}")
for chuyen, gia in gia_ve.items():
    if gia > 1_000_000:
        print(f"Chuyến {chuyen} có giá vé trên 1 triệu: {gia:,.0f}")

#b3 
cb = {"ma": "VJ-203", "diem_den": "Ha Noi", "tre_gio": True}
print(cb.get("so_khach", "Không có thông tin số khách"))

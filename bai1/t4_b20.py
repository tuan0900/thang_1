"""Tao file du lieu mau de luyen tap. Chay MOT LAN truoc khi lam du an."""

NOI_DUNG = """ma_nv|ho_ten|bo_phan|ngay_cong|luong_ngay|ngay_phep
NV001|  nguyen van an  |Hanh chinh|22|350000|12
NV002|tran thi binh|Khai thac|24|320000|8
NV003|  LE VAN CUONG|Hanh chinh|20|380000|15

NV004|pham thi dung|An ninh|26|300000|3
NV005|hoang van em|Khai thac|hai muoi|310000|10
NV006|vu thi phuong|An ninh|23|305000|5
NV007|dang van giang|Hanh chinh
NV008|  bui thi hoa |Khai thac|25|315000|0
"""

with open("nhan_vien.txt", "w", encoding="utf-8") as f:
    f.write(NOI_DUNG)

print("Da tao nhan_vien.txt voi 8 dong du lieu (co 3 dong bi loi co y).")

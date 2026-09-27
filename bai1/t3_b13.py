s={1,2,3}
s.update([4,5,6])
print(s)
print("-"*50)
# SET: khong trung lap, khong co thu tu
ma_chuyen = ["VN-1546", "VJ-203", "VN-1546", "QH-112", "VJ-203"]
duy_nhat = set(ma_chuyen)
print(sorted(duy_nhat))          # sorted() de ket qua on dinh khi in
print(f"Co {len(ma_chuyen)} dong, {len(duy_nhat)} ma khac nhau")

# Kiem tra ton tai - rat nhanh
da_xu_ly = {"VN-1546", "QH-112"}
if "VJ-203" not in da_xu_ly:
    print("VJ-203 chua duoc xu ly")

# PHEP TOAN TAP HOP
thang_8 = {"VN-1546", "VJ-203", "QH-112"}
thang_9 = {"VJ-203", "QH-112", "BL-455"}
print("Ca hai thang:", sorted(thang_8 & thang_9))
print("Chi thang 8 :", sorted(thang_8 - thang_9))
print("Moi thang 9 :", sorted(thang_9 - thang_8))
print("Tat ca      :", sorted(thang_8 | thang_9))

# TUPLE: giong list nhung KHONG sua duoc
toa_do = (21.0285, 105.8542)
print(toa_do[0], toa_do[1])
# toa_do[0] = 1     -> TypeError: 'tuple' object does not support item assignment
#B1:So sánh danh sách nhân viên hai tháng: thang_truoc = {"NV001","NV002","NV003","NV004"} 
# và thang_nay = {"NV002","NV003","NV005"}. In ra ai đã nghỉ, ai mới vào, ai còn lại.
print("-"*50)
thang_truoc = {"NV001", "NV002", "NV003", "NV004"}
thang_nay = {"NV002", "NV003", "NV005"}

print("Nghi viec:", sorted(thang_truoc - thang_nay))
print("Moi vao :", sorted(thang_nay - thang_truoc))
print("Con lai :", sorted(thang_truoc & thang_nay))

print("-"*50)
#B2:Cho list email có cả chữ hoa và khoảng trắng thừa, đếm số người thật sự khác nhau.
email_ds = ["A@x.com ", "b@X.com", " a@x.com", "C@x.com", "b@x.com "]
print(set(email.strip().lower() for email in email_ds))

print("-"*50)

#B3 
def thong_ke(list):
    max_list=max(list)
    min_list=min(list)
    sum_list=sum(list)
    return max_list, min_list, sum_list

lon, nho, tong = thong_ke([12, 45, 7, 89, 23])
print(f"Nho nhat {nho}, lon nhat {lon}, tong {tong}")

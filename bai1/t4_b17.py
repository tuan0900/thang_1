def nhap_tuoi(tuoi):
    if tuoi<0:
        raise ValueError("tuổi k đc âm")

    return tuoi

try:
   tuoi=nhap_tuoi(-5)
   print("tuổi đúng")
except ValueError as e:
    print("Lỗi : ",e)   


def doc_file(duong_dan):

     try:   
        with open(duong_dan,"r",encoding="utf-8") as f:
           text=f.readlines()
           return text

     except FileNotFoundError:
           print(f"[CANH BAO] Khong thay {duong_dan}")
           return ""

kiem_tra_file=doc_file("data.txt")
print(kiem_tra_file)

#B2: Cho ["187", "", "loi", "241", None]. Cộng tổng, bỏ qua dòng xấu, đếm số dòng lỗi. Dùng hàm doc_so_an_toan đã viết ở buổi 14.
def doc_so_an_toan(chuoi, mac_dinh=0):
    try:
        return int(str(chuoi).strip())
    except (ValueError, TypeError):
        return mac_dinh

arr=["187", "", "loi", "241", None]
tong=sum(doc_so_an_toan(x) for x in arr)
print(tong)

#int("mot tram")

# nv = {"ho_ten": "An"}
# nv["luong"]


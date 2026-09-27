from datetime import datetime

# with open("data.txt", "a") as f:
#     thoi_diem=datetime.now()
#     f.write(f"{thoi_diem} - da chay script\n")
# ds = file.readlines()

# print(ds)
# for dong in file:
#     print(dong)

def dinh_dang_tien(so_tien):
    return f"{so_tien:,.0f} VND".replace(",", ".")
don_hang = [
    {"ma": "DH001", "chi_nhanh": "Ha Noi",  "thanh_tien": 12_000_000},
    {"ma": "DH002", "chi_nhanh": "Da Nang", "thanh_tien": 8_500_000},
]
# with open("data.txt", "a") as f:
#     f.write("ma|chi_nhanh|thanh_tien\n")
#     for dh in don_hang:
#         f.write(f'{dh["ma"]}|{dh["chi_nhanh"]}|{dh["thanh_tien"]}\n')

# with open("data.txt", "r") as f:
#     tieu_de = f.readline().strip().split("|")
#     print(f"{tieu_de[0]:12s} {tieu_de[1]:>7s} {tieu_de[2]:>12s}")
#     for dong in f:
#        text=dong.strip().split("|")
#        print(f"{text[0]:12s} - {text[1]} - {dinh_dang_tien(int(text[2]))}")

list_dh=[]
with open("data.txt", "r") as f:
    tieu_de = f.readline().strip().split("|")
    for dong in f:
       gia_tri=dong.strip()
       if not gia_tri:
           continue
       text=gia_tri.split("|")
       list_dh.append(dict(zip(tieu_de,text)))


print(list_dh)
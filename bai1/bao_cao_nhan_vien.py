"""
Du an cuoi Thang 1 - Bao cao luong va ngay phep theo bo phan.

Doc  : nhan_vien.txt  (cac cot ngan cach bang dau |)
Ghi  : bao_cao_thang.txt  va  canh_bao.txt
Chay : python bao_cao_nhan_vien.py
"""
from datetime import datetime

def doc_file(ten_file):
    data=[]
    loi=[]
    try:
        with open(ten_file,'r',encoding="utf-8") as f:
            key=f.readline().strip().split("|")
            for i,dong in enumerate(f, start=2):
                text=dong.strip()
                if not text:
                    continue
                ket_qua_value=text.split("|") 
                
                if len(ket_qua_value)<6 :
                    loi.append((text,i,f"có {len(ket_qua_value)} cột , mà cần 6 cột"))
                    continue
                if not ket_qua_value[3].isdigit() or not ket_qua_value[4].isdigit() or not ket_qua_value[5].isdigit():
                    loi.append((dong,i,f"Cột số không đọc được"))
                    continue                  
                data.append(dict(zip(key,ket_qua_value)))
            return data,loi

    except FileNotFoundError:
        print("sai tên file")
        return [],[]

def lam_sach_ten(Ho_ten):
    return Ho_ten.strip().title()


def dinh_dang_tien(so_tien):
    return f"{so_tien:,.0f}".replace(",", ".")

def sap_xep_theo_cot(data,theo_cot):
    return sorted(data,key= lambda x:x[theo_cot],reverse=True)

def theo_bo_phan(data):
    nhan_vien={}
    for nv in data:
        bp=nv["bo_phan"]
        tong = int(nv["ngay_cong"]) * int(nv["luong_ngay"])*0.9
        if bp not in nhan_vien:
            nhan_vien[bp]={
               "bo_phan":bp,
               "so_nguoi":1,
               "quy_luong":tong,
               "so_phep":int(nv["ngay_phep"])
            }
            continue
        nhan_vien[bp]["so_nguoi"]+=1
        nhan_vien[bp]["quy_luong"]+=tong
        nhan_vien[bp]["so_phep"]+=int(nv["ngay_phep"]) 

    return nhan_vien.values()       

def theo_nhan_vien(kq):
    for p in kq:
        luong=int(p["luong_ngay"])*int(p["ngay_cong"])
        thuc_nhan=luong*0.9
        p["luong"]=luong
        p["thuc_nhan"]=thuc_nhan
    return sap_xep_theo_cot(kq,"luong")


def bao_cao_theo_bo_phan(nhan_vien,data):
    tong_luong=sum(v["quy_luong"] for v in nhan_vien)

    with open("bao_cao_thang.txt",'w',encoding="utf-8") as f:
            f.write("BAO CAO LUONG VA NGAY PHEP\n")
            f.write(f"Lập Lúc : {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n")
            f.write("PHAN 1 - TOM TAT THEO BO PHAN\n") 
            f.write("---------------------------------------------------------------------------------------------------\n") 
            f.write(f"{'Bộ Phận':12s} {'Số Người':>10s} {'Quỹ Lương':>20s} {'Tỷ Trọng':>15s} {'Phép':>10s}\n") 
            for r in sap_xep_theo_cot(nhan_vien,"quy_luong"):
                ty_trong=r["quy_luong"]/tong_luong
                f.write(f"{r["bo_phan"]:12s} {r["so_nguoi"]:>10} {dinh_dang_tien(r["quy_luong"]):>20} {ty_trong*100:>14.1f}% {r["so_phep"]:>10}\n")
            f.write("---------------------------------------------------------------------------------------------------\n") 
            f.write(f"{'Tổng':12s} {len(data):>10} {dinh_dang_tien(tong_luong):>20} {'100.0%':>15s} \n")
                        

def bao_cao_nhan_vien(nhan_vien):
    with open("bao_cao_thang.txt",'a',encoding="utf-8") as f:
         f.write("\n")
         f.write("PHAN 2 - CHI TIET TUNG NGUOI\n") 
         f.write(f"{'Mã':12s} {"Họ Tên":<20s} {"Công":>20s} {"Tổng Lương":>20s} {"Thực Nhận":>20s}\n")
         f.write("------------------------------------------------------------------------------------------------------\n") 
         for nv in nhan_vien:
             f.write(f"{nv['ma_nv']:12s} {nv["ho_ten"].strip().title():<20} {nv["ngay_cong"]:>20} {dinh_dang_tien(nv["luong"]):>20} {dinh_dang_tien(nv["thuc_nhan"]):>20}\n")

def file_canh_bao(dong_loi):
    with open("canh_bao.txt",'w',encoding="utf-8") as f:
         f.write(f"có {len(dong_loi)} dòng không đọc được\n")    
         f.write("-------------------------------------------------------------------------------------------------------\n")
         f.write("-------------------------------------------------------------------------------------------------------\n")
         for i in dong_loi:
             dong,cot_so,ma_loi=i
             f.write(f"Dong {cot_so}: {ma_loi}\n")
             f.write(f"  >> {dong}\n")

         

if __name__ == "__main__":
    kq,loi=doc_file("nhan_vien.txt")
    a=theo_bo_phan(kq)
    print(f"{a}\n")

    nv=theo_nhan_vien(kq)
    bao_cao_theo_bo_phan(a,kq)
    bao_cao_nhan_vien(nv)
    file_canh_bao(loi)
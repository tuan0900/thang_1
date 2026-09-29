# t1_b5 
 bài tập cho trước dữ liệu,bắt làm sạch bằng các pt strip().title().replace và split()->tính toán -> in ra
 x if dieu_kien else y là cách viết gọn của if/else khi chỉ chọn giữa hai giá trị.
 ví dụ :thue = tong_luong * 0.10 if tong_luong >= 2000000 else 0


  if/elseif/else

  Python kiểm tra các nhánh từ trên xuống, gặp nhánh đúng đầu tiên là dừng — thứ tự quyết định kết quả.

  range(start,end,step):nếu chỉ có range(n) thì có nghĩa là bắt đầu từ 0->n-1 và bước nhảy là 1
  for i in range(n): 
      câu lệnh


  for n in arr :
      khối lệnh

# Tuần 2
  ## b6 : if/elif/else
  ## b7 : Vòng lặp for
  -học thêm về for: thêm pt enumerate(ds, start=1) cho số thứ tự đếm từ 1. zip():gộp 2 danh sách thành từng cặp
  -sum() tính tổng
  -scope vòng for trong python(chat GPT-kaizuka)
   + trong python for không có block scop như ngôn ngữ khác
   + khi khai báo for i ... i sẽ tồn tại cho dù sau khi vòng lặp kết thúc,nó lấy giá trị i cuối cùng 

  ## b8 :while, break và continue

   1.học về while:khi chỉ biết điều kiện dừng
   2.học về break là dùng ngay vòng lặp và continue là bỏ bỏ đoạn code ở dưới mà thực hiện vòng lặp tiếp theo
   3.tư duy loại bỏ dữ liệu xấu:
    dữ liệu xấu->xử lí nó ->bỏ qua->sang dữ liệu tiếp theo
    dữ liệu hợp lệ -> tiếp tục xử lí bên dưới
   4.cấu trúc for...else,nếu break vòng lặp for thì cũng break else và không chạy vào else nữa
   5.học .isdigit() kiểm tra một chuỗi có phải toàn chữ số hay không
   6.continue + biến đếm là cách chuẩn để bỏ qua dòng dữ liệu hỏng mà vẫn biết đã bỏ bao nhiêu.
   7.ví dụ
    don = [("DH001", 12_000_000), ("DH002", 8_500_000),
            ("DH003", 21_000_000), ("DH004", 4_200_000)]

    for ma, tien in don:
        if tien > 20_000_000:
           print(f"Tim thay: {ma} - {tien:,.0f}")
           break
        else:
           print("Khong co don nao tren 20 trieu")       
  ## b9 : LIST
   ### cắt lát
     arr[start:end:step]
     start:index bắt đầu(gồm)
     end : index kết thúc(k gồm)
     step : bước nhảy-không để step thì mặc định là 1
     s[::-1] mảng ngược lại
   ### gán,duyệt,xóa
     a[0]=1
     for x in arr:
     arr.remove(x): xóa giá trị x đầu tiên trong list
     del a[index1] : xóa vị trí index1 
     del a[index1:index2] xóa từ vị trí index1 đến vị trí index2-1
     arr.pop() : xóa phần tử cuối và trả về giá trị
   ### Sắp xếp và 1 số pt khác
     arr.sort()
     arr.sorted()
     arr.count()->đếm
     arr.index()->tìm vị trí
   ### Thêm
    .append(x) : thêm vào cuối
    .insert(i,x) : thêm x vào vị trí index i
   ### Nối 2 LIST,lặp LIST,kiểm tra có tồn tại phần tử trong mảng hay không
    + Nối 2 list : [1,2,3] + ["a","b","c"] -> [1,2,3,"a","b","c"] 
    + lặp List   : [1,2]*3 -> [1,2,1,2,1,2]
    + Kiểm tra tồn tại : "a" in ["a","b","c"] ->true :a có tồn tại trong list
                         "b" in ["a","b","c"] ->false:x k tồn tại trong list
   ### List comprehension : tạo ra list mới từ list cũ
    + [x*2 for x in arr]
  ## B10:Ôn tập
# Tuần 3
  ## B11:DICT
   ### Tạo DICT 
     C1:
       {
        key:value,
        key:value
       }
      C2:
       dict={}
       dict[key]=value
      C3:dùng dict(key="value",key="value")
      C4: Dùng dict() với list/tuple các cặp
        nguoi = dict([
          ("ten", "Tuan"),
          (tuoi", 26),
          ("thanh_pho", "Thanh Hoa")
        ])

      C5:Dictionary comprehension-dùng khi tạo dict bằng vòng lặp
        ten = ["An", "Binh", "Cuong"]
        tuoi = [20, 25, 30]

        d = {t: a for t, a in zip(ten, tuoi)}
        kết quả:
        {
         "An": 20,
         "Binh": 25,
         "Cuong": 30
        }

   ### duyệt
     dict={
       "key1":"gt1",
       "key2":"gt2",
       "key3":"gt3",
       "key4":"gt4",
     }
      C1:for key in dict: (duyệt qua key)
         print(key,":",dict[key])  
      
      C2:(duyệt cả key và value): dict.item trả ra tuple[('key1','gt1'),('key2','gt2'),('key3','gt3'),('key4','gt4')]
      t=('key1','gt1')
      a,b=t->a='key1'/b='gt1'

      for key,value dict.item(): 
         ......

      C3:for value in dict.value(): (duyệt value)
          .....      
   ### Method chính(keys/values/get/update/items)
     get()
     keys:lấy ra tất cả các key
     values():lấy tất cả value
     items():Lấy cặp key - value ->[(key1,value1),...,(keyn,valuen)]
   ### Method khác
     dict.pop()
     dict.popitem()
     setdefault(key,value)
     fromkeys()
  ## B12: LIST DICT
    Mẫu nhóm và đếm (chính là PivotTable viết bằng tay) là mẫu bạn sẽ viết đi viết lại cả năm:

    1.Tạo một dict rỗng để chứa kết quả
    2.Duyệt từng bản ghi, lấy giá trị cần nhóm theo
    3.ket_qua[khoa] = ket_qua.get(khoa, 0) + gia_tri

  ## B13:SET và TUPLE
    1.set là 1 tập hợp bọc bởi 2 dấu {} như dict nhưng chỉ có giá trị và không có khóa
    2.khởi tạo set={}-> sai / kt_set=set()->đúng/set={1,2,3} ->đúng
    3.set là tập hợp k có phần tử trùng,k có thứ tự
    4.cũng có các phương thức thêm(add) ,xóa
      + add():thêm 1 phần tử
      + update():Thêm nhiều 
      + remove()
      + discard()
    5.phép toán tập hợp : 
      A&B(giao:lấy ptuwr chung của A và B)
      A-B(Hiệu:lấy ptuwr chỉ có ở A k có ở B)
      A|B(Hợp:lấy tất cả của A và B)
      A^B(Hiệu đối xứng:chỉ thuộc 1 trong 2)
    6.Luôn làm sạch (.strip().lower()) trước khi khử trùng ,nếu k sẽ đếm sai
    7 ví dụ:
      names=["An","Bình","An","Cường","Bình"]
      unique=list(set(names)) ----> kết quả : ["An","Bình","Cường"]
  ## B14:HÀM
# Tuần 4
  

    
   
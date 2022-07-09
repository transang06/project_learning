class SieuNhan:
    suc_manh = 50
    so_thu_tu = 1

    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
        self.stt = SieuNhan.so_thu_tu
        SieuNhan.so_thu_tu += 1

    @classmethod
    def from_string(cls, s):  # thường những phương thức xử lí thế này hay có tên là from…
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        ten, vu_khi, mau_sac = new_lst
        return cls(ten, vu_khi, mau_sac)

    @staticmethod
    def bien_hinh():
        print("1, 2, 3. Sieu nhan bien hinh")


infor_str = "Sieu nhan do - Kiem - Do"
sieu_nhan_A = SieuNhan.from_string(infor_str)
print(sieu_nhan_A.__dict__)
sieu_nhan_B = SieuNhan("Sieu nhan vang", "bua", "Vang")
sieu_nhan_A.suc_manh = 40
print(sieu_nhan_A.stt)
print(sieu_nhan_B.stt)
print(SieuNhan.so_thu_tu)
print(sieu_nhan_A.suc_manh)
print(SieuNhan.suc_manh)
print(sieu_nhan_B.__dict__)
sieu_nhan_A.bien_hinh()

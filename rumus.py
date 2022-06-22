

class rumus():
    def straightLine(self,data):
        return (data["harga"] - data['nilaiResidu']) / data['usiaEkonomis']

    def reducingBalance(self,data):
        # a = int(input("Harga Awal : "))
        # b = int(input("Nilai Residu : "))
        # c = int(input("Rate : "))
        #
        RB = (data["harga"] - data["nilaiResidu"]) * data['rate'] / 100
        return RB

    def sumOfTheYear(self,data):
        s = data["usiaEkonomis"] * (data["usiaEkonomis"] + 1) / 2
        soty = 1 * (data["harga"]- data["nilaiResidu"]) / s
        return soty

    def unitOfActivity(self,data):
        # harga = float(input("\nHarga Perolehan    = "))
        # residu = float(input("Nilai Residu       = "))
        # pemakaian = int(input("Pemakaian         = "))
        # kapasitas = int(input("Kapasitas        = "))

        return (data['harga'] - data['nilaiResidu']) * data['pemakaian'] / data['kapasitas']

        


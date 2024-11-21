from datetime import datetime

class Kitap:
    def __init__(self, baslik: str, yazar: str, yayin_yili: int, sayfa_sayisi: int, diller: list[str]):
        self.baslik = baslik
        self.yazar = yazar
        self.yayin_yili = yayin_yili
        self.sayfa_sayisi = sayfa_sayisi
        self.diller = diller

    def dil_ekle(self, dil: str):
        self.diller.append(dil) #Yeni bir dil ekler.

    def kitap_yasi_hesapla(self) -> int:
        return datetime.now().year - self.yayin_yili #Kitabın yaşını yayın yılına göre hesaplaması

    def kitap_goruntule(self, paragraf: bool = False):
        if paragraf:
            print(
                f"'{self.baslik}' başlıklı kitap, {self.yazar} tarafından yazılmıştır. "
                f"İlk olarak {self.yayin_yili} yılında yayımlanmış olan bu kitap, toplam {self.sayfa_sayisi} sayfadan oluşmaktadır. "
                f"Şu an için bu kitap, {', '.join(self.diller)} dillerinde bulunmaktadır."
            )
        else:
            # Satır bazlı görüntüleme
            print(f"Başlık: {self.baslik}")
            print(f"Yazar: {self.yazar}")
            print(f"Yayın Yılı: {self.yayin_yili}")
            print(f"Sayfa Sayısı: {self.sayfa_sayisi}")
            print(f"Diller: {', '.join(self.diller)}")


kitap = Kitap(
   baslik="Programlama Temelleri",
   yazar="Olvanot Jean Claude Rakotonirina",
   yayin_yili=2005,
   sayfa_sayisi=92,
   diller=["Türkçe", "İngilizce"]
)

kitap.dil_ekle("Fransızca")

kitap.kitap_goruntule(paragraf=True)

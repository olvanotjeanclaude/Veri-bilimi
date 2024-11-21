import numpy as np
from datetime import datetime

"""
1. Python	Sınıfı	Oluşturma
"""
class Kitap:
    def __init__(self, baslik: str, yazar: str, yayin_yili: int, sayfa_sayisi: int, diller: list[str]):
        self.baslik = baslik
        self.yazar = yazar
        self.yayin_yili = yayin_yili
        self.sayfa_sayisi = sayfa_sayisi
        self.diller = diller

    def dil_ekle(self, dil: str):
        self.diller.append(dil) #Yeni bir dil eklemek için

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
# kitap.kitap_goruntule(paragraf=True)
# print("****")
# kitap.kitap_goruntule(paragraf=False)


"""
2. Gelişmiş NumPy İşlemleri
"""
#Min/Max Değerleri ve İndeksleri
row_dict = dict()
matrix = np.random.randint(0, 100, (10, 10)) # 10x10 boyutunda rastgele tam sayı
for i in range(10):
    min_value = np.min(matrix[i])
    max_value = np.max(matrix[i])
    
    min_index = np.argmin(matrix[i]) 
    max_index = np.argmax(matrix[i])
    
    # Satırların min, max değerleri ve indekslerini sözlükte tutulması
    row_dict[i] = [(min_value, min_index), (max_value, max_index)]
    
# print(matrix)
# print("Min/Max Değerleri ve İndeksleri")
# print(row_dict)

# Her sütunun ortalama, medyan ve standart sapma 
col_dict = dict()

matrix = np.random.randint(0, 100, (10, 10)) # 10x10 boyutunda rastgele tam sayı

for col_index in range(10):
    column_mean = np.mean(matrix[:, col_index])
    column_median = np.median(matrix[:, col_index])
    column_standart_deviation = np.std(matrix[:, col_index]) 
    
    col_dict[col_index] = {
        'mean': column_mean,
        'median': column_median,
        'standart_deviation': column_standart_deviation 
    }
# print(matrix)
# print("Her sütunun ortalama, medyan ve standart sapma değerleri:")
# print(col_dict)


"""
3. Matris	Çarpımı
"""

def max_in_rows_of_product(matrix_A, matrix_B):
    matrix_AxB = np.dot(matrix_A, matrix_B)
    max_values_in_rows = np.max(matrix_AxB, axis=1) 
    # print("A X B:\n")
    # print(matrix_AxB)
    return max_values_in_rows

matrix_A = np.array([[2, 3, 4], [1, 0, 6]])
matrix_B = np.array([[1, 4], [2, 5], [3, 6]])

max_values = max_in_rows_of_product(matrix_A, matrix_B)

# print("Sonuç: Matris A x Matris B çarpımındaki her satırın en büyük değerleri:")
# print(max_values)


"""
4. Faktöriyel	Hesaplama
"""
def factorial_with_loop(n):
    if n < 0:
        return "Faktöriyel yalnızca pozitif tam sayı olmalıdır!"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial(n):
    if n < 0:
        return "Faktöriyel yalnızca pozitif tam sayı olmalıdır!"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number=10
# print(f"{number}! = {factorial_with_loop(number)}")
# print(f"{number}! = {factorial(number)}")


"""
5. Rasgele	Dizi İşlemleri
"""
random_integers = np.random.randint(1, 21, (5, 4))
# print("***Rasgele dizi:***")
# print(random_integers)
row_sums = np.sum(random_integers, axis=1)  
row_means = np.mean(random_integers, axis=1) 
row_stats = np.column_stack((row_sums, row_means))  # we can use  np.vstack((row_sums, row_means)).T and Transposing

# print("***Satır toplamları***")
# print(row_sums)
# print("***Satır ortalamaları***")
# print(row_means)
# print("******")
# print("Satırların Toplam ve Ortalamaları:\n", row_stats)

column_max = np.max(random_integers, axis=0) 
column_min = np.min(random_integers, axis=0)
column_max_min = np.column_stack((column_max, column_min))  # Yeni bir dizi oluştur
# print("Sütunların Maksimum ve Minimum Değerleri:\n", column_max_min)

"""
ÇİFT MATRIS İÇİN:
Yaklaşım: Tek Sayılara 1 Ekleme
Bu yöntemde, tek sayılara 1 eklenerek çift yapılır, çift sayılar ise olduğu gibi bırakılır

Eğer random_integers = [3, 4, 7, 8] ise:
random_integers % 2 → [1, 0, 1, 0]
(3 ve 7 için kalan 1, 4 ve 8 için 0.)
random_integers + (random_integers % 2) → [4, 4, 8, 8]
"""
even_matrix = random_integers + (random_integers % 2)
# print("Çift matris:\n", even_matrix)


"""
6. Büyük NumPy	Dizisi Analizi
"""
random_integers = np.random.randint(1, 101, size=30)

#DİZİDEKİ EN KÜÇÜK, EN BÜYÜK VE MEDYAN DEĞERİ
min_value = np.min(random_integers)  
max_value = np.max(random_integers) 
median_value = np.median(random_integers)

#ELEMANLARIN TOPLAMI, ORTALAMASI VE VARYANSI
sum_of_elements = np.sum(random_integers) 
mean_value = np.mean(random_integers) 
variance_value = np.var(random_integers)  

#DİZİDEKİ ÇİFT SAYILARIN VE 5’İN KATI OLAN SAYILARIN SAYISI
even_numbers = random_integers[random_integers % 2 == 0]  # Çift sayılar
even_count = len(even_numbers)  # Çift sayıların sayısı
even_sum = np.sum(even_numbers)  # Çift sayıların toplamı

multiples_of_five = random_integers[random_integers % 5 == 0]  # 5'in katları
multiples_of_five_count = len(multiples_of_five)  # 5'in katlarının sayısı
multiples_of_five_sum = np.sum(multiples_of_five)  # 5'in katlarının toplamı

#BÜYÜKTEN KÜÇÜĞE SIRALAMASI
sorted_descending = np.sort(random_integers)[::-1] 

#ORTALAMANIN ÜZERINDE
above_mean = random_integers[random_integers > mean_value]

#ELEMANLARININ KÜPÜ
cubed_values_of_elements = random_integers ** 3 #elemanlarının küpü

# DIZI ELEMANLARINI 4 DEFA YAN YANA 4’ER DEFA ALT ALTA YAZDIRARAK DIZIYI 2 BOYUTLU
## Tiling the array 4 times in the vertical and 4 times in the horizontal direction 
reshaped_array = np.tile(random_integers, (4, 4))

# Sonuçları yazdırın
print(f"Orijinal Dizi:\n{random_integers}")
print(f"En Küçük Değer: {min_value}")
print(f"En Büyük Değer: {max_value}")
print(f"Medyan Değer: {median_value}")
print(f"Toplam: {sum_of_elements}")
print(f"Ortalama: {mean_value}")
print(f"Varyans: {variance_value}")

print(f"Çift Sayılar: {even_numbers}, Sayısı: {even_count}, Toplamı: {even_sum}")
print(f"5'in Katları: {multiples_of_five}, Sayısı: {multiples_of_five_count}, Toplamı: {multiples_of_five_sum}")

print(f"Büyükten Küçüğe Sıralı Dizi:\n{sorted_descending}")
print(f"Ortalamanın Üzerindeki Elemanlar:\n{above_mean}")
print(f"Küp Alınmış Değerler Dizi:\n{cubed_values_of_elements}")
print(f"Yeniden Şekillendirilmiş (4x4) Dizi:\n{reshaped_array}")

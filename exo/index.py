import numpy as np

"""
2. Gelişmiş NumPy İşlemleri
"""

import numpy as np

matrix = np.random.randint(0, 100, (10, 10)) # 10x10 boyutunda rastgele tam sayı

row_dict = dict()

for i in range(10):
    min_value = np.min(matrix[i])
    max_value = np.max(matrix[i])
    
    min_index = np.argmin(matrix[i]) 
    max_index = np.argmax(matrix[i])
    
    # Satırların min, max değerleri ve indekslerini sözlükte tutulması
    row_dict[i] = [(min_value, min_index), (max_value, max_index)]
    
# print("Min/Max Değerleri ve İndeksleri")
# print(row_dict)

# Her sütunun ortalama, medyan ve standart sapma 
col_dict = dict()
for col_index in range(10):
    column_mean = np.mean(matrix[:, col_index])
    column_median = np.median(matrix[:, col_index])
    column_standart_deviation = np.std(matrix[:, col_index]) 
    
    col_dict[col_index] = {
        'mean': column_mean,
        'median': column_median,
        'standartDeviation': column_standart_deviation 
    }

# print("Her sütunun ortalama, medyan ve standart sapma değerleri:")
# print(col_dict)


# İki matrisin iç çarpımını hesaplayan ve her satırdaki en büyük değeri bulan fonksiyon
def max_in_rows_of_product(matrix_A, matrix_B):
    matrix_AxB = np.dot(matrix_A, matrix_B)
    max_values_in_rows = np.max(matrix_AxB, axis=1)    
   
    return max_values_in_rows

matrix_A = np.array([[2, 3, 4], [1, 0, 6]])
matrix_B = np.array([[1, 4], [2, 5], [3, 6]])

max_values = max_in_rows_of_product(matrix_A, matrix_B)

# print("Sonuç: Matris A x Matris B çarpımındaki her satırın en büyük değerleri:")
# print(max_values)

def factorial(n):
    if n < 0:
        return "Faktöriyel yalnızca pozitif tam sayılar için hesaplanabilir."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# number=10
# print(f"{number}! = {factorial(number)}")


# 1. Rastgele tamsayı değerleriyle (5, 4) boyutu

"""
5. Rasgele	Dizi İşlemleri
"""
random_integers = np.random.randint(1, 21, (5, 4))
print("***Rasgele dizi:***")
print(random_integers)
row_sums = np.sum(random_integers, axis=1)  
row_means = np.mean(random_integers, axis=1) 
row_stats = np.column_stack((row_sums, row_means))  # we can use  np.vstack((row_sums, row_means)).T and Transposing

print("***Satır toplamları***")
print(row_sums)
print("***Satır ortalamaları***")
print(row_means)
# print("******")
print("nSatırların Toplam ve Ortalamaları:", row_stats)

column_max = np.max(random_integers, axis=0) 
column_min = np.min(random_integers, axis=0)
column_max_min = np.column_stack((column_max, column_min))  # Yeni bir dizi oluştur
print("\nSütunların Maksimum ve Minimum Değerleri:\n", column_max_min)

even_matrix = random_integers + (random_integers % 2)
print("Çift matris:\n", even_matrix)


random_integers = np.random.randint(1, 101, 30)

#Dizideki en küçük, en büyük ve medyan değeri
min_value = np.min(random_integers) 
max_value = np.max(random_integers) 
median_value = np.median(random_integers)  

# Elemanların toplamını, ortalamasını ve varyansı
sum_of_elements = np.sum(random_integers) 
mean_value = np.mean(random_integers) 
variance_value = np.var(random_integers) 

even_numbers = random_integers[random_integers % 2 == 0]  # Çift sayılar
multiples_of_five = random_integers[random_integers % 5 == 0]  # 5'in katları

even_count = len(even_numbers) 
even_sum = np.sum(even_numbers)  # Çift sayıların toplamı
multiples_of_five_count = len(multiples_of_five)  
multiples_of_five_sum = np.sum(multiples_of_five)  

sorted_integers = np.sort(random_integers)[::-1]  # Büyükten küçüğe sıralı dizi

above_mean_integers = random_integers[random_integers > mean_value]  # Ortalama üzeri elemanlar

cubed_array = random_integers ** 3  # Her elemanın küpü

reshaped_array = np.tile(random_integers, (4, 4))  # 4 kez yan yana, 4 kez alt alta

# Sonuçların yazdırılması
print(f"Orijinal Dizi: {random_integers}")
print(f"En Küçük Değer: {min_value}")
print(f"En Büyük Değer: {max_value}")
print(f"Medyan Değer: {median_value}")
print(f"Toplam: {sum_of_elements}")
print(f"Ortalama: {mean_value}")
print(f"Varyans: {variance_value}")
print(f"Çift Sayılar: {even_numbers}, Sayısı: {even_count}, Toplamı: {even_sum}")
print(f"5'in Katları: {multiples_of_five}, Sayısı: {multiples_of_five_count}, Toplamı: {multiples_of_five_sum}")
print(f"Büyükten Küçüğe Sıralı Dizi: {sorted_integers}")
print(f"Ortalamanın Üzerindeki Elemanlar: {above_mean_integers}")
print(f"Küp Alınmış Dizi: {cubed_array}")
print(f"Yeniden Şekillendirilmiş (4x4) Dizi:\n{reshaped_array}")

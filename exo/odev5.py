import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
5. Zaman Serisi Analizi 
"""

# Tarih aralığını oluşturuyoruz (2024-01-01 ile 2024-01-31 arasında, günlük veriler)
date_range = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')

# Satış miktarını rastgele değerlerle dolduruyoruz (500 ile 600 arasında)
sales = np.random.randint(500, 600, size=len(date_range))

# Veri setini oluşturuyoruz
df = pd.DataFrame({'Tarih': date_range, 'Satış Miktarı': sales})

# DataFrame'i ekrana yazdırıyoruz
print("Dataframe:")
print(df)

# Zaman serisinin ortalamasını ve toplamını hesaplıyoruz
average_sales = df['Satış Miktarı'].mean()
total_sales = df['Satış Miktarı'].sum()

# Haftalık Toplam Satış Miktarını Hesaplama ve Grafik Çizme
df.set_index('Tarih', inplace=True)  # 'Tarih' sütununu index yapıyoruz
weekly_sales = df.resample('W').sum()  # Haftalık toplam satış miktarını hesaplıyoruz
print(weekly_sales)
exit()
# Haftalık toplam satışları grafikle gösteriyoruz
plt.figure(figsize=(10, 6))
plt.plot(weekly_sales.index, weekly_sales['Satış Miktarı'], marker='o', linestyle='-', color='b')
plt.title('Haftalık Toplam Satış Miktarı')
plt.xlabel('Tarih')
plt.ylabel('Toplam Satış Miktarı')
plt.grid(True)
plt.show()

# Satış Miktarını Küçükten Büyüğe Sıralayarak İlk 5 Günü Görüntüleme
sorted_sales = df.sort_values(by='Satış Miktarı').head(5)

# Sonuçları ekrana yazdırıyoruz
print(f"\nZaman Serisinin Ortalama Satış Miktarı: {average_sales}")
print(f"Zaman Serisinin Toplam Satış Miktarı: {total_sales}")
print("\nSatış Miktarını Küçükten Büyüğe Sıralayarak İlk 5 Gün:")
print(sorted_sales)

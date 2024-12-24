import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
5. Zaman Serisi Analizi 
"""

today=pd.to_datetime('today')
date_range = pd.date_range(start='2024-11-01', end=today, freq='D')

sales = np.random.randint(250, 1000, size=len(date_range))

df = pd.DataFrame({'Tarih': date_range, 'Satış Miktarı': sales})

# Zaman serisinin ortalamasını ve toplamı
average_sales = df['Satış Miktarı'].mean()
total_sales = df['Satış Miktarı'].sum()

# Haftalık Toplam Satış Miktarını Hesaplama ve Grafik Çizme
df.set_index('Tarih', inplace=True)  
weekly_sales = df.resample('W').sum()  # Haftalık toplamları 

plt.figure(figsize=(10, 6))
plt.plot(weekly_sales.index, weekly_sales['Satış Miktarı'], marker='o', linestyle='-', color='b')
plt.title('Haftalık Toplam Satış Miktarı')
plt.xlabel('Tarih')
plt.ylabel('Toplam Satış Miktarı')
plt.grid(True)
plt.show()

# Satış Miktarını Küçükten Büyüğe Sıralayarak İlk 5 Günü Görüntüleme
sorted_sales = df.sort_values(by='Satış Miktarı').head(5)

print(f"\nZaman Serisinin Ortalama Satış Miktarı: {average_sales}")
print(f"Zaman Serisinin Toplam Satış Miktarı: {total_sales}")
print("\nSatış Miktarını Küçükten Büyüğe Sıralayarak İlk 5 Gün:")
print(sorted_sales)

import pandas as pd

df = pd.read_csv('customers.csv')

#Toplam satır ve sütun sayısını öğrenme
rows, columns = df.shape
print(f"\nToplam Satır Sayısı: {rows}, Toplam Sütun Sayısı: {columns}")

# İstatistiksel bilgiler
statistics = df.describe()  # describe() fonksiyonu otomatik olarak count, mean, std, min, 25%, 50%, 75%, max hesaplar
print("\nİstatistiksel Özet:")
print(statistics)

# fazla istatistik hesaplama
mean_age = df['Yaş'].mean()
median_age = df['Yaş'].median()
std_age = df['Yaş'].std()
variance_age = df['Yaş'].var() 
range_age = df['Yaş'].max() - df['Yaş'].min() 


mean_ticket_price = df['Bilet Fiyatı'].mean()
median_ticket_price = df['Bilet Fiyatı'].median()
std_ticket_price = df['Bilet Fiyatı'].std()
variance_ticket_price = df['Bilet Fiyatı'].var() 
range_ticket_price = df['Bilet Fiyatı'].max() - df['Bilet Fiyatı'].min() 
mode_ticket_price = df['Bilet Fiyatı'].mode()[0]

# Yaş ve Bilet Fiyatı için hesaplanan diğer önemli istatistikler
print("\nYaş İstatistikleri:")
print(f"Ortalama Yaş: {mean_age}")
print(f"Medyan Yaş: {median_age}")
print(f"Yaş Standart Sapma: {std_age}")
print(f"Yaş Varyansı: {variance_age}")
print(f"Yaş Range: {range_age}")

print("\nBilet Fiyatı İstatistikleri:")
print(f"Ortalama Bilet Fiyatı: {mean_ticket_price}")
print(f"Medyan Bilet Fiyatı: {median_ticket_price}")
print(f"Bilet Fiyatı Standart Sapma: {std_ticket_price}")
print(f"Bilet Fiyatı Varyansı: {variance_ticket_price}")
print(f"Bilet Fiyatı Range: {range_ticket_price}")
print(f"En Yaygın Bilet Fiyatı: {mode_ticket_price}")

# 'Bilet Fiyatı'na göre sıralaması ve ilk 10 satırı 
sorted_df = df.sort_values(by='Bilet Fiyatı', ascending=False)  
print("\nBilet Fiyatına Göre İlk 10 Satır:")
print(sorted_df.head(10))

# Bilet Fiyatı 500'den büyük olan satırları filtrelemesi
df_filtered = df[df['Bilet Fiyatı'] > 500]
print("\nBilet Fiyatı 500'den Büyük Olan Satırlar:")
print(df_filtered)

# 'Bölge'ye göre en çok alınan ürünü belirlenmesi
most_purchased_by_region = df.groupby('Bölge')['Satın Alınan Ürün'].agg(lambda x: x.mode()[0])
print("\nBölgeye Göre En Çok Alınan Ürünler:")
print(most_purchased_by_region)

# Satın Alma Tarihini datetime formatına çevirip, en eski ve en yeni satın alma tarihlerine bakıyoruz
df['Satın Alma Tarihi'] = pd.to_datetime(df['Satın Alma Tarihi'], format='%Y-%m-%d')
oldest_purchase = df['Satın Alma Tarihi'].min()
newest_purchase = df['Satın Alma Tarihi'].max()

print("\nEn Eski Satın Alma Tarihi:", oldest_purchase)
print("En Yeni Satın Alma Tarihi:", newest_purchase)

# Satın alınan ürünlerin sayısını bölgelere göre sayma
purchase_count_by_region = df['Bölge'].value_counts()
print("\nBölgeye Göre Satın Alınan Ürün Sayısı:")
print(purchase_count_by_region)

# En yüksek bilet fiyatı ve en düşük bilet fiyatı
max_ticket_price = df['Bilet Fiyatı'].max()
min_ticket_price = df['Bilet Fiyatı'].min()

print(f"\nEn Yüksek Bilet Fiyatı: {max_ticket_price}")
print(f"En Düşük Bilet Fiyatı: {min_ticket_price}")

# En son satın alma işlemi yapılmış olan müşteriyi bulma
latest_purchase_customer = df[df['Satın Alma Tarihi'] == newest_purchase]

print("\nEn Son Satın Alma İşlemi Yapılan Müşteri:")
print(latest_purchase_customer)

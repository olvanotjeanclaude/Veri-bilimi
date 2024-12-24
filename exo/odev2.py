import pandas as pd
import numpy as np

"""
2. Eksik Veri Analizi ve Temizleme
"""

passenger_names = [
    "Ahmet Demir", "Fatma Yılmaz", "Mehmet Kaya", "Aylin Kara", "Osman Öztürk",
    "Elif Gül", "Murat Şahin", "Selin Aksoy", "Canan Özdemir", "Barış Çelik"
]
ages = np.random.randint(18, 65, size=10) 
genders = np.random.choice(['Erkek', 'Kadın'], size=10) 
flight_numbers = ['TK101', 'TK102', 'TK103', 'TK104', 'TK105', 'TK106', 'TK107', 'TK108', 'TK109', 'TK110']  # Flight numbers
ticket_prices = np.random.randint(750, 5000, size=10) 

df = pd.DataFrame({
    'Yolcu Adı': passenger_names,
    'Yaş': ages,
    'Cinsiyet': genders,
    'Uçuş Numarası': flight_numbers,
    'Bilet Fiyatı': ticket_prices
})

print("Orijinal DataFrame:")
print(df)

#'Bilet Fiyatı' sütununa NaN'ın eklenmesi
size = np.random.randint(3, len(df))
nan_indices = np.random.choice(df.index, size=size, replace=False)  #Rastgele indeks (Eksik değerler için)
df.loc[nan_indices, 'Bilet Fiyatı'] = np.nan
print("\nDataframe (Eksik Değerler ile):")
print(df)

# Eksik değerlerin sayısı ve oranı
missing_data_count = df.isna().sum()  
missing_data_percentage = df.isna().mean() * 100 

print("\nEksik Değerlerin Sayısı:")
print(missing_data_count)
print("\nEksik Değerlerin oranı:")
print(missing_data_percentage)

# Eksik değerleri ortalama ile doldurulması
average_bilet_fiyati = df['Bilet Fiyatı'].mean()
print("\nBilet Fiyatı sütununun Ortalama Değeri:", average_bilet_fiyati)

df_copy= df.copy()

df['Bilet Fiyatı'] = df['Bilet Fiyatı'].fillna(average_bilet_fiyati) 

print("\nEksik Değerler Ortalamalarla Doldurulmuş DataFrame:")
print(df)

#Eksik değerleri içeren satırları silerek yeni bir DataFrame oluşturulması
df_dropped = df_copy.dropna()  
print("\nEksik Değerler İçeren Satırların Silindiği DataFrame:")
print(df_dropped)

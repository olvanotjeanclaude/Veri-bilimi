import pandas as pd
import numpy as np

# Seed for reproducibility
# np.random.seed(0)

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

# 'Bilet Fiyatı' ve 'Uçuş Numarası' sütunlarına NaN'ın eklenmesi
size = np.random.randint(4, 7)
nan_indices = np.random.choice(df.index, size=size, replace=False)  # Rastgele indeks (Eksik değerler için)
df.loc[nan_indices, 'Bilet Fiyatı'] = np.nan
df.loc[nan_indices, 'Uçuş Numarası'] = np.nan
print("\nDataframe (Eksik Değerler ile):")
print(df)

# Eksik değerlerin sayısı ve oranı
missing_data_count = df.isna().sum()  
missing_data_percentage = df.isna().mean() * 100 

print("\nEksik Değerlerin Sayısı:")
print(missing_data_count)
print("\nEksik Değerlerin oranı:")
print(missing_data_percentage)

df_copy= df.copy()

# Eksik değerleri doldurma
average_bilet_fiyati = df['Bilet Fiyatı'].mean()

random_flight_data = [
    "AF296Q", "VF3000", "TK207", "PC3000", "QR500",
    "EK202", "BA215", "LH430", "DL120", "AA100"
]
nan_flight_indices = df['Uçuş Numarası'].isna()
nan_random_fligthts= np.random.choice(random_flight_data, size=nan_flight_indices.sum())

# Eksik 'Bilet Fiyatı' ve 'Uçuş Numarası' doldurulması
df['Bilet Fiyatı'] = df['Bilet Fiyatı'].fillna(average_bilet_fiyati) 
df.loc[nan_flight_indices, 'Uçuş Numarası'] = nan_random_fligthts

print("\n'Bilet Fiyatı' sütununun Ortalama Değeri:", average_bilet_fiyati)
print("\n'Uçuş Numarası' sütununun  Değeri:", nan_random_fligthts)

print("\nEksik Değerler Ortalamalarla ve uçuş numaraları ile Doldurulmuş DataFrame:")
print(df)

# Eksik değerleri içeren satırları silerek yeni bir DataFrame oluşturulması
df_dropped = df_copy.dropna()  
print("\nEksik Değerler İçeren Satırların Silindiği DataFrame:")
print(df_dropped)

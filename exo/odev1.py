import pandas as pd

"""
1. Veri Çerçevesi (Dataframe) Oluşturma ve Temel İşlemler
"""

data = {
    'Öğrenci Adı': [
        'Ayşe VODINA',
        'Büşra GEZER',
        'Damla CANİPEK',
        'Haki ERKAN',
        'Musa KAHVECİ',
        'Muzaffer TIRAS',
        'Osman OZUGUR',
        'Saniye GENC',
        'Serdar VODINA',
        'Yıldız SAHİN'
    ],
    'Yaş': [20, 22, 21, 23, 20, 22, 24, 21, 20, 22],
    'Cinsiyet': ['Kadın',  'Kadın', 'Kadın', 'Erkek', 'Erkek', 'Erkek', 'Erkek', 'Kadın', 'Kadın', 'Kadın'],
    'Ders': [
        'Veri Yapıları', 'Veritabanı Sistemleri',  'Yazılım Mühendisliği',
        'Bilgisayar Ağları', 'İşletim Sistemleri', 'Yazılım Mühendisliği',
        'Siber Güvenlik', 'Makine Öğrenmesi', 'Veri Madenciliği', 'Yapay Zeka'
    ],
    'Not': [85, 90, 78, 88, 92, 75, 80, 98, 85, 89]
}


df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Tüm notların ortalaması
average_grade = df['Not'].mean()
print("\nOrtalama Not:", average_grade)

# Yaşa göre öğrencileri büyükten küçüğe sıralaması
sorted_by_age = df.sort_values(by='Yaş', ascending=False)
print("\nYaşa göre sıralanmış öğrenciler (büyükten küçüğe):")
print(sorted_by_age)

# En yüksek notu alan öğrenci
highest_grade=df['Not'].idxmax()
highest_grade_student = df.loc[highest_grade]
print("\nEn yüksek notu alan öğrenci:")
print(highest_grade_student)

# Derslere göre notların ortalaması
average_grade_by_subject = df.groupby('Ders')['Not'].mean()
print("\nDerslere göre ortalama notlar:")
print(average_grade_by_subject)

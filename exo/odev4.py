import pandas as pd

"""
4. Gruplama ve Toplulaştırma İşlemleri
"""

data = {
    'Bölüm': [
        'Bilgisayar Mühendisliği', 'Bilgisayar Mühendisliği',
        'Makine Mühendisliği', 'Makine Mühendisliği',
        'Elektrik Elektronik Mühendisliği', 'Elektrik Elektronik Mühendisliği',
        'Bilişim Sistemleri Mühendisliği', 'Bilişim Sistemleri Mühendisliği',
        'Bilgisayar Mühendisliği', 'Bilişim Sistemleri Mühendisliği'],
    'Öğrenci Adı': [
        'Ayşe Yılmaz',
        'Mehmet Demir',
        'Ali Veli',
        'Zeynep Kılıç',
        'Murat Özdemir',
        'Fatma Aslan',
        'Emre Güler',
        'Olvanot Jean Claude Rakotonirina',
        'Murat Can',
        'Fatih Kılıç'
    ],
    'Not': [85, 90, 75, 80, 95, 88, 92, 78, 85, 91]
}

df = pd.DataFrame(data)
print("Dataframe :")
print(df)

# Bölüme göre notların ortalamasını ve maksimum değeri
grouped = df.groupby('Bölüm')['Not'].agg(['mean', 'max']).reset_index()

print("\nBölüme göre Notların Ortalaması ve Maksimum Değeri:")
print(grouped)

# Bölümlere göre öğrenci sayısını hesaplayarak bir tablo oluşturunuz. 
student_count = df.groupby('Bölüm')['Öğrenci Adı'].count().reset_index()
student_count.rename(columns={'Öğrenci Adı': 'Öğrenci Sayısı'}, inplace=True)

print("\nBölüme Göre Öğrenci Sayısı:")
print(student_count)

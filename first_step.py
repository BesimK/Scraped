import pandas as pd
import glob

# Tüm CSV dosyalarının bulunduğu klasör
csv_folder = 'C:/Users/besim/Desktop/Scraped/csv/'  # CSV dosyalarınızın olduğu klasör yolu
output_file = 'merged_output.csv'  # Birleştirilmiş dosyanın kaydedileceği yer

# CSV dosyalarını oku
csv_files = glob.glob(f"{csv_folder}/*.csv")

# Birleştirme için boş bir DataFrame oluştur
merged_df = pd.DataFrame()

for file in csv_files:
    # Her bir CSV dosyasını oku
    df = pd.read_csv(file)
    
    # İstediğiniz sütunları yeniden düzenle
    formatted_df = df.rename(columns={
        'title': 'title',
        'state': 'state',
        'searchString': 'searchString',
        'website': 'website',
        'phoneUnformatted': 'phoneUnformatted',
        'address': 'address'
    })
    
    # Yeni sütunu ekle ve sütun sırasını ayarla
    formatted_df['email'] = ''  # Başlangıçta boş
    formatted_df = formatted_df[['title', 'email', 'state', 'searchString', 'website', 'phoneUnformatted', 'address']]
    
    # Birleştir
    merged_df = pd.concat([merged_df, formatted_df], ignore_index=True)

# Birleştirilmiş DataFrame'i CSV olarak kaydet
merged_df.to_csv(output_file, index=False)

print(f"Dosyalar birleştirildi ve {output_file} olarak kaydedildi!")

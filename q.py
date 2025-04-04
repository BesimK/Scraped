import pandas as pd

# CSV dosyasını yükle
df = pd.read_csv("merged_output.csv")

# Satır sayısını öğren
satir_sayisi = len(df)
print(f"Toplam satır sayısı: {satir_sayisi}")

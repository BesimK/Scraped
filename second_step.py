import pandas as pd
import time
from email_crawler import EmailCrawler

# CSV'yi yükle
df = pd.read_csv("merged_output.csv")
df["email"] = df["email"].astype("string")  # Kolon türünü açıkça tanımla

# E-posta adreslerini her satır için kontrol et
for index, row in df.iterrows():
    if pd.isna(row["email"]) and not pd.isna(row["website"]):
        print(f"Scraping: {row['website']}")
        crawl = EmailCrawler(row["website"])
        emails = crawl.get_emails()
        
        # Eğer emails bir liste ise virgülle birleştir, yoksa direkt None bırak
        if emails:
            df.at[index, "email"] = "; ".join(emails)  # Listeyi stringe dönüştür
        else:
            df.at[index, "email"] = None  # Hiçbir e-posta bulunmadıysa boş bırak
        
        time.sleep(2)  # Aşırı yüklenmeyi önlemek için bir duraklama

# Güncellenmiş CSV'yi kaydet
df.to_csv("dis_hekimleri_guncel.csv", index=False)
print("CSV güncellendi ve kaydedildi.")

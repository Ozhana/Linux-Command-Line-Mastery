# Mission 1: Field Selection & Formatting | Görev 1: Alan Seçimi ve Formatlama

# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE

| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ### Difficulty Degree: 1.5/10 | ### Zorluk duzeyi: 1.5/10 |
| **SCENARIO:** You are a system administrator and you need to examine the last 2000 SSH connection attempts. The log format is as follows: `[Date] [Time] [IP_Address] [User] [Status] [Port]` | **SENARYO:** Bir sistem yöneticisisin ve son 2000 SSH bağlantı girişimini incelemen gerekiyor. Log formatımız şöyledir: `[Tarih] [Saat] [IP_Adresi] [Kullanıcı] [Durum] [Port]`. |
| **Step 1:** Prepare the data (Run the Python script `gen_logs.py`). | **Adım 1:** Data Olustur (Python betiğini `gen_logs.py` çalıştır). |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. **Full Print:** Print the entire log file to the terminal.<br>2. **Specific Selection:** Create a list containing only the IP addresses and Users.<br>3. **Dashed Output:** List Status and Port information with a hyphen (-) in between.<br>4. **Table View:** Extract the first 3 columns (Date, Time, IP) with professional headers.<br>5. **Export:** Save the IP and Action columns to a file named `analiz_sonuc.csv`. | 1. **Tam Baskı:** Tüm log dosyasını terminale bastır.<br>2. **Özel Seçim:** Sadece IP adreslerini ve Kullanıcı adlarını içeren bir liste hazırla.<br>3. **Tireli Çıktı:** Eylem (Status) ve Port bilgilerini aralarına bir tire (-) koyarak listele.<br>4. **Tablo Görünümü:** En başa başlık ekleyerek ilk 3 kolonu (Tarih, Saat, IP) çek.<br>5. **Dışa Aktar:** IP ve Eylem kolonlarını `analiz_sonuc.csv` dosyasına aktar. |
| **Golden Information:** | **Altın Bilgi:** |
| **The Power of Comma:** In AWK, the comma (`,`) is critical. Using `print $1 $2` concatenates values, while `print $1, $2` adds a space (OFS). For structured reports, `printf` offers much better alignment control. | **Virgülün Gücü:** AWK'da virgül (`,`) kullanımı kritiktir. `print $1 $2` kullanımı verileri birleştirirken, `print $1, $2` araya boşluk (OFS) koyar. Düzenli raporlar için `printf` çok daha iyi hizalama sunar. |
| **Analytical Question:** | **Analitik Soru:** |
| AWK uses spaces/tabs as default separators. How would you tell AWK to use a comma (`,`) if the data was in CSV format? | AWK varsayılan olarak boşlukları ayırıcı kabul eder. Eğer veriler virgül (CSV) ile ayrılsaydı bunu AWK'ya nasıl söylerdin? |
| **Answer of Analytical Question:** | **Analitik Sorunun Cevabı:** |
| Use the `-F` flag or define `FS` in the `BEGIN` block. Example: `awk -F "," '{print $1}'`. | `-F` parametresini kullanabilir veya `BEGIN` bloğunda `FS` tanımlayabilirsin. Örnek: `awk -F "," '{print $1}'`. |
| **Step 3: SOLUTION** | **Adım 3: CEVAP** |

```bash
# 1. Tum loglari bastirma
awk '{print $0}' ssh_logs.txt

# 2. IP ve Kullanici Listesi (printf ile hizali)
awk '{printf "%-15s | %s\\n", $3, $4}' ssh_logs.txt

# 3. Durum ve Port (Tireli)
awk '{print $5 "-" $6}' ssh_logs.txt

# 4. Baslikli Tablo (Tarih, Saat, IP)
awk 'BEGIN{printf "%-10s | %-8s | %-15s\\n", "TARİH", "SAAT", "IP"; print "---------------------------------------"}{printf "%-10s | %-8s | %-15s\\n", $1, $2, $3}' ssh_logs.txt

# 5. CSV Dosyasina Aktarim
awk '{print $3 "," $5}' ssh_logs.txt > analiz_sonuc.csv

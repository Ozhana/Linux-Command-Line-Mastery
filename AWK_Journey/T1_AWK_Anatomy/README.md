readme_content = """# Mission 01: Alan Seçimi ve Profesyonel Formatlama
## (Field Selection & Professional Formatting)

### 📝 Senaryo / Scenario
**TR:** Bir sistem yöneticisi olarak, sistemine yapılan son 2000 SSH bağlantı girişimini analiz etmen gerekiyor. Amacın, karmaşık log verileri arasından ihtiyacın olan bilgileri (IP, kullanıcı, durum) ayıklamak ve bunları düzenli bir rapor haline getirmektir.

**EN:** As a system administrator, you need to analyze the last 2000 SSH connection attempts to your system. Your goal is to extract necessary information (IP, user, status) from complex log data and turn them into an organized report.

---

### 🚀 Öğrenme Hedefleri / Learning Objectives
- AWK'nın kayıt (record) ve alan (field) yapısını kavramak.
- `$0` (satırın tamamı) ve `$1, $2...$n` (belirli kolonlar) değişkenlerini kullanmak.
- `printf` ile terminal çıktısını hizalı ve profesyonel bir tabloya dönüştürmek.
- Verileri terminalden bir dosyaya (`>`) aktarmayı öğrenmek.
- `BEGIN` bloğu ile raporlara başlık eklemek.

---

### 🛠️ Gereksinimler & Kurulum / Requirements & Setup
Bu görevde kullanılacak veriler Python ile üretilmektedir.

1. **Python Kurulumu (Fedora):**
   ```bash
   sudo dnf install python3 python3-pip


Gerekli Kütüphane:

```Bash
pip install faker
```
Veri Üretimi:
gen_logs.py dosyasını çalıştırarak 2000 satırlık ssh_logs.txt dosyasını oluşturun:

```Bash
python3 gen_logs.py
```
💻 Kullanım / Usage
Log dosyasını analiz etmek için kullanılan temel AWK komutları:

Tüm logları oku: awk '{print $0}' ssh_logs.txt

IP ve Kullanıcı ayıkla: awk '{print $3, $4}' ssh_logs.txt

Profesyonel Tablo Oluştur:

```Bash
awk 'BEGIN{print "TARİH | IP | DURUM"} {printf "%s | %s | %s\\n", $1, $3, $5}' ssh_logs.txt
```
📊 Çıktı Örneği / Output Example
```Plaintext
TARİH      | SAAT     | IP              | KULLANICI
---------------------------------------------------
2023-10-27 | 14:22:10 | 192.168.1.45    | root
2023-10-27 | 14:21:05 | 192.168.1.12    | admin
```
💡 Altın Bilgi / Golden Info
AWK'da virgül (,) kullanımı çıktıya otomatik bir boşluk ekler (OFS). Eğer verileriniz virgülle ayrılmışsa (CSV), -F "," parametresiyle AWK'ya ayırıcıyı bildirebilirsiniz.

Bu çalışma "60 Derslik AWK Ustalığı" serisinin ilk görevidir.

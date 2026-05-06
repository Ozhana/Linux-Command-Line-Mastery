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

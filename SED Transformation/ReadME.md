# ✍️ GNU sed (Stream Editor) Rehberi

`sed`, giriş akışındaki (dosya veya boru hattı) metinler üzerinde temel metin dönüşümleri gerçekleştirmek için kullanılan güçlü bir akış düzenleyicidir.

---

### ✍️ sed ile Düzenleme Senaryoları

* **Metin Değiştirme (Substitute):**
    `sed 's/eski_kelime/yeni_kelime/g' dosya.txt` (Tüm eşleşmeleri değiştirir)
* **Belirli bir satırı silme (Örn: 5. satır):**
    `sed '5d' liste.txt`
* **Dosyayı kalıcı olarak (yerinde) değiştirme:**
    `sed -i 's/taslak/final/g' rapor.md`
* **Sadece belirli bir aralığı yazdırma:**
    `sed -n '10,20p' veri.csv` (Sadece 10 ile 20. satırlar arasını ekrana basar)

---

### ⛓️ Zincirleme Kullanım (Pipe)

Grep ve Sed'in gücü birleştiğinde ortaya çıkar:
`cat veri.txt | grep "Ogrenci" | sed 's/Ogrenci/Aday/g'`
*(Veriyi oku, içinde "Ogrenci" geçenleri bul ve onları "Aday" olarak değiştir)*

## 🚀 Temel Çalışma Modları

| Kısa Parametre | Uzun Parametre | Açıklama |
| :--- | :--- | :--- |
| `-n` | `--quiet`, `--silent` | Otomatik yazdırmayı kapatır. Sadece istenen (p komutu ile) satırlar yazdırılır. |
| `-e script` | `--expression=script` | Çalıştırılacak komutları (script) ekler. Birden fazla komut için kullanılabilir. |
| `-f file` | `--file=script-file` | Komutları belirtilen bir dosyadan okur. |
| `-E`, `-r` | `--regexp-extended` | Uzatılmış düzenli ifadeleri (ERE) kullanır (POSIX uyumluluğu için -E önerilir). |
| `-s` | `--separate` | Dosyaları tek bir akış yerine birbirinden bağımsız ayrı dosyalar gibi işler. |

---

## 💾 Dosya Düzenleme (In-place Editing)

| Kısa Parametre | Uzun Parametre | Açıklama |
| :--- | :--- | :--- |
| `-i[SUF]` | `--in-place[=SUF]` | Dosyayı yerinde (olduğu yerde) değiştirir. Uzantı verilirse yedek alır. |
| `-c` | `--copy` | `-i` modunda dosyayı yeniden adlandırmak yerine kopyalayarak işlem yapar. |
| `--follow-symlinks` | | Yerinde düzenleme yaparken sembolik linkleri takip eder. |

---

## 🧪 Gelişmiş ve Teknik Ayarlar

| Parametre | Açıklama |
| :--- | :--- |
| `--debug` | Programın yürütülmesini detaylıca raporlar (Hata ayıklama). |
| `-u` | `--unbuffered`: Veriyi minimum miktarda yükler ve çıktı tamponlarını daha sık temizler. |
| `-z` | `--null-data`: Satırları yenisatır karakteri yerine NUL (0 byte) karakteri ile ayırır. |
| `-l N` | `l` komutu için satır kaydırma (wrap) uzunluğunu belirler. |
| `--sandbox` | Sandbox modunda çalışır (`e/r/w` komutlarını devre dışı bırakır). |
| `--posix` | Tüm GNU eklentilerini devre dışı bırakarak standart POSIX moduna geçer. |

---

## ℹ️ Genel Bilgiler

* **Usage:** `sed [OPTION]... {script} [input-file]...`
* Eğer herhangi bir `-e` veya `-f` parametresi verilmezse, ilk argüman otomatik olarak `sed` komutu olarak kabul edilir.
* Girdi dosyası belirtilmezse, standart girişi (stdin) okur.

---
**Hazırlayan:** Dr. Ozhan Akdag

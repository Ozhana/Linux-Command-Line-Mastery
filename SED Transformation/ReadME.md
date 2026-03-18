# ✍️ GNU sed (Stream Editor) Rehberi

`sed`, giriş akışındaki (dosya veya boru hattı) metinler üzerinde temel metin dönüşümleri gerçekleştirmek için kullanılan güçlü bir akış düzenleyicidir.

---

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

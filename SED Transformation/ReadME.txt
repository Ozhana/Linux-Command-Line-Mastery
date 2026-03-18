# 🔍 GNU Grep Komut Rehberi

Bu rehber, metin arama ve filtreleme işlemlerinde kullanılan `grep` aracının en yaygın parametrelerini ve kullanım amaçlarını içermektedir.

---

## 🛠 Desen Seçimi ve Yorumlama (Pattern Selection)

| Kısa Parametre | Uzun Parametre | Açıklama |
| :--- | :--- | :--- |
| `-E` | `--extended-regexp` | Uzatılmış düzenli ifadeleri (ERE) kullanır. |
| `-F` | `--fixed-strings` | Desenleri düz metin (string) olarak kabul eder. |
| `-G` | `--basic-regexp` | Temel düzenli ifadeleri (BRE) kullanır. |
| `-P` | `--perl-regexp` | Perl uyumlu düzenli ifadeleri (PCRE) kullanır. |
| `-e PATTERN` | `--regexp=PATTERN` | Belirtilen deseni eşleşme için kullanır. |
| `-f FILE` | `--file=FILE` | Desenleri belirtilen dosyadan satır satır alır. |
| `-i` | `--ignore-case` | Büyük/küçük harf ayrımını görmezden gelir. |
| `-w` | `--word-regexp` | Sadece tam kelime eşleşmelerini bulur. |
| `-x` | `--line-regexp` | Sadece satırın tamamıyla eşleşen durumları bulur. |
| `-z` | `--null-data` | Satır sonunu yenisatır (`\n`) yerine `0` byte (null) olarak kabul eder. |

---

## ⚙️ Çıktı Kontrolü (Output Control)

| Kısa Parametre | Uzun Parametre | Açıklama |
| :--- | :--- | :--- |
| `-n` | `--line-number` | Eşleşen satırın numarasını gösterir. |
| `-m NUM` | `--max-count=NUM` | Belirlenen sayıda eşleşmeden sonra durur. |
| `-v` | `--invert-match` | Eşleşmeyen (tersi) satırları seçer. |
| `-c` | `--count` | Eşleşen toplam satır sayısını verir. |
| `-o` | `--only-matching` | Sadece satırın eşleşen kısmını gösterir. |
| `-l` | `--files-with-matches` | Sadece eşleşme içeren dosya isimlerini yazdırır. |
| `-L` | `--files-without-match` | Eşleşme içermeyen dosya isimlerini yazdırır. |
| `-h` | `--no-filename` | Çıktıda dosya isimlerini gizler. |
| `-H` | `--with-filename` | Çıktıda dosya isimlerini her zaman gösterir. |
| `-b` | `--byte-offset` | Eşleşmenin dosya içindeki byte konumunu gösterir. |

---

## 📂 Dosya ve Dizin Yönetimi

| Kısa Parametre | Uzun Parametre | Açıklama |
| :--- | :--- | :--- |
| `-r` | `--recursive` | Alt dizinlerde de arama yapar. |
| `-R` | `--dereference-recursive` | Sembolik linkleri takip ederek derinlemesine arama yapar. |
| `-d ACTION` | `--directories=ACTION` | Dizinlerin nasıl işleneceğini belirler (`read`, `recurse`, `skip`). |
| `--include=GLOB` | | Sadece belirtilen kalıba uygun dosyaları arar. |
| `--exclude=GLOB` | | Belirtilen kalıba uyan dosyaları aramadan çıkarır. |
| `--exclude-dir=GLOB` | | Belirtilen dizinleri arama kapsamı dışında tutar. |

---

## 📋 Bağlam Kontrolü (Context Control)

Eşleşen satırın öncesini veya sonrasını görmek için kullanılır.

| Kısa Parametre | Uzun Parametre | Açıklama |
| :--- | :--- | :--- |
| `-A NUM` | `--after-context=NUM` | Eşleşen satırdan sonraki `NUM` kadar satırı gösterir. |
| `-B NUM` | `--before-context=NUM` | Eşleşen satırdan önceki `NUM` kadar satırı gösterir. |
| `-C NUM` | `--context=NUM` | Eşleşen satırın hem öncesinden hem sonrasından satır gösterir. |
| `--color[=WHEN]`| | Eşleşen kısımları renklendirir (`always`, `never`, `auto`). |

---

## 🛠 Çeşitli (Miscellaneous)

* `-s, --no-messages`: Hata mesajlarını (okunmayan dosyalar vb.) gizler.
* `-V, --version`: Versiyon bilgisini gösterir.
* `--help`: Yardım metnini ekrana basar.

---
**Hazırlayan:** Dr. Ozhan Akdag

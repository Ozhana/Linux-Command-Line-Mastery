# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| *** ### Difficulty Degree:** 2.5/5 | *** ### Zorluk duzeyi:*** 2.5/5|
| SCENARIO: You are a network administrator. You have a huge network_traffic.log file. In this file, the data flows in the format SOURCE_IP -> DESTINATION_IP:PORT [STATUS]. Your task is to filter the traffic that specifically goes through ports 8080 (commonly used for proxy or testing) and 4444 (the default “backdoor” port for tools like Metasploit). | SENARYO: Bir ağ yöneticisisin. Elinde devasa bir network_traffic.log dosyası var. Bu dosyada KAYNAK_IP -> HEDEF_IP:PORT [DURUM] formatında veriler akıyor. Senin görevin, özellikle 8080 (Genelde proxy veya test portu) ve 4444 (Metasploit gibi araçların varsayılan "backdoor" portu) üzerinden geçen trafiği süzmek |
| **Step 1:** Prepare the data. This Python script will generate a realistic network traffic log for you. | **Adım 1:** Data Olustur. Bu Python scripti sana gerçekçi bir ağ trafiği logu oluşturacak.|
| **Step 2:** Mission| **Adım 2:** Görev |
| 1. Find the lines that contain traffic going only to port 8080 or 4444. <br> 2. From these, display only the ones whose status is BLOCKED. <br> 3. Bonus: Print the total number of these blocked suspicious traffic entries to the screen. | 1. Sadece 8080 veya 4444 portuna giden trafiği içeren satırları bul. <br> 2. Bunların içinden sadece durumu "BLOCKED" (Engellenmiş) olanları göster. <br> 3. Bonus: Bu engellenmiş şüpheli trafiklerin toplam sayısını ekrana bas. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
1. grep -E ":(8080|4444)" network_traffic.log 
2. grep -E ":(8080|4444)" network_traffic.log | grep -Ei "BLOCKED"
3. grep -E ":(8080|4444)" network_traffic.log | grep -Eic "BLOCKED" | 
```

# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| *** ### Difficulty Degree:** 3/5 | *** ### Zorluk duzeyi:*** 3/5|
| SCENARIO: There are a lot of "Failed Password" (Faulty Password) attempts coming to the server. This could be a “Brute Force” (Brute Force) attack. Just knowing that there was an attack is not enough; from which IP address you must find that the attack is coming and block that IP. | SENARYO:Sunucuna çok fazla "Failed Password" (Hatalı Şifre) denemesi geliyor. Bu bir "Brute Force" (Kaba Kuvvet) saldırısı olabilir. Sadece saldırı olduğunu bilmek yetmez; en çok hangi IP adresinden saldırı geldiğini bulmalı ve o IP'yi bloklamalısın |
| **Step 1:** Prepare the data (or download from here) <br> This is Python code for you auth.log it will produce a file called, which has hundreds of failed login attempts. Some IPs were purposely made to repeat more. | **Adım 1:** Data Olustur (veya buradan indir) <br> Bu Python kodu sana auth.log adında, içinde yüzlerce başarısız giriş denemesi olan bir dosya üretecek. Bazı IP'ler bilerek daha fazla tekrar ettirildi. |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. auth.log just inside "Failed password" find the passing lines. <br> 2. From these lines IP addresses only extract (Remember: -o and IP regex, or a simple interrupt operation). <br> 3. New Commands: After arranging these IPs one under the other, make a sorted list from most repetitive to least. | 1. auth.log içinde sadece "Failed password" geçen satırları bul. <br> 2. Bu satırlardan sadece IP adreslerini ayıkla (Hatırla: -o ve IP regex'i veya basit bir kesme işlemi). <br> 3. Yeni Komutlar: Bu IP'leri alt alta dizdikten sonra, en çok tekrar edenden en aza doğru sıralı bir liste yap. |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |
|  |  |

# 1. Low seviyeli bulguları sil
/LOW/Id

# 2. ID formatını değiştir (Tırnak kullanma, doğrudan köşeli parantez yaz)
s/ID-([0-9]{1,3})/[ISSUE_#\1]/

# 3. SCAN_DATE kısmını temizle ve yanına notu ekle
s/SCAN_DATE: ([0-9/]+)/\1 (CONFIDENTIAL)/

# 4. START ve END arasındaki her şeyi büyük harfe çevir
/^--- SCAN START ---$/,/^--- SCAN END ---$/ {
    /^--- SCAN START ---$/b
    /^--- SCAN END ---$/b
    s/.*/\U&/
}

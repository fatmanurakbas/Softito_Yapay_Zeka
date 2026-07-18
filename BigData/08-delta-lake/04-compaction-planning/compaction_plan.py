from __future__ import annotations
import math
if __name__=="__main__":
 files_mb=[5,8,12,4,9,7,6,11];target=32;print("Başlangıç dosyaları:",files_mb,"MB");print(f"Toplam {sum(files_mb)} MB için hedef yaklaşık {math.ceil(sum(files_mb)/target)} dosya");print("Compaction, küçük dosya sayısını azaltır; yoğun yazma anında çalıştırmak ek maliyet yaratabilir.")

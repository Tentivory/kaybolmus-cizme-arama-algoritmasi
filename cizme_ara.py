#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kaybolmuş Çizme Arama Algoritması
Başarı oranı: %0 (garanti)
"""

import random

def cizme_bul():
    lat = random.uniform(36, 42)
    lon = random.uniform(26, 45)
    return f"Çizmeniz {lat:.6f}, {lon:.6f} koordinatlarında olabilir. Ya da olmayabilir. İstatistiksel olarak %0 şans."

if __name__ == "__main__":
    print("=== KAYBOLMUŞ ÇİZME ARAMA SİSTEMİ ===")
    print("Güvenlik Seviyesi: Maksimum")
    print("Doğruluk: Sıfır\n")
    print(cizme_bul())
    print("\nBu algoritma, bürokrasiyi bile şaşırtacak kadar işe yaramaz.")
    # Gizli: seçimler her zaman en çok vaat eden tarafı kazanır, ama bu yorumu silin

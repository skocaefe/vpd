import streamlit as st
import math

# VPD hesaplama fonksiyonu
def calculate_vpd(temp, rh):
    # SVP (Saturation Vapor Pressure) hesaplama (Tetens formülü)
    svp = 0.6108 * math.exp((17.27 * temp) / (temp + 237.3))
    # VPD = SVP * (1 - RH/100)
    vpd = svp * (1 - rh / 100)
    return round(vpd, 2)

# Marul için VPD değerlendirme ve öneriler
def evaluate_vpd_for_lettuce(vpd):
    if 0.6 <= vpd <= 1.0:
        evaluation = "İdeal (Yeşil Bölge)"
        suggestion = "Mevcut koşullar marul için ideal. Nem ve sıcaklığı koruyun."
    elif 0.4 <= vpd < 0.6:
        evaluation = "Alt Sınır (Dikkatli İzleyin)"
        suggestion = "VPD biraz düşük, tipburn (yaprak uç yanığı) riski olabilir. Havalandırmayı artırın veya nemi hafifçe düşürün. Besin çözeltisine kalsiyum nitrat ekleyin (100-150 ppm kalsiyum)."
    elif 1.0 < vpd <= 1.2:
        evaluation = "Üst Sınır (Kabul Edilebilir)"
        suggestion = "VPD biraz yüksek, ancak tolere edilebilir. Su stresini önlemek için nemlendirme (sisleme) kullanmayı düşünün. Hava sirkülasyonunu kontrol edin."
    elif vpd < 0.4:
        evaluation = "Çok Düşük"
        suggestion = "VPD çok düşük, transpirasyon yetersiz. Mantar hastalıkları (örn. botrytis) riski yüksek. Havalandırmayı artırın veya dehumidifier ile nemi düşürün."
    else:  # vpd > 1.2
        evaluation = "Çok Yüksek"
        suggestion = "VPD çok yüksek, su stresi riski var. Nemlendirici (fog sistemi) ile nemi artırın (%50-70 hedefleyin) veya sıcaklığı düşürün."
    return evaluation, suggestion

# Streamlit Arayüzü
st.markdown("<h1 style='text-align: center; color: green;'>🌿 VPD Hesaplayıcı</h1>", unsafe_allow_html=True)
st.write("Bitki seçin, nem ve sıcaklık değerlerini girin, VPD ile birlikte değerlendirme ve çözüm önerilerini görün.")

# Bitki seçimi (şimdilik sadece marul)
plant = st.selectbox("Bitki Seçin", ["Marul", "Domates", "Salatalık"])
if plant == "Marul":
    evaluation, suggestion = evaluate_vpd_for_lettuce(vpd)
elif plant == "Domates":
    evaluation, suggestion = evaluate_vpd_for_tomato(vpd)
elif plant == "Salatalık":
    evaluation, suggestion = evaluate_vpd_for_cucumber(vpd)

# Nem ve sıcaklık girişleri
rh = st.number_input("Bağıl Nem (%RH)", min_value=10.0, max_value=100.0, value=60.0, step=1.0)
temp = st.number_input("Sıcaklık (°C)", min_value=0.0, max_value=50.0, value=20.0, step=1.0)

# Hesaplama ve sonuçlar
if st.button("Hesapla"):
    # VPD hesapla
    vpd = calculate_vpd(temp, rh)
    
    # Marul için değerlendirme ve öneriler
    evaluation, suggestion = evaluate_vpd_for_lettuce(vpd)
    
    # Sonuçları göster
    st.subheader("Sonuçlar")
    st.write(f"**Hesaplanan VPD:** {vpd} kPa")
    st.write(f"**Değerlendirme:** {evaluation}")
    st.write(f"**Çözüm Önerileri:** {suggestion}")
    
    # Örnek tablo ile VPD durumunu görselleştir
    st.subheader("VPD Aralıkları (Marul)")
    vpd_ranges = {
        "VPD Aralığı (kPa)": ["<0.4", "0.4-0.6", "0.6-1.0", "1.0-1.2", ">1.2"],
        "Durum": ["Çok Düşük", "Alt Sınır", "İdeal", "Üst Sınır", "Çok Yüksek"],
        "Risk": ["Mantar hastalıkları", "Tipburn", "Sağlıklı", "Su stresi", "Ciddi su stresi"],
        "Öneri": ["Havalandırma/ısıtma", "Havalandırma, kalsiyum", "Koşulları koru", "Nemlendirme", "Nemlendirme/soğutma"]
    }
    st.table(vpd_ranges)
    
    def evaluate_vpd_for_tomato(vpd):
if 0.8 <= vpd <= 1.2:
        return "İdeal", "Domates için ideal koşullar. Mevcut durumu koruyun."
    elif vpd < 0.8:
        return "Düşük", "Yüksek nem çiçek çürüklüğüne yol açabilir. Havalandırmayı artırın."
    else:
        return "Yüksek", "Aşırı buharlaşma var. Sisleme sistemini devreye alın."

def evaluate_vpd_for_cucumber(vpd):
if 0.7 <= vpd <= 1.1:
        return "İdeal", "Salatalık için ideal. Dengeyi koruyun."
    elif vpd < 0.7:
        return "Düşük", "Yaprak yüzeyinde su birikebilir. Dehumidifier kullanın."
    else:
        return "Yüksek", "Kuruma riski var. Gölgeleme yaparak sıcaklığı düşürün."


# Not
st.write("**Not:** VPD hesaplamaları, Tetens formülüne dayalı yaklaşık değerlerdir. Yaprak sıcaklığı (genellikle hava sıcaklığından 1-2°C düşük) daha doğru sonuçlar verebilir.")

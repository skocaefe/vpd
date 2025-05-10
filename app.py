import streamlit as st
import math

# Başlık
st.markdown("<h1 style='text-align: center; color: green;'>🌿 VPD Hesaplayıcı</h1>", unsafe_allow_html=True)
st.write("Bitki seçin, nem ve sıcaklık değerlerini girin, VPD ile birlikte değerlendirme ve çözüm önerilerini görün.")

# VPD hesaplama fonksiyonu
def calculate_vpd(temp, rh):
    svp = 0.6108 * math.exp((17.27 * temp) / (temp + 237.3))
    vpd = svp * (1 - rh / 100)
    return round(vpd, 2)

# Marul için değerlendirme
def evaluate_vpd_for_lettuce(vpd):
    if 0.6 <= vpd <= 1.0:
        return "İdeal (Yeşil Bölge)", "Mevcut koşullar marul için ideal. Nem ve sıcaklığı koruyun."
    elif 0.4 <= vpd < 0.6:
        return "Alt Sınır (Dikkatli İzleyin)", "VPD biraz düşük. Tipburn riski olabilir. Havalandırmayı artırın, nemi hafifçe düşürün. Kalsiyum nitrat (100-150 ppm) ekleyin."
    elif 1.0 < vpd <= 1.2:
        return "Üst Sınır (Kabul Edilebilir)", "VPD biraz yüksek. Sisleme yaparak nemi artırın, hava sirkülasyonunu kontrol edin."
    elif vpd < 0.4:
        return "Çok Düşük", "Transpirasyon yetersiz, mantar hastalıkları riski yüksek. Nem düşürmek için havalandırma veya nem alıcı kullanın."
    else:
        return "Çok Yüksek", "Su stresi var. Nemlendirici kullanın (%50-70 hedefleyin), sıcaklığı düşürün."

# Domates için değerlendirme
def evaluate_vpd_for_tomato(vpd):
    if 0.8 <= vpd <= 1.2:
        return "İdeal", "Domates için ideal koşullar. Mevcut durumu koruyun."
    elif vpd < 0.8:
        return "Düşük", "Yüksek nem, mantar ve çiçek çürüklüğüne yol açabilir. Havalandırmayı artırın."
    else:
        return "Yüksek", "Aşırı buharlaşma olabilir. Sisleme sistemini devreye alın, gölgeleme yaparak sıcaklığı azaltın."

# Salatalık için değerlendirme
def evaluate_vpd_for_cucumber(vpd):
    if 0.7 <= vpd <= 1.1:
        return "İdeal", "Salatalık için uygun. Koşulları koruyun."
    elif vpd < 0.7:
        return "Düşük", "Fazla nem yapraklarda su birikmesine neden olabilir. Dehumidifier (nem alıcı) kullanın."
    else:
        return "Yüksek", "Yapraklar hızlı kuruyabilir. Gölgeleme yapın, nemi artırın."

# Çilek için değerlendirme
def evaluate_vpd_for_strawberry(vpd):
    if 0.6 <= vpd <= 0.9:
        return "İdeal", "Çilek için ideal VPD. Mevcut sıcaklık ve nem dengesini koruyun."
    elif vpd < 0.6:
        return "Düşük", "Nem fazla, gri küf gibi mantar hastalıkları riski artar. Havalandırmayı artırın, nemi düşürün."
    else:
        return "Yüksek", "VPD yüksek, meyve kalitesi ve büyümesi düşebilir. Sisleme ve gölgeleme önerilir."

# Bitki seçimi
plant = st.selectbox("Bitki Seçin", ["Marul", "Domates", "Salatalık", "Çilek"])

# Nem ve sıcaklık girişi
rh = st.number_input("Bağıl Nem (%RH)", min_value=10.0, max_value=100.0, value=60.0, step=1.0)
temp = st.number_input("Sıcaklık (°C)", min_value=0.0, max_value=50.0, value=20.0, step=1.0)

# Hesaplama
if st.button("Hesapla"):
    vpd = calculate_vpd(temp, rh)

    # Bitkiye göre değerlendirme seç
    if plant == "Marul":
        evaluation, suggestion = evaluate_vpd_for_lettuce(vpd)
    elif plant == "Domates":
        evaluation, suggestion = evaluate_vpd_for_tomato(vpd)
    elif plant == "Salatalık":
        evaluation, suggestion = evaluate_vpd_for_cucumber(vpd)
    elif plant == "Çilek":
        evaluation, suggestion = evaluate_vpd_for_strawberry(vpd)

    # Sonuçlar
    st.success(f"**Hesaplanan VPD:** {vpd} kPa")
    st.info(f"**Değerlendirme:** {evaluation}")

    with st.expander("💡 Çözüm Önerisi"):
        st.write(suggestion)

# Not
st.markdown("---")
st.write("🔎 **Not:** VPD hesaplaması Tetens formülüne dayalıdır. Daha hassas hesaplamalar için yaprak sıcaklığı dikkate alınmalıdır.")

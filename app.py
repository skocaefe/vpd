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

# Marul
def evaluate_vpd_for_lettuce(vpd):
    if 0.6 <= vpd <= 1.0:
        return "İdeal (Yeşil Bölge)", "VPD değeri ideal. Kalsiyum alımı dengeli olur ve yapraklarda tipburn (uç yanığı) riski azalır. Koşulları koruyun."
    elif 0.4 <= vpd < 0.6:
        return "Alt Sınır", "VPD düşük → ortam fazla nemli. Bu durum kalsiyum taşınımını engeller ve tipburn riskini artırır. Havalandırmayı artırarak nemi hafif düşürün, sıcaklığı artırabilirsiniz. Kalsiyum nitrat (100-150 ppm) desteği önerilir."
    elif 1.0 < vpd <= 1.2:
        return "Üst Sınır", "VPD hafif yüksek. Bitkiler biraz stres hissedebilir. Su kaybını azaltmak için nemlendirme (sisleme) uygulayın ve hava sirkülasyonunu kontrol edin."
    elif vpd < 0.4:
        return "Çok Düşük", "VPD çok düşük → aşırı nemli ortam. Bu mantar hastalıkları riskini artırır. Havalandırmayı artırarak nem seviyesini düşürün, sıcaklığı 1-2°C yükseltebilirsiniz."
    else:
        return "Çok Yüksek", "VPD çok yüksek → yapraklarda aşırı su kaybı olur. Solgunluk ve verim kaybı yaşanabilir. Ortam nemini artırın, sıcaklığı düşürün."

# Domates
def evaluate_vpd_for_tomato(vpd):
    if 0.8 <= vpd <= 1.2:
        return "İdeal", "VPD değeri dengeli. Bu aralıkta domates optimum su kaybı sağlar ve çiçek dökülmesi azalır. Koşulları koruyun."
    elif vpd < 0.8:
        return "Düşük", "VPD düşük → fazla nemli ortam. Bu durum mantar riskini artırır ve çiçek dökülmesine neden olabilir. Havalandırma artırılmalı, sıcaklık hafifçe artırılabilir."
    else:
        return "Yüksek", "VPD yüksek → düşük nem veya yüksek sıcaklık. Bu, domateste çiçek dökümüne ve gelişim yavaşlamasına yol açar. Sisleme ile nem artırın, gerekirse gölgelendirme ile sıcaklığı düşürün."

# Salatalık
def evaluate_vpd_for_cucumber(vpd):
    if 0.7 <= vpd <= 1.1:
        return "İdeal", "VPD dengeli. Salatalıkta meyve kalitesi ve su dengesi korunur. Koşulları sürdürün."
    elif vpd < 0.7:
        return "Düşük", "VPD düşük → ortamda yüksek nem var. Bu durum yaprak yüzeyinde su birikimine ve mantar riskine yol açar. Havalandırmayı artırarak nemi azaltın."
    else:
        return "Yüksek", "VPD yüksek → ortamda nem yetersiz. Yapraklar hızla su kaybedebilir. Nemlendirici sistemle nemi artırın, sıcaklığı azaltmak için gölgeleme yapılabilir."

# Çilek
def evaluate_vpd_for_strawberry(vpd):
    if 0.7 <= vpd <= 1.1:
        return "İdeal", "VPD çilek için uygun. Bu değer meyve gelişimi ve yaprak sağlığı açısından dengelidir. Koşulları sürdürün."
    elif vpd < 0.7:
        return "Düşük", "VPD düşük → yüksek nem ve düşük sıcaklık olabilir. Bu, meyvede çatlama ve mantar riskine yol açar. Havalandırmayı artırın ve sıcaklığı hafif yükseltin."
    else:
        return "Yüksek", "VPD yüksek → düşük nem veya yüksek sıcaklık. Bu, solgunluk ve küçük meyve oluşumuna neden olabilir. Ortam nemini artırın (sisleme), sıcaklığı 1-2°C düşürün."

# Bitki seçimi
plant = st.selectbox("Bitki Seçin", ["Marul", "Domates", "Salatalık", "Çilek"])

# Giriş alanları
rh = st.number_input("Bağıl Nem (%RH)", min_value=10.0, max_value=100.0, value=60.0, step=1.0)
temp = st.number_input("Sıcaklık (°C)", min_value=0.0, max_value=50.0, value=20.0, step=1.0)

# Hesaplama
if st.button("Hesapla"):
    vpd = calculate_vpd(temp, rh)

    # Bitkiye göre yorum
    if plant == "Marul":
        evaluation, suggestion = evaluate_vpd_for_lettuce(vpd)
    elif plant == "Domates":
        evaluation, suggestion = evaluate_vpd_for_tomato(vpd)
    elif plant == "Salatalık":
        evaluation, suggestion = evaluate_vpd_for_cucumber(vpd)
    elif plant == "Çilek":
        evaluation, suggestion = evaluate_vpd_for_strawberry(vpd)

    st.success(f"**Hesaplanan VPD:** {vpd} kPa")
    st.info(f"**Değerlendirme:** {evaluation}")
    st.write(f"📌 **Çözüm Önerisi:** {suggestion}")

# Not
st.markdown("---")
st.write("🔎 **Not:** VPD hesaplamaları Tetens formülüne dayalıdır. Daha hassas sonuçlar için yaprak sıcaklığı bilgisiyle birlikte hesaplama yapılması önerilir.")

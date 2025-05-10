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

# Değerlendirme fonksiyonları (neden-sonuç açıklamalarıyla)

def evaluate_vpd_for_lettuce(vpd):
    if 0.6 <= vpd <= 1.0:
        return "İdeal (Yeşil Bölge)", "VPD değeri ideal seviyede. Bu koşullar, marulda sağlıklı gelişim ve kalsiyum alımını destekler."
    elif 0.4 <= vpd < 0.6:
        return "Alt Sınır (Dikkatli İzleyin)", "VPD biraz düşük. Bu durum, marul yapraklarında uç yanığı (tipburn) riskini artırır. Havalandırmayı artırarak nemi düşürün ve kalsiyum nitrat (100-150 ppm) takviyesi yapın."
    elif 1.0 < vpd <= 1.2:
        return "Üst Sınır (Kabul Edilebilir)", "VPD hafif yüksek. Bitkiler biraz stres hissedebilir. Su kaybını azaltmak için nemlendirme (sisleme) uygulayın ve hava sirkülasyonunu kontrol edin."
    elif vpd < 0.4:
        return "Çok Düşük", "VPD çok düşük. Transpirasyon azalır, bu da bitki yüzeyinde mantar oluşumuna zemin hazırlar. Havalandırmayı artırarak nem seviyesini düşürmelisiniz."
    else:
        return "Çok Yüksek", "VPD çok yüksek. Bu durum, bitkide su stresine ve gelişim geriliğine yol açar. Seraya nemlendirici ekleyerek nemi artırın, sıcaklığı da 1-2°C düşürün."

def evaluate_vpd_for_tomato(vpd):
    if 0.8 <= vpd <= 1.2:
        return "İdeal", "VPD değeri domates için ideal. Bu seviyeler bitki büyümesini dengeler ve verimi artırır."
    elif vpd < 0.8:
        return "Düşük", "Düşük VPD, çiçek çürüklüğü ve mantar riskini artırır. Hava sirkülasyonunu artırarak nemi azaltın."
    else:
        return "Yüksek", "Yüksek VPD, aşırı su kaybına yol açar. Bu da çiçek dökümüne neden olabilir. Sisleme sistemi ile nemi artırın veya gölgeleme yaparak sıcaklığı azaltın."

def evaluate_vpd_for_cucumber(vpd):
    if 0.7 <= vpd <= 1.1:
        return "İdeal", "VPD değeri salatalık için ideal. Transpirasyon dengede, gelişim sağlıklı olur."
    elif vpd < 0.7:
        return "Düşük", "VPD düşükse yapraklarda su birikir, bu da mantar oluşumunu kolaylaştırır. Nem seviyesini düşürmek için havalandırmayı artırın."
    else:
        return "Yüksek", "Yüksek VPD yaprakların kurumasına neden olur. Sisleme sistemi ile nem sağlayın, gölgeleme ile sıcaklığı azaltın."

def evaluate_vpd_for_strawberry(vpd):
    if 0.7 <= vpd <= 1.1:
        return "İdeal", "VPD değeri çilek için uygundur. Bu ortamda meyve kalitesi artar ve yaprak sağlığı korunur."
    elif vpd < 0.7:
        return "Düşük", "Düşük VPD, hastalık riskini artırır ve meyvede çatlama olabilir. Nem seviyesini düşürmek için havalandırmayı ve sıcaklığı hafif artırabilirsiniz."
    else:
        return "Yüksek", "Yüksek VPD, çileklerde solgunluk ve küçük meyve oluşumuna neden olur. Sıcaklığı düşürerek veya nemlendirici kullanarak bu durumu dengeleyin."

# Bitki seçimi
plant = st.selectbox("Bitki Seçin", ["Marul", "Domates", "Salatalık", "Çilek"])

# Girişler
rh = st.number_input("Bağıl Nem (%RH)", min_value=10.0, max_value=100.0, value=60.0, step=1.0)
temp = st.number_input("Sıcaklık (°C)", min_value=0.0, max_value=50.0, value=20.0, step=1.0)

# Hesapla
if st.button("Hesapla"):
    vpd = calculate_vpd(temp, rh)

    # Değerlendirme
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
st.write("🔎 **Not:** VPD hesaplamaları, Tetens formülüne dayalıdır. Yaprak sıcaklığı verisiyle daha hassas ölçümler yapılabilir.")

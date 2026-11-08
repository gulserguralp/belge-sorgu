# Belge Sorgu Sistemi

**Canlı demo:** https://belge-sorgu-a92hvdpec6tuvtbp324xpu.streamlit.app/

> Uygulama bir süre kullanılmazsa uyku moduna geçer. Açılan sayfadaki uyandırma butonuna (Yes, get this app back up) basıp yaklaşık 30 saniye bekleyin.

Yüklediğiniz bir PDF belgesine doğal dilde soru sorup, cevabı yalnızca belgenin içeriğine dayalı olarak alabileceğiniz bir yapay zeka uygulaması. Sistem, cevabı belgenin hangi bölümünden ürettiğini de gösterir.

## Ne İşe Yarar?

Uzun bir belgeyi baştan sona okumak yerine, doğrudan sorunuzu sorarsınız. Örneğin uzun bir iş sözleşmesinde "hangi durumlarda işten çıkarılabilirim?" diye sorduğunuzda, sistem ilgili bölümü bulup size kaynağıyla birlikte cevap verir.

## Nasıl Çalışır?

1. Yüklenen PDF cümlelere göre parçalara ayrılır
2. Her parça, anlamını temsil eden bir sayı dizisine (embedding) çevrilir
3. Kullanıcının sorusu da aynı şekilde sayıya çevrilir
4. Soruya anlamca en yakın parçalar bulunur
5. Bu parçalar yapay zekaya verilir ve yalnızca belgeye dayalı bir cevap üretilir
6. Cevabın hangi parçalardan üretildiği kullanıcıya gösterilir

## Kullanılan Teknolojiler

- **Python** — ana programlama dili
- **Streamlit** — web arayüzü
- **sentence-transformers** — metinleri embedding'e çevirme (çok dilli model)
- **Anthropic Claude API** — cevap üretme
- **pypdf** — PDF okuma

## Kurulum ve Çalıştırma

1. Depoyu klonlayın:

       git clone https://github.com/gulserguralp/belge-sorgu.git
       cd belge-sorgu

2. Sanal ortam oluşturup etkinleştirin:

       python3 -m venv venv
       source venv/bin/activate

3. Gerekli kütüphaneleri kurun:

       pip install -r requirements.txt

4. Proje kök dizininde `.env` dosyası oluşturup Anthropic API anahtarınızı ekleyin:

       ANTHROPIC_API_KEY=sizin-anahtariniz

5. Uygulamayı çalıştırın:

       streamlit run app.py
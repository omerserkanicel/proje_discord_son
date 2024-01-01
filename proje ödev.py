import discord
from discord.ext import commands
import sounddevice as sd
import wave
import speech_recognition as sr
import webbrowser 
import pyautogui
from PIL import Image


intents = discord.Intents.default()

# Mesajları okuma ayrıcalığını etkinleştirelim

intents.message_content = True

# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım


# Discord botunu oluşturun
client = commands.Bot(intents=intents,command_prefix="/")

recognizer = sr.Recognizer()


@client.command(name='karbon_ayak_izi_hesapla', help='Karbon ayak izinizi hesaplar.')
async def karbon_ayak_izi_hesapla(ctx):
    await ctx.send(f'{ctx.author.mention}, karbon ayak izi hesaplamak için bazı sorulara cevap vermenizi istiyorum.')

    questions = [
        '1. Yılda kaç kilometre araç kullanıyorsunuz?',
        '2. Yılda kaç kez uçakla seyahat ediyorsunuz?',
        '3. Günlük su tüketiminiz nedir? (litre)',
        '4. Kaç saat bilgisayar başında çalışıyorsunuz?',
        '5. Geri dönüşüm yapıyor musunuz? (evet/hayır)',
    ]

    answers = []

    for question in questions:
        await ctx.send(question)
        response = await client.wait_for('message', check=lambda m: m.author == ctx.author)
        answers.append(response.content)

    # Hesaplama
    try:
        car_distance = float(answers[0])
        plane_trips = float(answers[1])
        daily_water_consumption = float(answers[2])
        computer_hours = float(answers[3])
        recycle = answers[4].lower() == 'evet'

        carbon_footprint = car_distance * 0.2 + plane_trips * 1.5 + daily_water_consumption * 0.1 + computer_hours * 0.05
        if recycle:
            carbon_footprint *= 0.8  # Geri dönüşüm yapanlar için indirim

        await ctx.send(f'{ctx.author.mention}, karbon ayak iziniz yaklaşık olarak {carbon_footprint:.2f} kgCO2.')
    except ValueError:
        await ctx.send(f'{ctx.author.mention}, lütfen sayısal değerler girin.')

@client.command(name='dinle', help='Mikrofonu dinle ve komutları algıla')
async def dinle(ctx, *args):
    await ctx.send('Dinleme başladı... Lütfen bir şeyler söyleyin.')

    try:
        # Ses kaynağını belirtin (örneğin, mikrofon veya ses dosyası)
        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        # Ses dosyasını metne çevirin
        text = recognizer.recognize_google(audio, language="tr-TR")
        print("Söylenen metin: {}".format(text))
        
        
        if text == "Alfa Romeo":
                await ctx.send('Yakıt Tüketim Bilgileri Geliyor...')
                image = Image.open("sonuclar/alfa.jpg")
                
                with open("sonuclar/alfa.jpg", 'rb') as file:
                    file = discord.File(file, filename="image.jpg")
                    await ctx.send(file=file)               
                    await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 54 lt. Şehir İçi Tüketim (100 km) 7.1 lt. Şehir Dışı Tüketim (100 km) 4.7 lt. Şehir İçi Tüketim (100 km) 4.9 lt. Şehir Dışı Tüketim (100 km) 3.3 lt. Karma Tüketim (100 km) 3.9 lt.")
                    await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    await ctx.send("Kuruluşu 1910 yılında olan Alfa Romeo, Anonima Lombarda Fabbrica Automobili (A.L.F.A) ismiyle Milano‘da kuruldu.24 HP gücünde üretilen ilk araçtan 5 yıl sonra şirketi Nicola Romeo satın aldı ve markanın ismi ALFA ROMEO adını almış oldu. Bugün STELLANTİS otomotiv grubunde yer alan marka, kendine has karakteristik yapısı ile özel bir kullanıcı kitlesi tarafından tercih ediliyor. Ülkemizde Alfa Romeo kullanıcıları ve hayranları kendilerine “Alfisti” ismini veriyor. Genellikle Sportif yapılı ve sürüş zevki yüksek konseptler üzerine yoğunlaşan marka son dönemde SUV modelleri ile kendini göstermeye devam ediyor. Yüksek kaliteli malzemeleri, sürüş odaklı tasarım detayları ile kendine has bir yapısı olan modellerin satışı ülkemizde Koç Holding bünyesinde yapılmaktadır. Alfa Romeo modelleri ise, Tonale, Stelvio, Giulia, Stelvio Quadrifoglio, Giulia Quadrifoglio")
        elif text == "Aston Martin":
                await ctx.send('Yakıt Tüketim Bilgileri Geliyor...')
                image = Image.open("sonuclar/aston.jpg")
                
                with open("sonuclar/aston.jpg", 'rb') as file:
                    file = discord.File(file, filename="image.jpg")
                    await ctx.send(file=file)               
                    await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 54 lt. Şehir İçi Tüketim (100 km) 7.1 lt. Şehir Dışı Tüketim (100 km) 4.7 lt. Şehir İçi Tüketim (100 km) 21.6 lt. Şehir Dışı Tüketim (100 km) 10.0 lt. Karma Tüketim (100 km) 14.3 lt.")
                    await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    await ctx.send("İngiliz otomobil markası Aston Martin, lüks segment otomobil üreten bir markadır. Temelleri 1913 yılına kadar uzanan marka, el işçiliği ile araç üretiyor. Plastik malzemelerin oldukça az kullanılmaya özen gösterildiği araçta pek çok detay alüminyum kullanılarak üretiliyor.")
            
        elif text == "Audi":
            await ctx.send('Yakıt Tüketim Bilgileri Geliyor...')
            image = Image.open("sonuclar/audi.jpeg")                    
            with open("sonuclar/audi.jpeg", 'rb') as file:
                file = discord.File(file, filename="image.jpg")
                await ctx.send(file=file)               
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 54 lt. Şehir İçi Tüketim (100 km) 7.1 lt. Şehir Dışı Tüketim (100 km) 4.7 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Alman kökenli Otomobil Markası AUDİ “Teknoloji ile Bir Adım Önde” mottosu ile tarihi 1899 yılına kadar uzanan bir yolculuğu ifade ediyor. Bugün küresel anlamda otomotiv sektörünü domine edici etkisi ile Almanya’nın en sevilen markalarından biri olarak karşımıza çıkan marka, Volkswagen otomotiv grubu içinde yer alıyor. Premium otomobil modelleri ile ön plana çıkan marka, son dönemde otomobillerinde geliştirdiği elektrifikasyon ile dikkat çekmeye devam ediyor. Sportif modelleri de bünyesinde barındıran marka “RS” isimli versiyonlar ile dinamizmi ön plana çıkartmayı başarıyor.")
        elif text == "Bentley":
            await ctx.send('Yakıt Tüketim Bilgileri Geliyor...')
            image = Image.open("sonuclar/bentley.jpg")                    
            with open("sonuclar/bentley.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg")
                await ctx.send(file=file)               
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Şehir İçi Tüketim (100 km) 21.7 lt. Şehir Dışı Tüketim (100 km) 9.6 lt. Karma Tüketim (100 km) 14.1 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Dünyanın en premium araçlarını üreten markaların başında gelen Bentley, 1919 yılında İngiltere’de kurulmuştur. Tamamen el işçiliği ile üretilen araçlar özel yapımdır. Kullanıcı isteğine göre siparişle üretilen araç pek çok farklı kişiselleştirme imkanı ile kullanıcısının isteklerine göre üretiliyor. Dünyanın en pahalı otomobillerinden olan Bentley modelleri, son dönemde ürettiği SUV modelleri ile dikkat çekmeye devam ediyor.")
        elif text == "BMW":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/bmw.jpg") 
            with open("sonuclar/bmw.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Şehir İçi Tüketim (100 km) 7.7 lt. Şehir Dışı Tüketim (100 km) 5.6 lt. Karma Tüketim (100 km) 6.4 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Premium otomobil denildiği zaman akla ilk gelen bir kaç markadan birisi olan BMW, tarihi 1916 yılına dayanan uzun bir serüven ile bugünlere gelmiş bir Alman otomobil markasıdır. İsmini kurulduğu yer olan Bavyera’ dan alan marka dünyanın en çok tutulan otomobil markalarından birisidir. Özellikle “lüks” algısını kullanıcılarına deneyimlendirmek üzere odaklanan marka, sportif sürüş karakterli “M” modelleri ile de oldukça dikkat çekmektedir. Uçak motoru üreticisi olarak kurulan marka, bugün otomobil ve motosiklet üretimi ile yolculuğuna devam etmektedir. Pek çok yeni teknolojiyi geliştirmek ile beraber elektrikli otomobiller konusunda öncü markalardan biri olmaya adaydır.")    
        elif text == "Bugatti":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/bugatti.jpg") 
            with open("sonuclar/bugatti.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt deposu hacmi 100 litre. Üretici verilerine göre, şehir içi yakıt tüketimi 0.0 lt/100km, Şehir dışı yakıt tüketimi 0.0 lt/100km")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1909 yılında kurulan marka, performans odaklı otomobiller üretiyor. El işçiliği ile özel olarak üretilen otomobiller dünyanın en hızlı otomobillerin başında geliyor. Almanya’da üretilen otomobiller genellikle 2 kişilik yarış arabaları tasarımı ile üretiliyor. Bununla beraber üst sınıf kaliteli malzeme ile üretilen araçlar oldukça lüks yapıya sahip.")    
        elif text == "Boeing":     
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/buick.jpg") 
            with open("sonuclar/buick.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Şehir içi yakıt tüketimi: 7.3 Litre Yakıt Tüketir 100 Kilometrede. · Şehir dışı yakıt tüketimi: 11.9 Litre Yakıt Tüketir")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Amerika üretimi olan Buick, tarihi 1899 yılına kadar giden bir otomobil markasıdır. Markanın ana pazarı Çin’dir. General motor bünyesinde olan marka 1950’li yıllardan sonra büyük ve geniş modelleri ile ilgi çekmiştir. Bugün nostaljik olarak büyük bir hayran kitlesi olan markanın, konforlu otomobilleri ile dikkat çekmektedir.")    
        elif text == "Cadillac":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/cadillac.jpg") 
            with open("sonuclar/cadillac.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt deposu hacmi 73 litre. Araçta Start & Stop özelliği bulunuyor. Üretici verilerine göre, şehir içi yakıt tüketimi 13.0 lt/100km, Şehir dışı yakıt tüketimi.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1902 yılında kurulan Cadillac, Amerikan menşeili bir marka olarak doğduğu yer olan bölgede oldukça popüler bir markadır. Lüks otomobil markası, General motor bünyesinde bulunmaktadır. Bugün elektrikli araçlar ve özellikle SUV sınıfı araçlarda popülerlik sağlayan marka, güçlü bir imaja sahiptir.")    
        elif text == "Chery":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/chery.jpg") 
            with open("sonuclar/chery.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.1.6 TGDI motor 183HP güç / 275Nm tork üretirken, otomobil 0-100km/sa hızlanmasını 9.2sn'de tamamlar ve 8.6L/100km ortalama yakıt tüketimine sakiptir.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Çin merkezli bir otomobil markası olan Chery, ülkemizde satış da olan bir firmadır. Türkiye’de Mermerler Oto distribütörlüğünde satılan otomobiller, 1997 yılında kurulmuştur. Yeni modelleri ile ülkemizde satış da olmaya devam edecektir. SUV ve binek modelleri ile uygun fiyatlı bir politika izlemektedir.")    
        elif text == "Chevrolet":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/chevrolet.jpg") 
            with open("sonuclar/chevrolet.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Otomobil 0'dan 100 km/s hıza 12.8 saniyede ulaşıyor ve 185 km/s (115 mph) maksimum hıza sahip. Araç Euro 5 emisyon standardına sahip.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Chevy veya Chevrolet Division of General Motors Company, 1911'de kurulmuş olan ABD merkezli bir otomobil şirketidir. Adını Kurucusu Louis Chevrolet'in soyadından almaktadır. 1918'de %54.6'sını satın alan General Motors bünyesine geçmiştir.")    
        elif text == "Chrysler":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/chrysler.jpeg") 
            with open("sonuclar/chrysler.jpeg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.şehir içerisinde 19.5 Litre yakıyor, şehir dışarında ise 8.2 Litre yakıyor.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1925 yılında kurulan marka, 1930 yılında Dodge markasına satılmıştır. Bugün Stellantis otomotiv gurubunda yer alan marka premium sınıf otomobiller üretmektedir.")    
        elif text =="Cupra":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/cupra.jpg") 
            with open("sonuclar/cupra.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.şehir içi ve şehir dışı karma 5.6 litredir.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Seat markasına bağlı olarak bir versiyon olarak serüvenine başlayan Cupra, bugün bağımsız bir otomobil markası olarak otomobil üretmeye devam ediyor. Seat markasının daha sportif bir versiyonu olarak yüksek performans sunan modeller ile satılmaya başlanan Cupra, bugün 3 farklı model ile ülkemizde satılıyor. Formentor, Leon ve Ateca modellerini ülkemizde satan marka Doğuş grubu bünyesinde satılıyor. Motor şanzıman ünitelerini SEAT markasından yani dolayısıyla Alman üretici Volkswagen grubundan alan CUPRA, tasarım detayları ile sportif modeller üretmektedir.")    

        elif text == "Dacia":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/dacia.jpeg") 
            with open("sonuclar/dacia.jpeg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt Kapasitesi 50 lt. Şehir İçi Tüketim (100 km) 5.3 lt. Şehir Dışı Tüketim (100 km) 4.0 lt. Karma Tüketim (100 km) 4.4 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Romanya‘da kurulan Dacia “Ulaşılabilir Otomobil” mottosu ile uygun fiyatlı ve aynı zamanda kaliteli otomobiller üretmek üzere yaşamına başlamış bir markadır. Dacia 1999 yılında Renault markası bünyesine girmiştir. Ülkemizde uygun fiyatlı otomobil satın almak isteyen kullanıcılar tarafında ağırlıkta tercih edilen model, ülkemizde artan araç fiyatları neticesinde bu özelliğini kaybetmiştir. Yenilenen logosu ile tasarım anlamında daha ilgi çekici modeller ile ülkemizde satılan Dacia modelleri, ticari modelleri ile de ülkemizde tercih ediliyor.")    
            
        elif text == "Daewoo":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/daewoo.jpg") 
            with open("sonuclar/daewoo.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Şehir içi yakıt tüketimi: 5.5 Litre Yakıt Tüketir 100 Kilometrede. · Şehir dışı yakıt tüketimi: 6.9 Litre Yakıt Tüketir .")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Güney Koreli üretici Daewoo 1967 yılında kurulmuştur. Genellikle sedan modeller üreten marka 1999 yılında iflas etmiştir. General Motor tarafından satın alınan marka, GM Daewoo olarak yaşantısına devam etmektedir.")    


        elif text == "Daihatsu":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/daihatsu.jpg") 
            with open("sonuclar/daewoo.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Ynt: Daihatsu Terios 1.3 İle 1.5 Arasında Yakıt Harcaması Hk. Terios 1. nesil 1.3 motor, 86 hp, şehir içi 11 lt civarı bir tüketimi vardır, Terios 2. nesil ise 1.5 motor, 105 hp, şehir içi 10lt civarı bir tüketimi vardır.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1907 yılında kurulan Daihatsu, Japonya’da kurulmuştur. Genel merkez kararı ile 2012 yılından beri sıfır otomobil satışı Türkiye’de olmayan markanın, yedek parça ve servis desteği ülkemizde devam etmektedir. SUV, spor otomobil ve ticari araçlar üreten markanın ülkemizde özellikle SUV modelleri tercih edilmektedir.")    

        elif text == "Dodge":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/dodge.jpg") 
            with open("sonuclar/dodge.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.şehir içi kullanımda 13 l / 100 km, uzun yolda 8.7 l /100 km ve karma tüketimde 11.2 l /100 km yakıt tüketimine sahip.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Amerikan markası olan Dodge, 1914 yılında kurulmuştur. Ford Model T için parça üreten marka daha sonrasında küçük şehir otomobilleri üretmeye başlamıştır. Bugün Stellantis otomotiv grubunda yer alan marka, güçlü motorlu pick-up modelleri ve spor otomobiller üretmektedir. Döneminde üretilen yüksek hacimli otomobiller ile bugün nostaljik anlamda oldukça çok seveni vardır.")    
        elif text == "DC":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/ds.jpg") 
            with open("sonuclar/ds.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. 4 lt/100 km")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("DS Automobiles 2014 yılında bağımsız bir marka olmuştur. Citroen markasının ve dahası PSA grubu otomobil yapılanmasının “premium” otomobil üreten versiyonu olarak ortaya çıkmıştır. Fransız kökenli marka, Citroen yetkili satıcılarında satılırken pek çok yerde kendi showroomlarında satılmaya devam etmektedir. DS markası bugün için Stellantis otomotiv grubu içinde yer almaktadır.")    

        elif text == "Ferrari":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/Ferrari.jpg") 
            with open("sonuclar/Ferrari.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt Kapasitesi 92 lt. Şehir İçi Tüketim (100 km) 22.9 lt. Şehir Dışı Tüketim (100 km) 10.4 lt. Karma Tüketim (100 km) 15.0 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("İtalya’nın Modena şehrinde kurulan Ferrari, otomotiv endüstrisi içinde önemli bir yere sahiptir. Tarihi boyunca supersport yarış araçları üreten marka, hız tutkunları için tercih edilen bir markadır. Markanın yaratıcısı Enzo Ferrari tarihi açısından oldukça önemlidir.")    

        elif text == "Fiat":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/Fiat.jpg") 
            with open("sonuclar/Fiat.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt Tüketimi ; 5.5 lt/100km, Şehir içi, Yavaş (0 - 40 km/s) ; 4.1 lt/100km, Şehir Dışı, Orta (40 - 80 km/s) ; 5.9 lt/100km.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1899 yılında ilk olarak temelleri Torino’da atılan Fiat, ismini kurulduğu bölgeden almıştır. (Fabbrica Italiana Automobili Torino) Bünyesinde Lancia, Alfa Romeo, Maserati, Chrysler, Dodge, Jeep, Yamaha Motor Company, Iveco, Ferrari gibi markaları barındırmaktadır. Son dönemde Fiat ve bünyesindeki markalarda yeni bir oluşum içine girmiştir ve Stellantis otomotiv grubu bünyesine katılmıştır.")    


        elif text == "Ford":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/Ford.jpg") 
            with open("sonuclar/Ford.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Şehir İçi Tüketim (100 km) 5.7 lt. Şehir Dışı Tüketim (100 km) 3.7 lt. Karma Tüketim (100 km) 4.5 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1903 yılında kurulan Ford Motor Company, Henry Ford tarafından kurulmuş ve ismini almıştır. Amerikan markası olan Ford, Avrupa’dada üretim yapmaktadır. Aynı zamanda Koç holding bünyesinde 1950’li yıllardan beri ülkemizde de üretim yapılmaktadır. Ford Otosan adıyla kurulan Koç Holding şirketi, bugün tüm dünyaya özellikle ticari araç özelinde ihracat yapmaktadır.")    

        elif text == "Geely":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\geely.jpg") 
            with open("sonuclar\geely.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. 7,25 L/100 km")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1986 yılında Çin’de kurulan Geely, otomobil, motosiklet, motor ve şanzıman üretimi yapan şirket, ülkemizde sedan otomobil modelleri ile satıştadır. Apple ile anlaşma yaparak gücüne güç katan marka, Apple Car Play’i araçlarında ilk kullanan markadır. Bununla beraber Volvo markasını da 2010 yılında Ford’dan satın almıştır.")    

        elif text == "Honda":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar/Honda.jpg") 
            with open("sonuclar/Honda.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. 7,25 L/100 km")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Japon otomobili denildiği zaman akla ilk gelen markaların başında gelen Honda, 1948 yılında Tokyo/Japonya‘da kurulmuştur. Sağlamlık ve uzun ömürlülük konusunda ün yapan marka, konforlu otomobiller ile beraber sportif kullanıma uygun versiyonlu araçlar ile ciddi bir hayran kitlesine sahiptir.")    

        elif text == "Hyundai":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\hyundai.jpg") 
            with open("sonuclar\hyundai.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Şehir İçi Tüketim (100 km) 7.8 lt. Şehir Dışı Tüketim (100 km) 5.1 lt. Karma Tüketim (100 km) 6.1 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Güney Kore merkezli Hyundai, Gemi ve iş makinası üretimi gibi pek çok farklı alanda üretim yapan bir şirkettir. 1967 yılında Seul, Güney Kore’de kurulmuştur. Türkçe karşılığı çağdaş ve modern anlamına gelen Hyundai, Kia ile kardeş şirketlerdir. Elektrikli araçlar konusunda oldukça iddialı çalışmalar yapan marka, Accent modeli Hyundai için bir dönüm noktası olmuştur. Genesis isimli lüks segment otomobil üreten bir yan markası da vardır.")    


        elif text == "Infinity":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\infiniti.jpg") 
            with open("sonuclar\infiniti.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.  5.8 lt/100 km")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Nissan Motors’a bağlı lüks otomobil markası olan İnfiniti, ülkemizde özellikle SUV modelleri tercih edilen markanın pek çok dünya ülkesinde satışı mevcuttur.")    

        elif text == "Isuzu":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\ısuzu.jpg") 
            with open("sonuclar\ısuzu.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 76 lt. Şehir İçi Tüketim (100 km) 9.3 lt. Şehir Dışı Tüketim (100 km) 6.9 lt. Karma Tüketim (100 km) 7.8 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Japonya merkezli bir otomobil markası olan Isuzu özellikle motor dayanıklılığı ile meşhur bir markadır. Özellikle ticari araç grubunda araç üretimi yapan markanın, D-Max isimli Pick-Up modeli oldukça popülerdir. Toplu taşıma, turizm, kamyon ve kamyonet tarzında modelleri vardır.")    
        elif text == "Iveco":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\iveco.jpg") 
            with open("sonuclar\iveco.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.100 km de 16.5 litre yakıyor.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("İtalya merkezli ticari araç markası olan Iveco, dünya çapında ticari araç satışı yapmaktadır. Aynı zamanda dizel motor üretimi yapan marka, tır kamyon ve kamyonet satışı yapmaktır.")    


        elif text == "Jaguar":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\jaguar.jpg") 
            with open("sonuclar\jaguar.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt Kapasitesi 70 lt. Şehir İçi Tüketim (100 km) 11.6 lt. Şehir Dışı Tüketim (100 km) 6.1 lt. Karma Tüketim (100 km) 8.1 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("İngiltere merkezli otomobil markası olan Jaguar, tarihi 1922 yılına kadar gidiyor. Şuan ki sahibi Hindistanlı üretici Tata olan marka, premium sınıf araç üreten bir markadır. Lüks algısı yüksek modeller üreten Jaguar, sportif karakterli yüksek performans gücüne sahip otomobiller üretir.")    

        elif text == "jeep":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\Jeep.jpg") 
            with open("sonuclar\Jeep.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt Kapasitesi 48 lt. Şehir İçi Tüketim (100 km) 7.4 lt. Şehir Dışı Tüketim (100 km) 5.0 lt. Karma Tüketim (100 km) 5.9 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Askeri amaçlı araç ve motosiklet üretimi ile yaşamına başlayan Jeep 1940’lı yıllarda kurulmuştur. Sağlam, dayanıklı ve uzun ömürlü araçlar üretmek amacıyla tasarlanan Jeep modelleri bugün gelinen noktada, daha lüks ve konforlu araçlar üretmektedir. SUV sınıfında araçlar üreten marka, Stellantis otomobil grubunda yer almaktadır.")    

        elif text == "Kia":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\kia.jpg") 
            with open("sonuclar\kia.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt Kapasitesi 48 lt. Şehir İçi Tüketim (100 km) 7.4 lt. Şehir Dışı Tüketim (100 km) 5.0 lt. Karma Tüketim (100 km) 5.9 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Askeri amaçlı araç ve motosiklet üretimi ile yaşamına başlayan Jeep 1940’lı yıllarda kurulmuştur. Sağlam, dayanıklı ve uzun ömürlü araçlar üretmek amacıyla tasarlanan Jeep modelleri bugün gelinen noktada, daha lüks ve konforlu araçlar üretmektedir. SUV sınıfında araçlar üreten marka, Stellantis otomobil grubunda yer almaktadır.")    

        elif text == "Lada":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\lada.jpg") 
            with open("sonuclar\lada.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.4.76 litreyle o mesafeyi katetmiştir, dolayısıyla 100 km de 9,52 litre lpg yakıyor demektir.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Rusya merkezli bir marka olan Lada, geçmişten bugüne ikonik bir model haline gelen Niva modeli ile bilinmektedir. Sağlamlığı ile ön plana çıkan Niva modeli, uzunca bir dönem aynı tasarıma bağlı kalarak yolculuğuna devam etmektedir. 4×4 bir arazi aracı satın almak isteyen kullanıcıların uygun fiyatlı olması nedeniyle tercih ettiği model, son yıllarda bir yenilenme sürecine girmiştir. Lada markasının Vesta, Samara gibi binek araç modelleri de mevcuttur.")    

        elif text == "Lamborghini":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\lamborghini.jpg") 
            with open("sonuclar\lamborghini.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt Kapasitesi 90 lt. Şehir İçi Tüketim (100 km) 24.7 lt. Şehir Dışı Tüketim (100 km) 10.7 lt. Karma Tüketim (100 km) 16.0 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1963 yılında kurulan Lamborghini, supersport otomobil üreten bir İtalyan otomobil üreticisidir. Şuandaki sahibi Volkswagen grup olan marka üretim hayatına traktör üreterek başlamıştır. Dünyanın en pahalı ve lüks otomobil modellerini üretmek konusunda vizyon edinen marka, süper hızlı modeller üretmektedir.")    
        elif text == "Lancia":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\lancia.jpg") 
            with open("sonuclar\lancia.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.şehir içi yakıt tüketimi 5.9 lt/100km, Şehir dışı yakıt tüketimi 4.1 lt/100km ve ortalama olarak da 4.8 lt/100km yakıt tüketiyor")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1906 yılında kurulan Lancia, 1969 yılından beri Fiat markasının çatısı altındadır. Ülkemizde de bir dönem satışta olan marka şuan için satış yapmamakla beraber yedek parça ve servis konusunda işlemlerine devam etmektedir.")    
        elif text == "Land Rover":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\land.jpg") 
            with open("sonuclar\land.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 85 lt. Şehir İçi Tüketim (100 km) 8.5 lt. Şehir Dışı Tüketim (100 km) 7.0 lt. Karma Tüketim (100 km) 7.5 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("İngiliz otomobil üreticisi Land Rover, 2008 yılında Hindistanlı otomobil üreticisi Tata’ya satılmıştır. Premium sıfır SUV modelleri üreten marka, “lüks SUV” denildiği zaman ülkemizde ilk akla gelen markalardan birisidir. Kuruluşu ikinci dünya savaşı yıllarına dayanan marka ilk dönemlerde askeri yeteneği olan, sağlam ve arazi kabiliyeti yüksek modeller üretmiştir. Zaman içinde ikonik bir tarz yakalayan Defender modeli Land Rover modelleri içinde en bilinen araçlardandır.")    
        elif text == "Land Rover":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\land.jpg") 
            with open("sonuclar\land.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 85 lt. Şehir İçi Tüketim (100 km) 8.5 lt. Şehir Dışı Tüketim (100 km) 7.0 lt. Karma Tüketim (100 km) 7.5 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("İngiliz otomobil üreticisi Land Rover, 2008 yılında Hindistanlı otomobil üreticisi Tata’ya satılmıştır. Premium sıfır SUV modelleri üreten marka, “lüks SUV” denildiği zaman ülkemizde ilk akla gelen markalardan birisidir. Kuruluşu ikinci dünya savaşı yıllarına dayanan marka ilk dönemlerde askeri yeteneği olan, sağlam ve arazi kabiliyeti yüksek modeller üretmiştir. Zaman içinde ikonik bir tarz yakalayan Defender modeli Land Rover modelleri içinde en bilinen araçlardandır.")    
        elif text == "Land Rover":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\land.jpg") 
            with open("sonuclar\land.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 85 lt. Şehir İçi Tüketim (100 km) 8.5 lt. Şehir Dışı Tüketim (100 km) 7.0 lt. Karma Tüketim (100 km) 7.5 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("İngiliz otomobil üreticisi Land Rover, 2008 yılında Hindistanlı otomobil üreticisi Tata’ya satılmıştır. Premium sıfır SUV modelleri üreten marka, “lüks SUV” denildiği zaman ülkemizde ilk akla gelen markalardan birisidir. Kuruluşu ikinci dünya savaşı yıllarına dayanan marka ilk dönemlerde askeri yeteneği olan, sağlam ve arazi kabiliyeti yüksek modeller üretmiştir. Zaman içinde ikonik bir tarz yakalayan Defender modeli Land Rover modelleri içinde en bilinen araçlardandır.")    
        elif text == "Land Rover":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\land.jpg") 
            with open("sonuclar\land.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 85 lt. Şehir İçi Tüketim (100 km) 8.5 lt. Şehir Dışı Tüketim (100 km) 7.0 lt. Karma Tüketim (100 km) 7.5 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("İngiliz otomobil üreticisi Land Rover, 2008 yılında Hindistanlı otomobil üreticisi Tata’ya satılmıştır. Premium sıfır SUV modelleri üreten marka, “lüks SUV” denildiği zaman ülkemizde ilk akla gelen markalardan birisidir. Kuruluşu ikinci dünya savaşı yıllarına dayanan marka ilk dönemlerde askeri yeteneği olan, sağlam ve arazi kabiliyeti yüksek modeller üretmiştir. Zaman içinde ikonik bir tarz yakalayan Defender modeli Land Rover modelleri içinde en bilinen araçlardandır.")    
        elif text == "Lexus":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\lexus.jpg") 
            with open("sonuclar\lexus.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.  Aracın ortalama yakıt tüketimi ise 100 kilometrede 6.3-6.6 litre")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Japonya merkezli otomobil markası olan Toyota’nın lüks segment araç üreten markası olan Lexus, özellikle Ortadoğu ve Amerikan pazarında popüler bir markadır. Lüks sınıf sedan modelleri ile tanınmaktadır. Amerika’da “en sağlam otomobil” ödülünü uzunca zamandır elinde tutan model, Japon otomobili Toyota’nın sağlamlık imajını üstüne koyarak geliştirmektedir.")    
        elif text == "Lincoln":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\lincoln.jpg") 
            with open("sonuclar\lincoln.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.  Yakıt tüketimi - Şehir içi:18.1 L/100 km, Şehir dışı:13.1 L/100 km,  Ortalama: 15 L/100 km")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Amerika markası olan Lincoln, lüks sınıf araç üretimi yapmaktadır. Cadillac markası ile rekabet halinde olan marka, üretiminin neredeyse tamamını Amerikan pazarına ayırmaktadır. Ülkemizde satışta olmayan Lincoln büyük hacimli motorları nedeniyle de ülkemizde tercih edilemiyor.")    
        elif text == "Lotus":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\lotus.jpg") 
            with open("sonuclar\lotus.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.   Şehir içi: 8.3 L/100 km , Şehir dışı: 5 L/100 km,  Ortalama: 6.3 L/100 km")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1952 yılında Londra İngiltere’de kurulan otomobil markası Lotus, bugün elektrikli araç üretimi ile yeni modellerini piyasaya sürmektedir. 600 km menzil sunan elektrikli SUV modeli 0-100 km/h hızlanmasını 2.95 saniyede tamamlamaktadır. Ülkemizde satışta olmayan model, supersport modeller ve SUV araçlar üretmektedir.")    
        elif text == "Maserati":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\maserati.jpg") 
            with open("sonuclar\maserati.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.  Yakıt Kapasitesi 70 lt. Şehir İçi Tüketim (100 km) 7.6 lt. Şehir Dışı Tüketim (100 km) 5.0 lt. Karma Tüketim (100 km) 5.9 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("İtalyan otomobil markası Maserati, spor otomobil üreten bir markadır. 1914 yılında kurulan marka, 1993 yılında Ferrari ile birlikte Fiat tarafından satın alındı. Yüksek motor gücüne sahip dinamizmi yüksek modeller üreten markanın lüks algısı oldukça yüksektir.")    
        elif text == "Mazda":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\mazda.jpg") 
            with open("sonuclar\mazda.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.  Yakıt Kapasitesi 51 lt. Şehir İçi Tüketim (100 km) 6.8 lt. Şehir Dışı Tüketim (100 km) 4.8 lt. Karma Tüketim (100 km) 5.8 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1920 yılında Fuchū, Hiroshima Prefektörlüğü, Japonya'da kurulan çok uluslu Japon otomobil üreticisidir.")    
        elif text == "maclaren":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\mclaren.jpg") 
            with open("sonuclar\mclaren.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.  Şehir içi yakıt tüketimi 15.8 Lt/100 km Şehir dışı yakıt tüketimi 7.9 Lt/100 km")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Dünyaca ünlü supersport otomobil üreticisi Mclaren, İngiltere merkezli bir otomobil markasıdır. Dünyanın en hızlı modellerini üretmeye aday marka, yarış sporlarında vazgeçilmez bir marka haline gelmiştir.")    
        elif text == "Mercedes":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\mercedes.jpg") 
            with open("sonuclar\mercedes.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.   Yakıt deposu hacmi 50 litre. Üretici verilerine göre, şehir içi yakıt tüketimi 4.2 lt/100km, Şehir dışı yakıt tüketimi 3.4 lt/100km ve ortalama yakıt tüketimi 3.7 lt/100km olarak belirtilmiş.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Almanya’nın en ünlü otomobil markalarının başında gelen Mercedes-Benz tüm dünyada kabul görmüş lüks sınıf otomobiller üreten bir markadır. 1926 yılında kurulan marka içten yanmalı motorun temellerini atmakla beraber otomobil endüstrisine büyük katkıları olmuştur. Dünyanın en uzun yolculuğunu yapan, fren balatasını bulan önemli bir markadır. tarihsel katkısının yanında ticari araç sınıfında da Mercedes-Benz bir tercih olmuştur.")    
        elif text == "mg":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\mg.jpg") 
            with open("sonuclar\mg.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. şehir içi 7.0, şehir dışı 6.0 litre yakıt tüketim değerlerine sahip.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("İngiltere’de kurulan MG markasının tarihi 1924 yılına kadar uzanıyor. Bugün ülkemizde de satış da olan marka, elektrikli ve benzinli motor ünitelerine sahip SUV modelleri ile satılıyor.")    
        elif text == "Mini":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\mini.jpg") 
            with open("sonuclar\mini.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Şehir İçi Tüketim (100 km) 6.0 lt. Şehir Dışı Tüketim (100 km) 4.1 lt. Karma Tüketim (100 km) 4.8 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Kült bir yapısı olan Mini, küçük spor araçlar üreten bir otomobil markasıdır. 1960’lı yıllardan bu yana varlığını sürdüren Mini tarihi boyunca ikonik tasarım detaylarını korumuş ve bugün o günlerden izler taşıyan araçlar üreterek tasarım diline bağlı kalmıştır. İngiltere’de kurulan marka ilerleyen dönemlerde BMW çatısı altına girmiştir ve bugün hala BMW grubunun bir parçasıdır. Retro tasarım detaylarına sahip markanın binek otomobil sınıfında araçları vardır ve SUV modellerine ek olarak hatchback karoser seçeneğine sahip modelleri mevcuttur.")    
        elif text == "Mitsubishi":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\mitsu.jpg") 
            with open("sonuclar\mitsu.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 75 lt. Şehir İçi Tüketim (100 km) 7.5 lt. Şehir Dışı Tüketim (100 km) 5.6 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Türkiye’deki ortaklığını Temsa ile yapan Mitsubishi 1970 yılında Japonya’da kurulmuştur. Japon otomobil markası ürettiği otomobiller ile sağlamlık ve uzun ömürlülük konusunda ün kazanmayı başarmıştır. Binek, SUV ve Pick-Up modellerine ek olarak ticari araç sınıfında da oldukça tercih edilmiştir. Motor sporlarında yarış otomobilleri ile başarılı işler yapmayı başaran Mitsubishi, Nisan-Renault ortaklığına dahil olmuştur.")    
        elif text == "Nissan":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\issan.jpg") 
            with open("sonuclar\issan.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Şehir İçi Tüketim (100 km) 4.3 lt. Şehir Dışı Tüketim (100 km) 3.5 lt. Karma Tüketim (100 km) 3.8 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Japonya‘da kurulan Nissan, arazi araçları, yarış otomobilleri, binek ve pick-up gibi pek çok farklı segment ve karoserdeki modelleri ile sağlam ve dayanıklı modeller üretmiştir. 1910 yılına kadar uzanan tarihi boyunca yukarı ivmesini sürdürmeyi başaran Nissan, Renault ile uzun yıllardır süren ortaklığı devam etmektedir. Ortak motor-şanzıman kombinasyonlarını kullanan Nissan ve Renault özellikle dizel motor ünitesi olan “DCİ” motor ile oldukça popülarite yakalamıştır.")
        elif text == "Opel":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\opel.jpg") 
            with open("sonuclar\opel.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 75 lt. Şehir İçi Tüketim. 7,1 lt. Şehir Dışı Tüketim. 4,8 lt. Ortalama Tüketim. 5,6 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Alman otomobil markası Opel, 1917 yılındaki kuruluşundan 2017 yılına kadar Alman General Motors’un idi. 2017 yılında ise Stellantis otomobil grubuna dahil oldu. Binek, SUV ve ticari otomobiller üreten marka, pek çok ülkede satış da ve ciddi bir pazar payına sahip. İngiliz Vauxhall markası ise Opel’in kardeş markasıdır.")
        elif text == "Peugeot":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\pejo.jpg") 
            with open("sonuclar\pejo.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Şehir İçi Tüketim (100 km) 5.3 lt. Şehir Dışı Tüketim (100 km) 4.0 lt. Karma Tüketim (100 km) 4.5 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Fransız otomobil markası Peugeot, tarihi 1890 yılına kadar uzanmaktadır. Bugün Stellantis otomotiv grubunun içinde yer alan Peugeot uzun yıllardır içinde olduğu PSA grubunu bu şekilde güncellemiş oldu. Binek, SUV, hafif ticari gibi pek çok sınıfta araç üreten marka elektrikli otomobil üretimi konusunda ciddi yatırımlar yapmaya devam ediyor.")        
        elif text == "Porsche":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\porş.jpg") 
            with open("sonuclar\porş.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 85 lt. Şehir İçi Tüketim (100 km) 7.8 lt. Şehir Dışı Tüketim (100 km) 6.2 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Sportif araç deneyimi denildiği zaman ilk akla gelen markaların başında olan Alman otomobil markası Posche, 1931 yılında kurulmuştur. Bugün Volkswagen AG çatısında bulunan lüks otomobil markası, Ferdinand Porsche tarafından kurulmuş ve ismini de buradan almıştır. Bugüne gelindiği zaman yarış arabası konsepti yerini biraz daha lüks SUV modellerine bırakmıştır.")
        elif text == "Proton":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\proton.jpg") 
            with open("sonuclar\proton.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Şehir içi yakıt tüketimi. 11.1 Lt/100 km. Şehir dışı yakıt tüketimi. 6.9 Lt/100 km.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Sportif araç deneyimi denildiği zaman ilk akla gelen markaların başında olan Alman otomobil markası Posche, 1931 yılında kurulmuştur. Bugün Volkswagen AG çatısında bulunan lüks otomobil markası, Ferdinand Porsche tarafından kurulmuş ve ismini de buradan almıştır. Bugüne gelindiği zaman yarış arabası konsepti yerini biraz daha lüks SUV modellerine bırakmıştır.")
        elif text == "Renault":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\eno.jpg") 
            with open("sonuclar\eno.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Şehir içi yakıt tüketimi. 6,5 lt/100 km	 Şehir dışı yakıt tüketimi. 5,1 lt/100 km")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1898 yılında temelleri atılan Renault bugün geldiği noktada, tüm dünyada bilinen ve popülaritesi yüksek bir marka haline gelmiştir. Pek çok alanda üretim yapan marka, ülkemizde binek ve ticari grupta satışlar yapmaktadır. Fransız otomobil markası olan Renault, Nissan ile bir ortaklığı bulunmaktadır. Bu birleşime Mitsubishi markası da katılmıştır.")
        elif text == "Rolls Royce":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\oys.jpg") 
            with open("sonuclar\oys.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 100 lt. Şehir İçi Tüketim (100 km) 22.8 lt. Şehir Dışı Tüketim (100 km) 10.2 lt. Karma Tüketim (100 km) 14.8 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Lüks otomobil üreticisi Rolls Royce, İngiltere’de kurulmuştur. Oldukça pahalı otomobiller üreten marka, tamamen lüks ve konfor algısı üzerine tasarımlar yapmaktadır. Prestij algısı yüksek otomobiller üreten marka ülkemizde satılmaktadır.")
        elif text == "Rover":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\over.jpg") 
            with open("sonuclar\over.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt Kapasitesi 85 lt. Şehir İçi Tüketim (100 km) 8.5 lt. Şehir Dışı Tüketim (100 km) 7.0 lt. Karma Tüketim (100 km) 7.5 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("İngiliz otomobil markası Rover, 1968 yılında kurulmuştur. Bir dönem ülkemizde oldukça popüler olan marka, şuan ülkemizde satış yapmamaktadır.")
       
        elif text == "Seat":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\seat.jpg") 
            with open("sonuclar\seat.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 50 lt. Şehir İçi Tüketim (100 km) 6.1 lt. Şehir Dışı Tüketim (100 km) 4.2 lt. Karma Tüketim (100 km) 4.9 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("İspanya merkezli bir otomobil markası olan Seat, bugün Volkswagen AG grubu içinde yer almaktadır. Sportif sürüş odaklı tasarımlar ve motor kombinasyonları kullanan marka, 1950 yılında kurulmuştur. Genç kullanıcı kitlesini hedef alan Seat, dinamizmi ön planda tutan tasarımlara imza atmıştır. Volkswagen grubunun altyapısı ile üretilen modeller, ortak motor-şanzıman kombinasyonlarını kullanmaktadır.")
        elif text == "Skoda":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\skoda.jpg") 
            with open("sonuclar\skoda.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Şehir İçi Tüketim (100 km) 5.1 lt. Şehir Dışı Tüketim (100 km) 3.8 lt. Karma Tüketim (100 km) 4.3 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Çek Cumhuriyeti merkezli bir otomobil markası olan Skoda, “Simply Clever” mottosu ile hayatı kolaylaştıracak çözümleri araçlarına entegre etmeye çalışıyor. Kullanıcı dostu detaylar ile akılcı çözümler sunan Skoda, Volkswagen AG otomotiv grubu içinde yer almaktadır. 1895 yılında kurulan marka 1991 yılında Volkswagen grubuna katılmıştır.")
        elif text == "Skyfall":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\skywell.jpg") 
            with open("sonuclar\skywell.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Batarya kapasitesi 72 kWh Yakıt tüketimi	15,6 kWh / 100 km")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Güzel gökyüzü anlamına gelen Skywell, Çin menşeili bir otomobil üreticisidir. 2000’li yıllarda kurulan şirket teknolojik ürünler üreten bir firma iken bugün otomobil üretimi ile pek çok ülkede yüksek satış rakamlarına ulaşmaya başlamıştır. Günümüzde ABD, Meksika, Kanada, Güney Amerika, Avusturya, Almanya, Romanya, Filistin, İsrail, Ürdün ve Türkiye gibi birçok ülkede satılmaktadır. Ülkemizde satışta olan model ET5 isimli tamamen elektrikli araç satışı yapmaktadır.")
        elif text == "Smart":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\smart.jpg") 
            with open("sonuclar\smart.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Şehir içi (100 km'de)	6,1 lt, Şehir dışı (100 km'de)4 lt, Ortalama (100 km'de) 4,7 lt ")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("1994 yılında Mercedes-Benz ve Swatch tarafından kurulan marka, küçük şehir otomobilleri üretmektedir. Son dönemde elektrikli modelleri ile gündeme gelen Smart, ikonik bir tasarım yapısına sahiptir. Bugün hala Mercedes-Benz bünyesinde üretilmektedir.")
        elif text == "Subaru":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\subaru.jpg") 
            with open("sonuclar\subaru.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt Kapasitesi 60 lt. Şehir İçi Tüketim (100 km) 7.9 lt. Şehir Dışı Tüketim (100 km) 5.5 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Japonya markası olan Subaru, 1953 yılında kurulmuştur. Özellikle yarış otomobilleri üreten marka, bugüne gelindiği zaman elektrikli SUV modellerine ağırlık vermiştir. Lüks segment araç tasarımları konusunda dikkat çekici modeller üreten marka, Japon otomobil severler tarafından oldukça sevilmektedir.")
        elif text == "Suzuki":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\suzuki.jpg") 
            with open("sonuclar\suzuki.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt Kapasitesi 60 lt. Şehir İçi Tüketim (100 km) 4,6 lt.  Şehir Dışı Tüketim (100 km) 3,9 lt. Ortalama (100 km'de) 4,1 lt")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Japon otomobil üreticisi Suzuki, tarihi 1909 yılına kadar uzanan bir otomobil markasıdır. Aynı zamanda tanınan bir motosiklet üreticisi olan marka, Hibrit otomobiller üreterek günün teknolojisini yakalamıştır. ‘Way of Life!’ mottosu ile kullanıcılarına akılcı çözümler sunan marka, pek çok ülkeye otomobil ihraç etmektedir.")
        elif text == "Tata":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\stata.jpg") 
            with open("sonuclar\stata.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Yakıt Kapasitesi 60 lt. Şehir İçi Tüketim (100 km) 8 Lt.  Şehir Dışı Tüketim (100 km) 4.8 Lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Hindistan merkezli otomobil markası olan Tata 1868 yılında kurulmuştur. Merkezi Mumbai’de olan marka pek çok farklı sektörde faaliyet gösteren bir şirkettir. Türkiye’deki disbiritörlüğünü İsotlar grubun yaptığı Tata, bugün yeni bir model satışı sunmamaktadır.")
        elif text == "Tesla":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\stesla.jpg") 
            with open("sonuclar\stesla.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Düz bir yolda 100 kilometrede ortalama 	15,7 kWh, uzun menzilli batarya ise 16,9 kWh değerinde elektrik tüketir")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Yerli ve Milli gururumuz Togg T10X akıllı cihazı ")   
        
        elif text == "togg":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\stogg.jpg") 
            with open("sonuclar\stogg.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Düz bir yolda 100 kilometrede ortalama 16,7 kWh, uzun menzilli batarya ise 16,9 kWh değerinde elektrik tüketir")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Türkiye'nin Otomobili Girişim Grubu veya kısaca Togg, Türkiye merkezli bir otomobil üretici şirkettir. Şirket, fikrî mülkiyet haklarına sahip olduğu ilk otomobilini 29 Ekim 2022 seri üretime hazır hâle geldi.")
        elif text == "Toyota":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\stoyota.jpg") 
            with open("sonuclar\stoyota.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Şehir İçi Tüketim (100 km) 7.6 lt. Şehir Dışı Tüketim (100 km) 4.8 lt. Karma Tüketim (100 km) 5.8 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Japon otomobil üreticisi Toyota, küresel anlamda en çok otomobil satan markaların başında geliyor. Pek çok farklı segmentte araç üreten Toyota, elektrikli otomobil üretimi konusunda büyük yol almış bir markadır.")
        elif text == "Volkswagen":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\os.jpg") 
            with open("sonuclar\os.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Şehir İçi Tüketim (100 km) 7.6 lt. Şehir Dışı Tüketim (100 km) 4.8 lt. Karma Tüketim (100 km) 5.8 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Japon otomobil üreticisi Toyota, küresel anlamda en çok otomobil satan markaların başında geliyor. Pek çok farklı segmentte araç üreten Toyota, elektrikli otomobil üretimi konusunda büyük yol almış bir markadır.")
        elif text == "Volvo":
            await ctx.send("Yakıt Tüketim Bilgileri Geliyor...")
            image = Image.open("sonuclar\olvo.jpg") 
            with open("sonuclar\olvo.jpg", 'rb') as file:
                file = discord.File(file, filename="image.jpg") 
                await ctx.send(file=file)   
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır.Şehir İçi Tüketim (100 km) 7.6 lt. Şehir Dışı Tüketim (100 km) 4.8 lt. Karma Tüketim (100 km) 5.8 lt.")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                await ctx.send("Japon otomobil üreticisi Toyota, küresel anlamda en çok otomobil satan markaların başında geliyor. Pek çok farklı segmentte araç üreten Toyota, elektrikli otomobil üretimi konusunda büyük yol almış bir markadır.")

    
        await ctx.send(f'Söyledikleriniz kaydedildi: "{text}"')

        # Dinleme sonrasında otomatik olarak karbon_ayak_izi_hesapla fonksiyonunu çağır
        await karbon_ayak_izi_hesapla(ctx)

    except sr.UnknownValueError:
        await ctx.send('Anlaşılamadı. Lütfen tekrar deneyin.')

client.run("MTE3NTQwNjE3MzI5MDIzODAwMg.GSHMTZ.mgIVZYeC9V1FQQGTuB2J-tJEXjrgdgSXz2lhNQ")  # TOKEN yerine botunuzun gerçek token'ını ekleyin
    

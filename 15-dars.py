# 14-dars lug`at bilan tabishuv

# car_0 = {'model': 'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])
#
# en_uz = {'apple':'olma','pear':'shaftoli','apricot':'o`rik'}
# print(en_uz)
#
# mevalar = {'olma':10000,'tarvuz':12000,'qovun':14000}
# print(mevalar['olma'])

# talaba = {'ism':'firdavs','yosh':17,'t_yil':2004}
# print(f"{talaba['ism'].title()},\
#          {talaba['yosh']}-yoshda,\
#          {talaba['t_yil']}-yilda tug`ilgan)")
# del talaba['yosh']
# print(talaba)
# talaba['kurs'] = 11
# talaba['fakultet'] = 'iqtisod'
# print(talaba)
# talaba['ism']  = 'behruz'
# print(talaba)

# talaba_1 = {}
# talaba_1['ism'] = 'firdavs choriyorov'
# talaba_1['sinf'] = 11
# talaba_1['yosh'] = 17
# print(talaba_1)
#
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'samsung S9',
#     'anvar': 'j2'
# }
# phh = telefonlar.get('hasan',)
#
# print(phh)

# otam = {
#     'ism':'ilhom',
#     't_yil':1978,
#     'yosh':43
# }
# tyil = otam['t_yil']
# yosh = otam['yosh']
# print(f"otamning ismi {otam['ism'].title()},{tyil}-yilda, {yosh} yoshda")
#
# taomlar = {
#     'dadam':'makaron',
#     'ayam':'shashlik',
#     'akam':'loviyali',
#     'ukam':'mastava'
#}
# makaron = taomlar['dadam']
# shashlik = taomlar['ayam']
# loviya = taomlar['akam']
# mastava = taomlar['ukam']
# print(f"dadam {makaron} ni yoqtiradi, ayam {shashlik} ni,"
#       f"akam {loviya}ni,ukam {mastava}ni yoqtiradi")

# lugat = {
#     'integer':'butun son',
#     'float':'o\'nlik son',
#     'string':'matn',
#     'list':'ro`xat',
#     'tuple':'o`zgarmas ro`yxat',
#     'input':'foydalananuvchi interpreteri',
# }
#
# kalit = input("kalit so`zni kiriting:").lower()
# tarjima = lugat.get(kalit)
# if tarjima==None:
#     print("bunday so`z mavjud emas")
# else:
#     print(f"{kalit.title()} {tarjima} deb tarjima qilinadi")

en_uz = {
    'apple':'olma',
    'describe':'tasvirlamoq',
    'grateful':'minnatdor',
    'design':'qaror',
    'nearby':'yaqin',
    'community':'jamiyat',
    'finally':'va nihoyat'
}

uzb = input('inglizcha so`z kiriting:').lower()
tarjima = en_uz.get(uzb)
if tarjima==None:
    print('bunday so`z mavjud emas')
else:
    print(f"{uzb.title()} {tarjima} deb tarjima qilinadi")
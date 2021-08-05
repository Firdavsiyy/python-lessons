# 11-dars bir necta shartlardi tekshirish
# elif - agar aks holda
# yosh = int(input("yoshingiz nechida:"))
# if yosh<=4:
#     narx = 0
# elif yosh<=12:
#     narx = 8000
#      narx = 5000
# elif yosh<=18:
#
# else:
#     narx = 10000
# print(f"sizga kirish {narx} sum") # or yoki degani
#
# kun = input("bugun qanday kun?")
# harorat = float(input("havo harorati qanday?"))
#
# if kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat>=30:
#     print("chomilgani ketdik")
# elif kun.lower()== 'yakshanba' or kun.lower()=='shanba' and harorat<30:
#     print("uyda dam olamiz!")  # and operatori yordamida 2 ta shartni bajarish mumkin
# BOOLEAN-malumotlar turi
# price = 15000  # mijoz 15000 sumga taom oldi
# choy = True  # mijoz choy ham oldi
# salat = True # mijoz salat olmadi
#
# if choy and salat:  # agar choy ham salat ham olgan bo'lsa
#     price = price + 10000  # narhga 10000 sum qoshamiz
# elif choy or salat:
#     price = price + 4000  # narxga 5000 sum qosamiz
#
# print(f"jami {price} sum")

# narx = 15000
# choy = 0
# non = 1
# salat  = True
# shirinlik  = False
# ichimlik = True
#
# if choy:
#     print("mijoz choy oldi")
#     narx = narx + 3000
#    print("mijoz  non    oldi")
#      narx = narx + 2000
#  if salat:
#      print("mijoz   salat   oldi")
#      narx = narx + 20000
#  if shirinlik:
#      print("mijoz  shirinlik    oldi")
# #     narx  = narx + 9000
#  if ichimlik:
#     print("mijoz  ichimlik    oldi")
#
#  print(f"Jami {narx} so'm")f non:
# osh = 20000
# shashlik = 42000
# manti = 5000
# xonim = 10000
# somsa = 7000
menu = ["osh","shashlik","manti","xonim","somsa"]
buyurtmalar = ['lavash','choy','manti','xonim','osh']
# ovqat = input("nima ovqat yeysiz?>>>")
# if ovqat.lower() not in menu:
#     print("afsuski bizda bunday ovqat yo'q")
# else:
#     print("buyurtma qabul qilindi.")
    # not in
if buyurtmalar:
    for taom in buyurtmalar:
     if taom in menu:
        print(f'menuda {taom} bor')
     else:
        print(f'kechirasiz, menuda {taom} yoq')
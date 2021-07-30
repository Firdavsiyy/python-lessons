# 11-dars bir necta shartlardi tekshirish
# elif - agar aks holda
yosh = int(input("yoshingiz nechida?"))
if yosh <= 4:
    narh = 0
elif yosh <= 12:
    narh = 5000
else:
    narh = 10000
    print("sizga kirish", narh, "so'm")

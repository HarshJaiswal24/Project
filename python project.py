inr_usd=0.012422
usd_inr=81.6445
rub_inr=1.3418
inr_rub=0.7522
cad_inr=60.9925
inr_cad=0.0164
cny_inr=11.4676
inr_cny=0.0872
eur_inr=84.298
inr_eur=0.0119
gbp_inr=97.059
inr_gbp=0.0103
print()
print("###### THIS CONVERTER IS ONLY USED TO CONVERT CURRENCY TO INR OR VICEVERSA ######")
print()
while True:
 print("PRESS 1 TO START!")
 print("PRESS 2 TO UPDATE CONVERSION RATE!")
 print("PRESS 3 TO EXIT!")
 print()
 choice=input("Enter your choice : ")
 if choice=="1":
 while True:
 print("{:15} : {:>4}".format("COUNTRY", "CURRENCY CODE"))
 denotion={"Indian Rupee":"INR",
 "US Dollars":"USD",
 "British Pounds":"GBP",
 "Euros":"EUR",
 "Canadian Dollar":"CAD",
 "Chinese Yuan":"CNY",
 "Russian Ruble":"RUB"}
 for i in denotion:
 print("{:15} : {:>4}".format(i,denotion[i]))
 from_unit=input("Enter the currency from which you want to convert: ")
 print()
 for j in denotion:
 if from_unit==denotion[j]:
 continue
 else:
 print("{:15} : {:>4}".format(j,denotion[j]))
 print()
 to_unit=input("Enter the currency to which you want to convert: ")
 print()
 values=denotion.values()
 if (from_unit and to_unit) in values:
 break
 else:
 print("Invalid Input")
 print()
 while True:
 Amount=input("Enter the Amount you want to convert: ")
 if Amount.isdigit():
 Amount=int(Amount)
 break
 else:
 print("Invalid Amount")
 if from_unit == "INR" and to_unit == "USD":
 print("Conversion rate is :", inr_usd)
 print()
 print(f'Converted Amount is {Amount*inr_usd}')
 elif from_unit == "USD" and to_unit == "INR":
 print("Conversion rate is :", usd_inr)
 print()
 print(f'Converted Amount is {Amount*usd_inr}')
 elif from_unit == "RUB" and to_unit == "INR":
 print("Conversion rate is :", rub_inr)
 print()
 print(f'Converted Amount is {Amount*rub_inr}')
 elif from_unit == "INR" and to_unit == "RUB":
 print("Conversion rate is :", inr_rub)
 print()
 print(f'Converted Amount is {Amount*inr_rub}')
 elif from_unit == "CAD" and to_unit == "INR":
 print("Conversion rate is :", cad_inr)
 print()
 print(f'Converted Amount is {Amount*cad_inr}')
 elif from_unit == "INR" and to_unit == "CAD":
 print("Conversion rate is :", inr_cad)
 print()
 print(f'Converted Amount is {Amount*inr_cad}')
 elif from_unit == "CNY" and to_unit == "INR":
 print("Conversion rate is :", cny_inr)
 print()
 print(f'Converted Amount is {Amount*cny_inr}')
 elif from_unit == "INR" and to_unit == "CNY":
 print("Conversion rate is :", inr_cny)
 print()
 print(f'Converted Amount is {Amount * inr_cny}')
 elif from_unit == "EUR" and to_unit == "INR":
 print("Conversion rate is :", eur_inr)
 print()
 print(f'Converted Amount is {Amount* eur_inr}')
 elif from_unit == "INR" and to_unit == "EUR":
 print("Conversion rate is :", inr_eur)
 print()
 print(f'Converted Amount is {Amount * inr_eur}')
 elif from_unit == "GBP" and to_unit == "INR":
 print("Conversion rate is :", gbp_inr)
 print()
 print(f'Converted Amount is {Amount*gbp_inr }')
 elif from_unit == "INR" and to_unit == "GBP":
 print("Conversion rate is :", inr_gbp)
 print()
 print(f'Converted Amount is {Amount * inr_gbp}')
 else:
 print("INVALID DENOTION","\n")
 elif choice=="2":
 print("{:15} : {:>4}".format("", "CURRENCY CODE"))
 denotion={"Indian Rupee":"INR",
 "US Dollars":"USD",
 "British Pounds":"GBP",
 "Euros":"EUR",
 "Canadian Dollar":"CAD",
 "Chinese Yuan":"CNY",
 "Russian Ruble":"RUB"}
 for i in denotion:
 print("{:15} : {:>4}".format(i,denotion[i]))
 choose1=input("Enter the currency from which you want to convert: ")
 print()
 for j in denotion:
 if choose1==denotion[j]:
 continue
 else:
 print("{:15} : {:>4}".format(j,denotion[j]))
 print()
 choose2=input("Enter the currency to which you want to convert: ")
 if choose1=="INR" and choose2=="USD":
 temp=float(input("Enter updated rate : "))
 inr_usd=temp
 elif choose1=="USD" and choose2=="INR":
 temp=float(input("Enter updated rate : "))
 usd_inr=temp
 elif choose1=="RUB" and choose2=="INR":
 temp=float(input("Enter updated rate : "))
 rub_inr=temp
 elif choose1=="INR" and choose2=="RUB":
 temp=float(input("Enter updated rate : "))
 inr_rub=temp
 elif choose1=="INR" and choose2=="CAD":
 temp=float(input("Enter updated rate : "))
 inr_cad=temp
 elif choose1=="CAD" and choose2=="INR":
 temp=float(input("Enter updated rate : "))
 cad_inr=temp
 elif choose1=="INR" and choose2=="CNY":
 temp=float(input("Enter updated rate : "))
 inr_cny=temp
 elif choose1=="CNY" and choose2=="INR":
 temp=float(input("Enter updated rate : "))
 cny_inr=temp
 elif choose1=="INR" and choose2=="EUR":
 temp=float(input("Enter updated rate : "))
 inr_eur=temp
 elif choose1=="EUR" and choose2=="INR":
 temp=float(input("Enter updated rate : "))
 eur_inr=temp
 elif choose1=="INR" and choose2=="GBP":
 temp=float(input("Enter updated rate : "))
 inr_gbp=temp
 elif choose1=="GBP" and choose2=="INR":
 temp=float(input("Enter updated rate : "))
 gbp_1inr=temp
 elif choice=="3":
 print("Exit")
 break
 else:
 print("Invalid Choice")

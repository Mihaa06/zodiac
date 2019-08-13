from datetime import*
print("Bun venit!Scrie data ta de nastere si eu o sa-ti ghicesc zodia!")
anul=int(input("In ce an esti nascut?"))
luna=int(input("in ce luna esti nascut"))
ziua=int(input("in ce zi esti nascut?"))
s_start=date(2004,3,21)
s_end=date(2004,4,19)
data=date(anul,luna,ziua)
if s_start <= data <= s_end:
    print("esti Berbec!")
s_start=date(2004,4,20)
s_end=date(2004,5,20)
data=date(anul,luna,ziua)
if s_start <= data <= s_end:
    print("esti Taur!")
s_start=date(2004,5,21)
s_end=date(2004,6,20)
data=date(anul,luna,ziua)
if s_start <= data <= s_end:
    print("esti Gemeni!")
s_start=date(2004,6,21)
s_end=date(2004,7,22)
data=date(anul,luna,ziua)
if s_start <= data <= s_end:
    print("esti Rac!")
s_start=date(2004,7,23)
s_end=date(2004,8,22)
data=date(anul,luna,ziua)
if s_start <= data <= s_end:
    print("esti Leu!")
s_start=date(2004,8,23)
s_end=date(2004,9,22)
data=date(anul,luna,ziua)
if s_start <= data <= s_end:
    print("esti Fecioara!")
s_start=date(2004,9,23)
s_end=date(2004,10,22)
data=date(anul,luna,ziua)
if s_start <= data <= s_end:
    print("esti Balanta!")
s_start=date(2004,10,23)
s_end=date(2004,11,21)
data=date(anul,luna,ziua)
if s_start <= data <= s_end:
    print("esti Scorpion!")
s_start=date(2004,11,22)
s_end=date(2004,12,21)
data=date(anul,luna,ziua)
if s_start <= data <= s_end:
    print("esti Sagetator!")
s_start=date(2004,12,22)
s_end=date(2004,1,19)
data=date(anul,luna,ziua)
if s_start <= data <= s_end:
    print("esti Capricorn!")
s_start=date(2004,1,20)
s_end=date(2004,2,18)
data=date(anul,luna,ziua)
if s_start <= data <= s_end:
    print("esti Varsator!")
s_start=date(2004,2,19)
s_end=date(2004,3,20)
data=date(anul,luna,ziua)
if s_start <= data <= s_end:
    print("esti Pesti!")









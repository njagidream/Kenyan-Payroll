print('KRA TAX CALCULATOR')
print('-------------------------')
tax = 0
gsalary=0
nssf=200
def calcNhif(gsalary1):
    if gsalary1 <= 5999 :
      nhif=150
    elif(gsalary1 >= 5999 and gsalary1 <= 7999) :
      nhif=300
    elif(gsalary1 >= 8000 and gsalary1 <= 11999) :
      nhif=400
    elif(gsalary1 >= 12000 and gsalary1 <= 14999) :
      nhif=500
    elif(gsalary1 >= 15000 and gsalary1 <= 19999) :
      nhif=600
    elif(gsalary1 >= 20000 and gsalary1 <= 24999) :
      nhif=750
    elif(gsalary1 >= 25000 and gsalary1 <= 29999) :
      nhif=850
    elif(gsalary1 >= 30000 and gsalary1 <= 34999) :
      nhif=900
    elif(gsalary1 >= 35000 and gsalary1 <= 39999) :
      nhif=950
    elif(gsalary1 >= 40000 and gsalary1 <= 44999) :
      nhif=1000
    elif(gsalary1 >= 45000 and gsalary1 <= 49999) :
      nhif=1100
    elif(gsalary1 >= 50000 and gsalary1 <= 59999) :
      nhif=1200
    elif(gsalary1 >= 60000 and gsalary1 <= 69999) :
      nhif=1300
    elif(gsalary1 >= 70000 and gsalary1 <= 79999) :
      nhif=1400
    elif(gsalary1 >= 80000 and gsalary1 <= 89999) :
      nhif=1500
    elif(gsalary1 >= 90000 and gsalary1 <= 99999) :
      nhif=1600
    elif gsalary1 >= 100000 :
      nhif=1700
    return nhif


def taxcalc(gsalary2):
    tax=0
    if(gsalary2 <= 10164):
      tax = 0
    elif gsalary2 > 10164 and gsalary2 <= 19740 :
      tax1 = 10 / 100 * 10164
      tax2 = (15 / 100 * (gsalary2 - 10164))
      tax = tax1 + tax2
    elif gsalary2 > 19740 and gsalary2 <= 29316 :
      tax1 = 10 / 100 * 10164
      tax2 = 15 / 100 * 9576
      tax3 = (20 / 100 * (gsalary2 - 19740))
      tax = tax1 + tax2 + tax3
    elif (gsalary2 > 29316 and gsalary2 <= 38892) :
      tax1 = 10 / 100 * 10164
      tax2 = 15 / 100 * 9576
      tax3 = 20 / 100 * 9576
      tax4 = 25 / 100 * (gsalary2 - 29316)
      tax = tax1 + tax2 + tax3 + tax4
    elif gsalary2 > 38892 :
      tax1 = 10 / 100 * 10164
      tax2 = 15 / 100 * 9576
      tax3 = 20 / 100 * 9576
      tax4 = 25 / 100 * 9576
      tax5 = 30 / 100 * (gsalary2 - 38892)
      tax = tax1 + tax2 + tax3 + tax4 + tax5
    return tax

def main():
    print('ENTER GROSS SALARY')
    gsalaryx = int(input())
    gsalnet=gsalaryx -nssf
    nhifamt =int( calcNhif(gsalaryx))
    taxz = int(taxcalc(gsalnet))-1162 # subtract relief
    print('Tax is ' + str(taxz))
    print('NHIF is ' + str(nhifamt))
    print('NSSF is ' + str(nssf))
    print('Net Income is ' + str(round(gsalaryx-taxz-nhifamt-nssf)))


main()


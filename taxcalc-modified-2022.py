print('KRA TAX CALCULATOR')
print('-------------------------')
tax = 0
gsalary=0
nssf=200
def calcNhif(gsalary1):
    if gsalary1 <= 24000 :
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
    if(gsalary2 <= 24000):
      tax = 0
    elif gsalary2 > 24000 and gsalary2 <= 32333 :
      tax1 = 10 / 100 * 24000
      tax2 = (25 / 100 * (gsalary2 - 24000))
      tax = tax1 + tax2
    
    elif gsalary2 > 32333 :
      tax1 = 10 / 100 * 24000
      tax2 = 25 / 100 * 8333
      tax3 = 30 / 100 * (gsalary2 - 32333)
      tax = tax1 + tax2 + tax3
    return tax

#calculate NHIF Relief
def calcnhifrelief(nhifamt):
    nhifrelief=15/100*nhifamt
    return nhifrelief

def main():
    print('ENTER GROSS SALARY')
    gsalaryx = int(input()) #capture gross salary 
    gsalnet=gsalaryx -nssf  #subtract nssf
    nhifamt =int( calcNhif(gsalaryx)) # nhif compute
    nhifrlf=calcnhifrelief(nhifamt )
    taxz = int(taxcalc(gsalnet))
    if(taxz>0):
       taxz = int(taxcalc(gsalnet))-2400-nhifrlf # subtract relief and nhifrelief

    print('=======================')   
    print('Tax is ' + str(taxz))
    print('NHIF is ' + str(nhifamt))
    print('NSSF is ' + str(nssf))
    print('Net Income is ' + str(round(gsalaryx-taxz-nhifamt-nssf)))

# Execute main function
main()


#Melissa Radford
#CIS 261
#Project Phase 3


from datetime import datetime
import locale

FILENAME = "Employees.txt"

def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
def GetDatesWorked():
    while True:
        date_str = input("Enter from date (YYY-MM-DD): ")
        try:
            fromdate = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue
        break
    while True:
        date_str = input("Enter end date (YYYY-MM-DD): ")
        try:
            enddate= datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Try again.")
            print()
        if enddate <= fromdate:
            print("End date must be after from date. Try again.")
            print()
        else: 
            break
    return fromdate, enddate    
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

#def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
#    print(empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")

def printinfo(DetailsPrinted):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00

    with open(FILENAME, "r") as EmpFile:
        while True:
            rundate = input ("Enter start date for report (MM/DD/YYYY) or All for all data in file:  ")
            if (rundate.upper() == "ALL"):
                break
            try:
                rundate = datetime.strptime(rundate, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Try again.")
                print()
                continue
        
        while True:
            EmpDetail = EmpFile.readline()
            if not EmpDetail:
                break
            EmpDetail = EmpDetail.replace("\n", "")
            EmpList = EmpDetail.split("|")
            fromdate = EmpList[0]
            if (str(rundate).upper() != "ALL"):
                checkdate = datetime.strptime(fromdate, "%Y-%m-%d" )
                if (checkdate < rundate):
                    continue
            enddate = EmpList[1]
            empname = EmpList[2]
            hours = float(EmpList[3])
            hourlyrate  = float(EmpList[4])
            taxrate = float(EmpList[5])
            grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
            print ("********************************************************")
            print("Name: ", empname)
            #print("From date:  ", fromdate)
            #print("To date:  ", enddate)
            print("Hours Worked:  ", f"{hours:,.2f}")
            print("Hourly Rate:  ", f"{hourlyrate:,.2f}")
            print("Gross Pay:  ", f"{grosspay:,.2f}" )
            print("Tax rate:  ", f"{taxrate:,.1%}" )
            print("Income tax:  ", f"{incometax:,.2f}")
            print("Net Pay:  ", f"{netpay:,.2f}")
            print ("********************************************************")
            print()

            TotEmployees += 1
            TotHours += hours
            TotGrossPay += grosspay
            TotTax += incometax
            TotNetPay += netpay
        
            EmpTotals["TotEmp"] = TotEmployees
            EmpTotals["TotHours"] = TotHours
            EmpTotals["TotGross"] = TotGrossPay
            EmpTotals["TotTax"] = TotTax
            EmpTotals["TotNet"] = TotNetPay
            DetailsPrinted = True
        if (DetailsPrinted):
            PrintTotals (EmpTotals)
        else:
            print("No detail information to print")


#def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
#    print()n
#    print(f"Total Number Of Employees: {TotEmployees}")
#    print(f"Total Hours Worked: {TotHours:,.2f}")
#    print(f"Total Gross Pay: {TotGrossPay:,.2f}")
#    print(f"Total Income Tax:  {TotTax:,.2f}")
#    print(f"Total Net Pay: {TotNetPay:,.2f}")

def PrintTotals(EmpTotals):    
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Of Employees: {EmpTotals["TotHours"]:,.2f}')
    print(f'Total Gross Pay Of Employees: {EmpTotals["TotGross"]:,.2f}')
    print(f'Total Tax Of Employees: {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay Of Employees: {EmpTotals["TotNet"]:,.2f}')



if __name__ == "__main__":
    with open(FILENAME, "a") as EmpFile:
    #EmpDetailList = []
        EmpTotals = {}
        DetailsPrinted = False
        while True:
            empname = GetEmpName()
            if (empname.upper() == "END"):
                break
            fromdate, enddate = GetDatesWorked()
            hours = GetHoursWorked()
            hourlyrate = GetHourlyRate()
            taxrate = GetTaxRate()
        #grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        #printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
            fromdate = fromdate.strftime ('%Y-%m-%d')
            enddate = enddate.strftime('%Y-%m-%d')

            EmpDetail = fromdate + "|" + enddate + "|" + empname + "|" + str(hours) + "|" + str(hourlyrate) + "|" + str(taxrate) + "\n"
            EmpFile.write(EmpDetail)

        #TotEmployees += 1
        #TotHours += hours
        #TotGrossPay += grosspay
        #TotTax += incometax
        #TotNetPay += netpay
   
    EmpFile.close()
    printinfo(DetailsPrinted)
    
    #PrintTotals(EmpTotals)
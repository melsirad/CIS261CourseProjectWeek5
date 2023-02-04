#Melissa Radford
#CIS 261
#Project Phase 2


def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname
def GetDatesWorked():
    fromdate = input("Enter start date (MM/DD/YYYY): ")
    enddate = input("Enter end date (MM/DD/YYYY:) ")
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

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        endate = EmpList[1]
        empname = EmpList[2]
        hoursworked = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]


        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
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
    print(f'Total Hours Of Employees: {EmpTotals["TotHours"]}')
    print(f'Total Gross Pay Of Employees: {EmpTotals["TotGross"]}')
    print(f'Total Tax Of Employees: {EmpTotals["TotTax"]}')
    print(f'Total Net Pay Of Employees: {EmpTotals["TotNet"]}')



if __name__ == "__main__":
    #TotEmployees = 0
    #TotHours = 0.00
    #TotGrossPay = 0.00
    #TotTax = 0.00
    #TotNetPay = 0.00
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        #grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        #printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)

        EmpDetail = [fromdate, enddate, empname, hours, hourrate, taxrate]
        EmpDetailList.append(EmpDetail)

        #TotEmployees += 1
        #TotHours += hours
        #TotGrossPay += grosspay
        #TotTax += incometax
        #TotNetPay += netpay

    printinfo(EmpDetailList)
    PrintTotals(EmpTotals)
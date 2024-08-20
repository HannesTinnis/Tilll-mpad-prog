

def calculate_monthly_payment(principal, annual_rate, years):
    #beräkna rate ( monthly_rate = annual_rate/12 /100)
    #beräkna month (month = years * 12)
    month = years * 12 
    monthly_rate = annual_rate / 12 / 100
    
    payment = (principal * monthly_rate * (1+monthly_rate) ** month) / ((1 + monthly_rate)** month - 1)
    return payment
    

principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))
payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")

    
    
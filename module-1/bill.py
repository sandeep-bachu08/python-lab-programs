consumer_name=input("Enter your name:")
consumer_Id=float(input("Enter your ID:"))
Previous_Meter_Reading=float(input("Enter your meter_reading:"))
Current_Meter_Reading=float(input("Enter your meter reading:"))
cost_per_unit=float(input("Enter your cost per unit:"))
units=float(input("Enter your units:"))
units_consumed=Current_Meter_Reading-Previous_Meter_Reading
Energy_charge=cost_per_unit*units
Electricity_Duty=5% Energy_charge
Fixed_meter_charge=100
Net_bill=Energy_charge+Electricity_Duty+Fixed_meter_charge
print("units consumed:",units_consumed)
print("Energy_charge:",Energy_charge)
print("Electricity duty:",Electricity_Duty)
print("Fixed meter charge:",Fixed_meter_charge)
print("Net bill:",Net_bill)
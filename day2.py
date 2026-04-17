age = int(input("How old are you? ")) 
income = int(input("How much do you earn per year? "))

if age >=18 and income >= 30000:
    print("You are financially stable (Basic level).")
else:
    print("You need to improve your situation.")
if income >= 60000:
    print("You are doing very well.")
if income <= 20000:
    print("You need to increase your income urgently.")
print("===================================================")
print("             SMART TRIP PLANNER")
print("===================================================")

place = input("\nWhere do you want to travel? ")
days = int(input("How many days? "))
budget = float(input("What is your total budget (₹)? "))

print("\nChoose your travel style:")
print("1. Budget")
print("2. Balanced")
print("3. Luxury")

style = int(input("Enter choice: "))

print("\nWhat do you prefer?")
print("1. Adventure")
print("2. Nature")
print("3. History")
print("4. Food")
print("5. Mixed")

choice = int(input("Enter choice: "))

# Budget distribution
if style == 1:
    travel = budget * 0.30
    hotel = budget * 0.25
    food = budget * 0.20
    activities = budget * 0.15
    emergency = budget * 0.10

elif style == 2:
    travel = budget * 0.25
    hotel = budget * 0.30
    food = budget * 0.20
    activities = budget * 0.15
    emergency = budget * 0.10

else:
    travel = budget * 0.20
    hotel = budget * 0.40
    food = budget * 0.20
    activities = budget * 0.15
    emergency = budget * 0.05

print("\n=======================================")
print("                 TRIP ANALYSIS")
print("========================================")

print("\nDestination :", place)
print("Duration    :", days, "days")
print("Budget      : ₹", budget)

print("\nBUDGET PLAN")
print("----------------------------------------")
print("Travel      : ₹", round(travel))
print("Hotel       : ₹", round(hotel))
print("Food        : ₹", round(food))
print("Activities  : ₹", round(activities))
print("Emergency   : ₹", round(emergency))

print("\nDAILY BUDGET")
print("-----------------------------------------")
print("₹", round(budget / days), "per day")

print("\nTRAVEL PLAN")
print("-----------------------------------------")

for i in range(1, days + 1):

    if choice == 1:
        activity = "Adventure activity + local exploration"

    elif choice == 2:
        activity = "Nature spot + scenic exploration"

    elif choice == 3:
        activity = "Historical place + local sightseeing"

    elif choice == 4:
        activity = "Local food + famous restaurants"

    else:
        activity = "Sightseeing + food + local activity"

    print("Day", i, "->", activity)

print("\nTRAVEL ADVICE")
print("--------------------------------------------------")

if budget / days < 1000:
    print("• Keep your daily expenses under control.")
    print("• Prefer affordable transport and accommodation.")
else:
    print("• You have a reasonable daily travel budget.")
    print("• Keep some money for unexpected expenses.")

print("• Keep emergency money separately.")
print("• Check local transport before travelling.")
print("• Keep important documents safely.")

print("\n=====================================================")
print("             YOUR TRIP IS READY!")
print("======================================================")
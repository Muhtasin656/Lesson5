actual_cost=float(input("enter the cost"))
sale_cost=float(input("enter the sale cost"))
if sale_cost>actual_cost:
    profit=sale_cost-actual_cost
    print(f"the total profit is{profit}")
else:
    print("no profit")
    
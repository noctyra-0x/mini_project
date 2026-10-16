expense_list=[]
print("----Personal Expense Tracker----")
for i in range(2):
    category=input("\nEnter the category ( e.g. Food, Transport)")
    price=float(input("Enter price for {category}: $ "))
    item={"category": category , "price" :price}
    expense_list.append(item)
    total=0
    print("---Summary Total---")
    for item in expense_list:
        print(f"{item['category']} : ${item['price']:.2f}")
        total= total + item["price"]
    with open("receipt.txt" , "w") as file:
        file.write("===Your Receipt===\n")
        for item in expense_list:
            file.write(f"{item['category']} : ${item['price']}:.2f\n")
            file.write("\nTotal: ${total: .2f}\n")
    print("\n  Saved receipt to 'Receipt File' ")
    
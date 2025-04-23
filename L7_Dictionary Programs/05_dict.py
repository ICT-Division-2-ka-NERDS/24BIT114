groceries_price={"banana":10,"apple":30,"curd":50}
groceries_amount={"banana":3,"apple":2,"curd":1}
total_bill=sum(groceries_price[item]*groceries_amount.get(item,0) for item in groceries_price)
print("Total bill:",total_bill)

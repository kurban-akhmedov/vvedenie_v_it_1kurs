s = int(input())
price = 7.61
price_with_discount = price * s - (price * s) * 0.18
discount_is = price * s * 0.18
print("The final price is: " + str("%.2f" % price_with_discount) + " $")
print("The discount is: " + str("%.2f" % discount_is) + " $")
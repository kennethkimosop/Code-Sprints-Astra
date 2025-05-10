# p = original price
# d = percentage discount

def getdiscountedPS(p, d):
    discounted_price = p * (1 - d / 100)
    return round(discounted_price, 2)


print(getdiscountedPS(1500, 50))  
print(getdiscountedPS(89, 20))    
print(getdiscountedPS(100, 75))   


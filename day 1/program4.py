# TAKE 2 INPUTS, COST PRICE,SELLING PRICE OF A PRODUCT FROM USER AND RETURN FOLLOWING:
#  * PROFIT FROM HIS SELL
#  * WHAT SHOULD BE THE SELLING PRICE IF WE WANT TO INCREASE PROFIT BY 5%

a=int(input("enter cost price of the product ="))
b=int(input("enter selling price of the product ="))
c=b-a
d=b+(a*0.05)
print("profit from his sell =",c)
print("selling price after increasing profit by 5% =",d)

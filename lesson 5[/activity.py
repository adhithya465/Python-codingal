field1=20
field2=140
field3=50
field4=70
field5=10
total=(field1+field2+field3+field4+field5)
mean=total/5
print("Total: ",total)
print("Mean: ",mean)
price_per_kg=20
earnings=price_per_kg*total
print("earnings: ", earnings)
bags=total//25
leftover=total%25
print("bags: ", bags)
print("leftover: ", leftover, " kgs")
last_year=500
print("Better than last year? ",total>last_year )
print("Same as last year?",total==last_year)
print("Worse than last year?", total<last_year)
print("As least as good as the previous year?", total>=last_year)
total+=30
print("total: ", total)
total-=15
print("total: ",total)
bags=total//25
leftover=total%25
print("bags: ", bags)
print("leftover: ", leftover, " kgs")

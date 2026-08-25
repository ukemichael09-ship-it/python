# ======================================================

# --- Assignment Operator (=) ---
field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

# --- Arithmethic Operators (+, -, *, /) ---
# Calculate total and average harvest
total = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest   :", total, "kg")
print("Average per field  :", average, "kg")

# Price per kg is 15 rupees - calculate total earnings
price_per_kg = 15
earings = total * price_per_kg
print("Total earnings   : Rs.", earnings)

# --- Floor Division (///) and Moduls (%) ---
# Pack the harvest into bags of 25 kg each
bags   = total // 25
leftover = total % 25

print("Full bags packed   :", bags)
print("Leftover grain   :", leftover, "kg")

# ---Comparson Operators (>, <, ==, >=) ---
# Compare this year's harvest with last year
last_year = 500
print("Better than last yer?  :", total > last_year)
print("Smae as last year?   :", total == last_year)
print("At least as good?   :", total >= last_year)

# --- Assignment Operators (+=, -=) ---
# A bonus field adds 30 kg to the total
total += 30
print("After bonus crop   :", total, "kg")

# Subtract 15 kg saved as seeds for next season
total -= 15
print("Afterseed reserve :", total, "kg")

# Final bag count after all adjustments
bags = total // 25
print("Finale bags packed   :", bags)
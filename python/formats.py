price1 = 231233.14159
price2 = -2323213.32
price3 = 12323232.211

# :.2f
# :0(2) meaning it will allocate zeroes up until space is reached
# :10 gives space
# :<2 left justified
# :>10 right justified
# :^10 centered
# :+ positive sign or space :
# :,

print(f"Price 1 | ₱{price1:>20,.2f}")
print(f"Price 2 | ₱{price2:>20,.2f}")
print(f"Price 3 | ₱{price3:>20,.2f}")
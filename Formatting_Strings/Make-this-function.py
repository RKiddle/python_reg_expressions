""""
To perform an operation between var1 and var2 inside a f-string, use f"{var1 * var2}". 
Remember that you can use the format specifier :.nf to indicate the number n of decimals.
""""

# Include both variables and the result of dividing them 
print(f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {(number1/number2):.1f} tweets per min")

# Replace the substring http by an empty string
print(f"{string1.replace('https', '')}")

# Divide the length of list by 120 rounded to two decimals
print(f"Only {len(list_links)*100/120:.2f}% of the posts contain links")

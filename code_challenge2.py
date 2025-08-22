def breakdown(amount):
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    result = {}

    for denom in denominations:
        count = amount // denom
        if count > 0:
            result[denom] = count
            amount %= denom
    return result

# Main program
amount = int(input("Enter amount to deposit: ₱"))
print("\nBreakdown:")

breakdown_result = breakdown(amount)
for denom, count in breakdown_result.items():
    print(f"₱{denom} x {count}")
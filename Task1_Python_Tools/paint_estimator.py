def get_float(prompt):
    try:
        return float(input(prompt) or 0)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_float(prompt)

def get_paint_type():
    print("\nChoose paint type:")
    print("1. Emulsion Paint (Rs 180 per litre)")
    print("2. Oil Paint (Rs 250 per litre)")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        return 'Emulsion', 180
    elif choice == '2':
        return 'Oil', 250
    else:
        print("Invalid choice.")
        return get_paint_type()

# Step 1: Input Room Dimensions
print("🎨 Room Paint Quantity & Cost Estimator")

length = get_float("Enter room length in feet: ")
width = get_float("Enter room width in feet: ")
height = get_float("Enter room height in feet: ")

# Step 2: Calculate Wall Area (4 walls only, no ceiling/floor)
wall_area = 2 * height * (length + width)  # in sq.ft
coverage_per_litre = 100  # 1 litre covers 100 sq.ft

# Step 3: Calculate paint needed
litres_needed = wall_area / coverage_per_litre

# Step 4: Choose paint type and cost
paint_type, price_per_litre = get_paint_type()

# Step 5: Total cost
total_cost = litres_needed * price_per_litre

# Step 6: Output result
print("\n🧾 Paint Estimation Summary:")
print(f"Total wall area: {wall_area:.2f} sq.ft")
print(f"Paint type: {paint_type}")
print(f"Litres of paint needed: {litres_needed:.2f} L")
print(f"Price per litre: Rs {price_per_litre}")
print(f"Total cost: Rs {total_cost:.2f}")

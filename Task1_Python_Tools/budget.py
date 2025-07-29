def get_float_input(prompt):
    try:
        return float(input(prompt) or 0)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_float_input(prompt)

print("🛋️ Interior Design Budget Calculator 🖌️")

furniture = get_float_input("Enter cost of Furniture (Rs): ")
paint = get_float_input("Enter cost of Paint (Rs): ")
lights = get_float_input("Enter cost of Lights (Rs): ")
decor = get_float_input("Enter cost of Decor (Rs): ")
discount = get_float_input("Enter Discount (Rs): ")

subtotal = furniture + paint + lights + decor
tax = subtotal * 0.18  # GST 18%
total = subtotal + tax - discount

print("\n🧾 Budget Summary:")
print(f"Subtotal: Rs {subtotal:.2f}")
print(f"GST (18%): Rs {tax:.2f}")
print(f"Discount: Rs {discount:.2f}")
print(f"Total Estimated Budget: Rs {total:.2f}")

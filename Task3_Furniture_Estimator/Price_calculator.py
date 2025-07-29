from fpdf import FPDF

def calculate_furniture_price():
    print("=== Interior Furniture Price Estimator ===")

    customer_name = input("Enter your name: ").strip()
    if not customer_name:
        print("Name cannot be empty.")
        return

    estimates = []

    # Initial prompt to proceed
    while True:
        start = input("Do you want to start adding furniture items? (yes/no): ").strip().lower()
        if start == "no":
            print("No estimates were added.")
            return
        elif start == "yes":
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    furniture_items = [
        "Bed",
        "Wardrobe",
        "Crockery Unit",
        "Storage Unit",
        "Chest of Drawers"
    ]

    wood_types = {
        "Plywood": 1500,
        "MDF": 1200,
        "Teak Wood": 2500,
        "Particle Board": 1000,
        "Solid Wood": 3000
    }

    while True:
        try:
            print("\nSelect furniture type:")
            for i, item in enumerate(furniture_items, 1):
                print(f"{i}. {item}")
            choice = int(input("Enter your choice (1-5): "))
            if choice < 1 or choice > len(furniture_items):
                print("Invalid furniture choice.")
                continue
            furniture_type = furniture_items[choice - 1]

            print("\nSelect wood type:")
            wood_keys = list(wood_types.keys())
            for i, wood in enumerate(wood_keys, 1):
                print(f"{i}. {wood} (Rs.{wood_types[wood]} per sq.ft)")
            wood_choice = int(input("Enter your choice (1-5): "))
            if wood_choice < 1 or wood_choice > len(wood_keys):
                print("Invalid wood choice.")
                continue
            selected_wood = wood_keys[wood_choice - 1]
            price_per_sqft = wood_types[selected_wood]

            length = float(input("\nEnter length (in feet): "))
            breadth = float(input("Enter breadth (in feet): "))
            height = float(input("Enter height (in feet): "))
            if length <= 0 or breadth <= 0 or height <= 0:
                print("Dimensions must be positive.")
                continue

            dimensions = [length, breadth, height]
            dimensions.sort(reverse=True)
            used_dims = dimensions[:2]
            area = used_dims[0] * used_dims[1]
            total_price = area * price_per_sqft

            estimates.append({
                "furniture": furniture_type,
                "wood": selected_wood,
                "used_dims": used_dims,
                "area": area,
                "rate": price_per_sqft,
                "price": total_price
            })

            print(f"\n--- Estimate Added ---")
            print(f"Furniture: {furniture_type}")
            print(f"Wood Type: {selected_wood}")
            print(f"Used Area: {used_dims[0]} ft × {used_dims[1]} ft = {area:.2f} sq.ft")
            print(f"Rate: Rs.{price_per_sqft}/sq.ft")
            print(f"Estimated Price: Rs.{total_price:.2f}")

            while True:
                more = input("\nDo you want to add another furniture item? (yes/no): ").strip().lower()
                if more in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
            if more == "no":
                break

        except ValueError:
            print("Please enter valid numeric inputs.")
            continue

    if not estimates:
        print("No estimates were added.")
        return

    # PDF generation
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Interior Furniture Estimate Invoice", ln=True, align='C')

    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Customer Name: {customer_name}", ln=True)

    for idx, estimate in enumerate(estimates, 1):
        pdf.ln(5)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, f"Item {idx}:", ln=True)

        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"Furniture Type: {estimate['furniture']}", ln=True)
        pdf.cell(0, 10, f"Wood Type: {estimate['wood']}", ln=True)
        dims = estimate["used_dims"]
        pdf.cell(0, 10, f"Used Area: {dims[0]} ft × {dims[1]} ft = {estimate['area']:.2f} sq.ft", ln=True)
        pdf.cell(0, 10, f"Rate: Rs.{estimate['rate']}/sq.ft", ln=True)
        pdf.cell(0, 10, f"Estimated Price: Rs.{estimate['price']:.2f}", ln=True)

    filename = f"{customer_name}_invoice.pdf".replace(" ", "_")
    pdf.output(filename)
    print(f"\nPDF invoice saved as: {filename}")

# Run the estimator
calculate_furniture_price()

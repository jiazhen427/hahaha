import streamlit as st

# Expanded car database with many brands
cars = [
    # Affordable/Family Cars
    {"name": "Perodua Alza", "seats": 7, "type": "Family", "price": 70000},
    {"name": "Proton Exora", "seats": 7, "type": "Family", "price": 68000},
    {"name": "Perodua Myvi", "seats": 5, "type": "Compact", "price": 50000},
    {"name": "Toyota Vios", "seats": 5, "type": "Sedan", "price": 85000},
    {"name": "Honda BR-V", "seats": 7, "type": "Family", "price": 90000},
    {"name": "Hyundai Tucson", "seats": 5, "type": "SUV", "price": 160000},
    {"name": "Kia Carnival", "seats": 8, "type": "Family", "price": 200000},
    {"name": "Mazda CX-5", "seats": 5, "type": "SUV", "price": 170000},

    # Mid to Premium Cars
    {"name": "BMW 3 Series", "seats": 5, "type": "Luxury", "price": 280000},
    {"name": "Mercedes-Benz C200", "seats": 5, "type": "Luxury", "price": 290000},
    {"name": "Audi A4", "seats": 5, "type": "Luxury", "price": 270000},
    {"name": "Volkswagen Passat", "seats": 5, "type": "Luxury", "price": 180000},
    {"name": "Lexus RX350", "seats": 5, "type": "Luxury", "price": 400000},

    # High-End Luxury
    {"name": "BMW X5", "seats": 7, "type": "Luxury", "price": 450000},
    {"name": "Mercedes-Benz GLC", "seats": 5, "type": "Luxury", "price": 380000},
    {"name": "Maybach S580", "seats": 5, "type": "Ultra Luxury", "price": 1600000},
    {"name": "Maserati Levante", "seats": 5, "type": "Luxury", "price": 700000},

    # Supercars
    {"name": "Ferrari 488 GTB", "seats": 2, "type": "Supercar", "price": 1200000},
    {"name": "Lamborghini Huracan", "seats": 2, "type": "Supercar", "price": 1500000},
    {"name": "Porsche 911 GT3", "seats": 2, "type": "Supercar", "price": 1700000},
    {"name": "McLaren 720S", "seats": 2, "type": "Supercar", "price": 1600000},
    {"name": "Aston Martin DB11", "seats": 4, "type": "Supercar", "price": 1300000}
]

def calculate_affordable_price(monthly_income, loan_years=7, max_percent=0.2, interest_rate=0.03):
    monthly_payment = monthly_income * max_percent
    total_budget = monthly_payment * 12 * loan_years  # Simple estimate
    return total_budget

def main():
    st.title("🚘 Car Affordability Calculator")

    st.markdown("This app helps you find cars you can afford based on your monthly income and needs.")

    income = st.number_input("Enter your monthly income (RM)", min_value=1000, value=7000, step=100)
    seats = st.number_input("Minimum number of seats needed", min_value=2, max_value=10, value=7)
    
    # Dynamically get unique car types
    car_types = sorted(set(car["type"] for car in cars))
    car_types.insert(0, "Any")
    car_type = st.selectbox("Preferred car type", car_types)

    if income > 0:
        st.divider()
        max_price = calculate_affordable_price(income)
        st.write(f"💰 Estimated max car price you can afford: **RM {max_price:,.2f}**")

        st.subheader("✅ Cars You Can Afford:")
        found = False
        for car in cars:
            if (
                car["price"] <= max_price and
                car["seats"] >= seats and
                (car_type == "Any" or car["type"] == car_type)
            ):
                st.markdown(f"- **{car['name']}** — RM {car['price']:,}")
                found = True

        if not found:
            st.warning("😕 No cars found within your budget and needs.")

if __name__ == "__main__":
    main()


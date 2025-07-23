import streamlit as st

# Full car database, now includes supercars
cars = [
    {"name": "Perodua Alza", "seats": 7, "type": "Family", "price": 70000},
    {"name": "Proton Exora", "seats": 7, "type": "Family", "price": 68000},
    {"name": "Perodua Myvi", "seats": 5, "type": "Compact", "price": 50000},
    {"name": "Honda BR-V", "seats": 7, "type": "Family", "price": 90000},
    {"name": "Toyota Vios", "seats": 5, "type": "Sedan", "price": 85000},

    # Supercars
    {"name": "Ferrari 488 GTB", "seats": 2, "type": "Supercar", "price": 1200000},
    {"name": "Lamborghini Huracan", "seats": 2, "type": "Supercar", "price": 1500000},
    {"name": "Porsche 911", "seats": 4, "type": "Supercar", "price": 1000000},
    {"name": "McLaren 720S", "seats": 2, "type": "Supercar", "price": 1600000},
    {"name": "Aston Martin DB11", "seats": 4, "type": "Supercar", "price": 1300000},
]

def main():
    st.title("🚗 Car Affordability Calculator")

    income = st.number_input("Enter your monthly income (RM)", min_value=1000, step=100)
    seats_needed = st.number_input("Minimum number of seats needed", min_value=2, max_value=10, step=1)

    # Dynamically get all car types + "Any" option
    car_types = list(set(car["type"] for car in cars))
    car_types.sort()
    car_types.insert(0, "Any")
    car_type = st.selectbox("Select car purpose/type", car_types)

    if income > 0:
        max_monthly_payment = income * 0.2
        loan_years = 7
        interest_rate = 0.03
        total_budget = max_monthly_payment * 12 * loan_years

        st.write(f"💰 Estimated max car price you can afford: **RM {total_budget:,.2f}**")

        st.subheader("🚙 Cars You Can Afford:")
        found = False
        for car in cars:
            if (car["price"] <= total_budget and 
                car["seats"] >= seats_needed and 
                (car_type == "Any" or car["type"] == car_type)):
                st.write(f"- {car['name']} - RM {car['price']:,}")
                found = True

        if not found:
            st.write("😢 Sorry, no cars found within your budget and needs.")

if __name__ == "__main__":
    main()


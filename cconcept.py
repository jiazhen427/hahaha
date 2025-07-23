import streamlit as st

# Sample car database
cars = [
    {"name": "Perodua Alza", "seats": 7, "type": "Family", "price": 70000},
    {"name": "Proton Exora", "seats": 7, "type": "Family", "price": 68000},
    {"name": "Perodua Myvi", "seats": 5, "type": "Compact", "price": 50000},
    {"name": "Honda BR-V", "seats": 7, "type": "Family", "price": 90000},
    {"name": "Toyota Vios", "seats": 5, "type": "Sedan", "price": 85000},
]

def main():
    st.title("🚗 Car Affordability Calculator")

    income = st.number_input("Enter your monthly income (RM)", min_value=1000, step=100)
    seats_needed = st.number_input("Minimum number of seats needed", min_value=2, max_value=10, step=1)
    car_type = st.selectbox("Select car purpose/type", ["Any", "Family", "Compact", "Sedan"])

    if income > 0:
        max_monthly_payment = income * 0.2
        loan_years = 7
        interest_rate = 0.03  # 3% annual interest
        total_budget = max_monthly_payment * 12 * loan_years  # Simplified loan estimation

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

import streamlit as st
import math

# Expanded car database with images, HP, CC and many brands
cars = [
    {"name": "Perodua Alza", "seats": 7, "type": "Family", "price": 70000, "image": "https://i.imgur.com/OaV9sQE.jpg", "hp": 105, "cc": 1500},
    {"name": "Proton Exora", "seats": 7, "type": "Family", "price": 68000, "image": "https://i.imgur.com/qTkZJAz.jpg", "hp": 125, "cc": 1600},
    {"name": "Perodua Myvi", "seats": 5, "type": "Compact", "price": 50000, "image": "https://i.imgur.com/Z5wr8VO.jpg", "hp": 95, "cc": 1300},
    {"name": "Toyota Vios", "seats": 5, "type": "Sedan", "price": 85000, "image": "https://i.imgur.com/2rAyABu.jpg", "hp": 107, "cc": 1500},
    {"name": "Honda BR-V", "seats": 7, "type": "Family", "price": 90000, "image": "https://i.imgur.com/OzEj20k.jpg", "hp": 120, "cc": 1500},
    {"name": "Hyundai Tucson", "seats": 5, "type": "SUV", "price": 160000, "image": "https://i.imgur.com/m0LjBp1.jpg", "hp": 181, "cc": 2000},
    {"name": "Kia Carnival", "seats": 8, "type": "Family", "price": 200000, "image": "https://i.imgur.com/WnYgeZU.jpg", "hp": 199, "cc": 2200},
    {"name": "Mazda CX-5", "seats": 5, "type": "SUV", "price": 170000, "image": "https://i.imgur.com/fMECnH1.jpg", "hp": 191, "cc": 2500},
    
    {"name": "BMW 3 Series", "seats": 5, "type": "Luxury", "price": 280000, "image": "https://i.imgur.com/ERBaVPK.jpg", "hp": 255, "cc": 2000},
    {"name": "Mercedes-Benz C200", "seats": 5, "type": "Luxury", "price": 290000, "image": "https://i.imgur.com/S8Wr37R.jpg", "hp": 204, "cc": 1500},
    {"name": "Audi A4", "seats": 5, "type": "Luxury", "price": 270000, "image": "https://i.imgur.com/8Whbklr.jpg", "hp": 201, "cc": 2000},
    {"name": "Volkswagen Passat", "seats": 5, "type": "Luxury", "price": 180000, "image": "https://i.imgur.com/YKLy3ZT.jpg", "hp": 220, "cc": 2000},
    {"name": "Lexus RX350", "seats": 5, "type": "Luxury", "price": 400000, "image": "https://i.imgur.com/wukZTkT.jpg", "hp": 275, "cc": 3500},
    {"name": "BMW X5", "seats": 7, "type": "Luxury", "price": 450000, "image": "https://i.imgur.com/ifldL9x.jpg", "hp": 335, "cc": 3000},
    {"name": "Mercedes-Benz GLC", "seats": 5, "type": "Luxury", "price": 380000, "image": "https://i.imgur.com/WZ7FM8v.jpg", "hp": 258, "cc": 2000},
    {"name": "Maybach S580", "seats": 5, "type": "Ultra Luxury", "price": 1600000, "image": "https://i.imgur.com/jU6qHCL.jpg", "hp": 496, "cc": 4000},
    {"name": "Maserati Levante", "seats": 5, "type": "Luxury", "price": 700000, "image": "https://i.imgur.com/tUXLtGj.jpg", "hp": 345, "cc": 3000},

    {"name": "Ferrari 488 GTB", "seats": 2, "type": "Supercar", "price": 1200000, "image": "https://i.imgur.com/YbG5kkz.jpg", "hp": 661, "cc": 3900},
    {"name": "Lamborghini Huracan", "seats": 2, "type": "Supercar", "price": 1500000, "image": "https://i.imgur.com/QTjAXEq.jpg", "hp": 631, "cc": 5200},
    {"name": "Porsche 911 GT3", "seats": 2, "type": "Supercar", "price": 1700000, "image": "https://i.imgur.com/KqJqKgD.jpg", "hp": 502, "cc": 4000},
    {"name": "McLaren 720S", "seats": 2, "type": "Supercar", "price": 1600000, "image": "https://i.imgur.com/4j5ImbZ.jpg", "hp": 710, "cc": 4000},
    {"name": "Aston Martin DB11", "seats": 4, "type": "Supercar", "price": 1300000, "image": "https://i.imgur.com/N6ZrLMx.jpg", "hp": 528, "cc": 4000}
]

# Monthly loan formula
def calculate_monthly_payment(price, down_payment=20000, interest_rate=0.03, years=7):
    loan_amount = price - down_payment
    r = interest_rate / 12
    n = years * 12
    if r == 0:
        return loan_amount / n
    return loan_amount * (r * (1 + r)**n) / ((1 + r)**n - 1)

def calculate_affordable_price(monthly_income, max_percent=0.2):
    return monthly_income * max_percent

def main():
    st.title("🚘 Car Affordability Calculator")
    st.markdown("Find out what car you can afford based on your monthly income and your needs.")

    income = st.number_input("Enter your monthly income (RM)", min_value=1000, value=7000, step=100)
    seats = st.number_input("Minimum number of seats needed", min_value=2, max_value=10, value=5)

    car_types = sorted(set(car["type"] for car in cars))
    car_types.insert(0, "Any")
    car_type = st.selectbox("Preferred car type", car_types)

    if income > 0:
        max_monthly_payment = calculate_affordable_price(income)
        st.divider()
        st.write(f"💰 Maximum monthly loan payment you can afford: **RM {max_monthly_payment:,.2f}**")

        st.subheader("✅ Cars You Can Afford")
        found = False
        for car in cars:
            monthly_payment = calculate_monthly_payment(car["price"])
            if (
                monthly_payment <= max_monthly_payment and
                car["seats"] >= seats and
                (car_type == "Any" or car["type"] == car_type)
            ):
                st.image(car["image"], width=300)
                st.markdown(f"### {car['name']}")
                st.write(f"Type: {car['type']}")
                st.write(f"Seats: {car['seats']}")
                st.write(f"Engine: {car['cc']} cc")
                st.write(f"Horsepower: {car['hp']} hp")
                st.write(f"Price: RM {car['price']:,}")
                st.write(f"Estimated Monthly Payment: **RM {monthly_payment:,.2f}**")
                st.markdown("---")
                found = True

        if not found:
            st.warning("😕 No cars found within your budget and filters.")

if __name__ == "__main__":
    main()



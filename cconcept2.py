import streamlit as st

def calculate_monthly_loan(price, deposit, interest_rate, years):
    loan_amount = price - deposit
    total_interest = loan_amount * (interest_rate / 100) * years
    total_payable = loan_amount + total_interest
    monthly_payment = total_payable / (years * 12)
    return monthly_payment

def main():
    st.title("🚗 Car Cost Calculator")

    st.subheader("Step 1: Enter Car Details")
    car_model = st.text_input("Car model", value="Porsche 911 GT3")
    car_price = st.number_input("Car price (RM)", value=1700000, step=10000)
    
    st.subheader("Step 2: Cost Parameters")
    deposit = st.number_input("Deposit (RM)", value=300000, step=10000)
    interest_rate = st.slider("Interest rate (%)", min_value=0.0, max_value=10.0, value=3.0)
    loan_term_years = st.slider("Loan term (years)", 1, 9, value=7)

    insurance = st.number_input("Annual insurance (RM)", value=15000, step=1000)
    road_tax = st.number_input("Annual road tax (RM)", value=5000, step=500)
    wear_tear = st.number_input("Annual wear & tear (RM)", value=10000, step=1000)

    st.subheader("📊 Results")

    monthly_payment = calculate_monthly_loan(car_price, deposit, interest_rate, loan_term_years)
    yearly_loan_payment = monthly_payment * 12

    total_yearly_cost = yearly_loan_payment + insurance + road_tax + wear_tear

    st.write(f"🚘 **Model**: {car_model}")
    st.write(f"💰 **Monthly Loan Payment**: RM {monthly_payment:,.2f}")
    st.write(f"📅 **Yearly Loan Payment**: RM {yearly_loan_payment:,.2f}")
    st.write(f"📦 **Total Yearly Cost (with insurance, tax, etc)**: RM {total_yearly_cost:,.2f}")

if __name__ == "__main__":
    main()


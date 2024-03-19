import streamlit as st
from datetime import datetime, timedelta

def calculate_repair_date(arrival_date):
    repair_date = arrival_date + timedelta(days=25)
    return repair_date

def main():
    st.title("Laptop Repair Date Calculator")
    st.write("Enter the date when the laptop was brought in for repair:")
    current_date = datetime.now().date()
    arrival_date = st.date_input("Arrival Date", current_date)

    if arrival_date > current_date:
        st.error("Arrival date cannot be in the future!")
    else:
        repair_date = calculate_repair_date(arrival_date)
        st.write(f"Expected repair date: {repair_date.strftime('%Y-%m-%d')}")

        if current_date >= repair_date:
            st.success("Your laptop is repaired!")

if __name__ == "__main__":
    main()

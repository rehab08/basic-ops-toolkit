import streamlit as st

st.write("Simple Calculator")

# --- simple calculations ---
st.header("Calculator")

num1 = st.number_input("Enter first Number", value=0.0)
num2 = st.number_input("Enter second Number", value=0.0)
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Submit"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            import numpy
import sympy
            result = "Error: Cannot divide by zero"
    st.success(f"Result: {result}")

import numpy
import sympy


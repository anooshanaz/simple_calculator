import streamlit as st

def main():
    st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")
    st.markdown("""
        <style>
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 18px;
            }
            .stTextInput>div>div>input {
                font-size: 20px;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🧮 Simple Calculator")
    
    num1 = st.number_input("Enter first number", value=0.0, step=1.0, format="%.2f")
    num2 = st.number_input("Enter second number", value=0.0, step=1.0, format="%.2f")
    
    operation = st.radio("Choose an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))
    
    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                st.error("Cannot divide by zero!")
                return
            result = num1 / num2
        
        st.success(f"Result: {result:.2f}")

if __name__ == "__main__":
    main()

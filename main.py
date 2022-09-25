from fastapi import FastAPI
import streamlit as st

app = FastAPI()
current_command = "no command"

@app.get("/current_cmd")
def get_current_command():
    global current_command
    return current_command


def print_out_web_interface():
    global current_command
    st.header("Command Input")
    st.text("\n\n\n")
    
    command = st.text_input("Input your command: ")

    if st.button("Set Command"):
        current_command = command
        st.text("Command was set to: $ %s" % (command))

print_out_web_interface()
    

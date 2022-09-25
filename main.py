from fastapi import FastAPI
import uvicorn
import streamlit as st
import nest_asyncio

nest_asyncio.apply()

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


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)

print_out_web_interface()

    

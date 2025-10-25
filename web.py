import streamlit as st
from streamlit import checkbox

import functions
todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo +'\n')
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        if todo in st.session_state:
            del st.session_state[todo]
            st.rerun()


st.text_input(label="", placeholder="Add new todo....",
           on_change=add_todo, key='new_todo').strip()




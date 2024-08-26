from functione import get_todos, write_todos
import streamlit as st

todos = get_todos()

def add_todo():
    new_todo = st.session_state["new todo"]
    todos.append(new_todo+"\n")
    functione.write_todos(todos)



st.title("Scam List")
st.subheader("Made in India")
st.write("This app is to increase Yor productivity")

i=0
for index, todo in enumerate(todos):
    chckbox =  st.checkbox(todo, key=todo)
    if chckbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="", placeholder = "Add new todo....", on_change=add_todo, key="new todo")



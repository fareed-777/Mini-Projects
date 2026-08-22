import streamlit as st
import json
import time

# Page Configuration with Animations & Dark Theme
st.set_page_config(page_title="Task Hub", page_icon="⚡", layout="centered")

# Custom Title with Visual Effects
st.title("⚡ Interactive To-Do Hub")
st.caption("Powered by Streamlit")

# File Data Logic
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

# --- INPUT SECTION ---
with st.form("add_task_form", clear_on_submit=True):
    col1, col2 = st.columns([3, 1])
    with col1:
        new_title = st.text_input("New Task", placeholder="What needs to be done?")
    with col2:
        submitted = st.form_submit_button("Add Task", use_container_width=True)

    if submitted and new_title.strip():
        new_task = {"id": len(tasks) + 1, "title": new_title, "Status": False}
        tasks.append(new_task)
        save_tasks(tasks)
        st.toast("Task added successfully!", icon="🎉") # Pop-up effect
        st.rerun()

# --- DISPLAY & EFFECT SECTION ---
st.subheader("Your Tasks")

if not tasks:
    st.info("No active tasks found! Add one above.")
else:
    for idx, task in enumerate(tasks):
        col_check, col_del = st.columns([4, 1])
        
        with col_check:
            # Interactive Checkbox
            is_done = st.checkbox(f"**{task['title']}**", value=task["Status"], key=f"check_{idx}")
            if is_done != task["Status"]:
                tasks[idx]["Status"] = is_done
                save_tasks(tasks)
                if is_done:
                    st.balloons() # Confetti/Balloons animation effect!
                st.rerun()

        with col_del:
            # Delete Button
            if st.button("🗑️", key=f"del_{idx}"):
                tasks.pop(idx)
                for i, t in enumerate(tasks, start=1):
                    t["id"] = i
                save_tasks(tasks)
                st.toast("Task deleted!", icon="🗑️")
                st.rerun()

# Progress Bar Effect
if tasks:
    completed_count = sum(1 for t in tasks if t["Status"])
    progress = completed_count / len(tasks)
    st.divider()
    st.write(f"**Overall Progress:** {int(progress * 100)}%")
    st.progress(progress)
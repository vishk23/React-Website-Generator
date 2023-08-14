import streamlit as st
import openai
import subprocess
import os
from pathlib import Path
import psutil


directory = Path.cwd()

api_key = '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'

def get_react_code_from_gpt3(prompt):
    openai.api_key = api_key
    try:
        st.write("prompting")
        response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
            "role": "system",
            "content": "the user will prompt a description of a simple website, or code in another language/framework. You must take the user prompt, and generate react code to satisfy the request. the code must run in only one file. only provide code in your response. make sure your response begins with 'import react'. ensure your code can be directly executed into a react project, so only include code in your response. do not include ''' or '''jsx, be sure to start with just import react . "
            },
            {
            "role": "user",
            "content":  prompt 
            }
        ],
        temperature=1,
        )
        summary = response.choices[0].message.content # type: ignore
        st.write('prompt done')
        st.write(summary)
        print(summary)
        return summary
    except openai.error.APIError as e:
            print(f"APIError occurred: {e}")
            st.warning(f"APIError occurred: {e}")

def save_to_app_js(code):
    st.write("code")
    st.write(Path.cwd())
    path = Path.cwd() / 'chatgpt-react-generator' / 'src'/ 'App.js'
    with open(path, 'w') as file:
        file.write(code)

def run_react_app():
    original_dir = Path.cwd()  # Store the original directory
    react_app_dir = original_dir / 'chatgpt-react-generator'
    
    try:
        os.chdir(react_app_dir)
        subprocess.run(["npm", "start"], check=True)
        st.write('executed')
    except Exception as e:
        st.write(f"An error occurred: {e}")
        st.write('failed')
    finally:
        os.chdir(original_dir)



def stop_processes_from_directory(target_directory):
    current_pid = os.getpid()  # Get the current process ID

    for proc in psutil.process_iter(attrs=['pid', 'cwd']):
        try:
            # Check if the process's current working directory matches the target
            # and the process is not the current process (Streamlit app)
            if proc.info['cwd'] == target_directory and proc.info['pid'] != current_pid:
                psutil.Process(proc.info['pid']).terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


st.title("React App Generator with GPT-3")

user_prompt = st.text_area("Enter a description for your React app:")

if st.button("Generate and Run React App"):
    my_bar = st.progress(0, text='initalizing...')
    directory_path = Path.cwd() / "chatgpt-react-generator"
    stop_processes_from_directory(directory_path)


    my_bar = st.progress(25, text='prompting gpt')
    react_code = get_react_code_from_gpt3(user_prompt)
    my_bar = st.progress(50, text='prompting gpt')
    my_bar = st.progress(75, text='saving result')
    save_to_app_js(react_code)
    my_bar = st.progress(95, text='running website')
    run_react_app()
    my_bar = st.progress(100, text='complete')
    st.balloons()

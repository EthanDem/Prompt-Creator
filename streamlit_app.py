import streamlit as st
import json
import base64

def create_prompt(title, content):
    return {"title": title, "prompt": content}

def create_json_sequence(name, prompts):
    return {"name": name, "prompts": prompts}

def download_link(object_to_download, download_filename, download_link_text):
    if isinstance(object_to_download,str):
        object_to_download = object_to_download.encode()

    b64 = base64.b64encode(object_to_download).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

def app():
    st.title("JSON Prompt Creator")

    st.header("Upload existing JSON file")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        data = json.load(uploaded_file)
    else:
        data = []

    st.header("Add new prompt sequence")
    sequence_name = st.text_input("Enter sequence name")
    number_of_prompts = st.slider("Number of prompts in the sequence", 1, 25)

    prompts = []
    for i in range(number_of_prompts):
        st.subheader(f"Prompt {i+1}")
        title = st.text_input(f"Prompt title {i+1}")
        content = st.text_input(f"Prompt content {i+1}")
        prompts.append(create_prompt(title, content))

    if st.button("Download JSON file"):
        data.append(create_json_sequence(sequence_name, prompts))
        json_data = json.dumps(data, indent=4)
        tmp_download_link = download_link(json_data, 'prompt.json', 'Click here to download your JSON file')
        st.markdown(tmp_download_link, unsafe_allow_html=True)

app()

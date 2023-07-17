from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
import os
import sys
import json
import streamlit as st
from streamlit_chat import message
from langchain.llms import OpenAI
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from google.cloud import aiplatform
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_chat import message
import tkinter
import tkthread
# matplotlib.use('TKAgg')
from langchain import LLMChain, OpenAI, SQLDatabase, SQLDatabaseChain, LLMMathChain
from langchain.agents import AgentExecutor, Tool, ZeroShotAgent, initialize_agent, load_tools
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import SQLDatabaseSequentialChain
from langchain.utilities import SerpAPIWrapper
from google.cloud import bigquery
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms import VertexAI
import os
from google.oauth2 import service_account
matplotlib.use('TKAgg')
from langchain.agents import load_tools
PROJECT_ID = "your project id "

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "service account credential "
credentials = service_account.Credentials.from_service_account_file("service account credentials")
aiplatform.init(project=PROJECT_ID, location="us-central1", credentials=credentials)
st.set_page_config(page_title='Bot')

st.markdown('''
        <div style="display: flex; align-items: center; justify-content: center;">
          <h1 style='text-align: center;'>SufiBot</h1>
          <img src="logo"
               width="40" style="margin-left: 10px;">
        </div>
        ''',unsafe_allow_html=True)

# Initialise session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

def gen_res(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})
    erp_data = pd.read_csv(r"path to csv")
    transactinol_data = pd.read_csv(r"path to csv")
    agent = create_pandas_dataframe_agent(VertexAI(temperature=0), [erp_data, transactinol_data], verbose=True)
    response = agent.run(prompt)
    print('res', response)
    plt.show()
    st.session_state['messages'].append({"role": "assistant", "content": response})
    return response

def clear_text():
    st.session_state["input"] = ""
# container for chat history
if 'something' not in st.session_state:
    st.session_state.something = ''

def submit():
    user_input=st.session_state.input
    output = gen_res(user_input)
    print(output, 'out')
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)
    st.session_state.something = st.session_state.input
    st.session_state.input = ''
def main():
    response_container = st.container()
    # container for text box
    container = st.container()
    with container:
        user_input = st.text_input("Please Enter Your Text Here:", key='input',on_change=submit)
        if user_input:
            pass
            # output = gen_res(user_input, index)
            # print(output, 'out')
            # st.session_state['past'].append(user_input)
            # st.session_state['generated'].append(output)


    clear_button = st.button("Clear Conversation", key="clear", on_click=clear_text)

    if clear_button:
        st.session_state['generated'] = []
        st.session_state['past'] = []
        st.session_state['messages'] = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
                message(st.session_state["generated"][i], key=str(i))


if __name__ == "__main__":
    #index = construct_index("docs")
    main()
    plt.show()

import streamlit as st
import asyncio
from teams.dsa_solver_team import get_dsa_solver_team
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from utils.docker import start_docker_executor,stop_docker_executor, docker
from config.model_clients import get_openai_model_client
from agents.code_executer_agent import get_code_executer_agent
from agents.dsa_problem_solver_agent import get_dsa_solver_agent
from main import get_team


st.title("DSA Solver")
st.write("This is a simple DSA solver application.")

task = st.text_input("Enter your DSA Question here",value='Can you give me a solution to add 2 numbers?')

async def run(team, task):
    try:
        await start_docker_executor()
        async for message in team.run_stream(task = task):
            print('='*50)
            if isinstance(message, TextMessage):
                print(msg:= f"{message.source}: {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:=f'Task Result: {message.stop_reason}')
                yield msg

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await stop_docker_executor()




if st.button("Solve"):
    st.write('Solving your question...')

    
    task = task

    async def collect_messages():
        team  = await get_team()
        async for msg in run(team, task):
            # if isinstance(msg, str):
            if msg.startswith('user'):
                with st.chat_message('user',avatar='👤'):
                    st.markdown(msg)
            elif msg.startswith('dsa_solver'):
                with st.chat_message('ProblemSolverExpert',avatar='🧑🏻‍💻') :
                    st.markdown(msg)
            elif msg.startswith('code_executor'):
                with st.chat_message('CodeExecutorAgent',avatar='🤖'):
                    st.markdown(msg)
            else:
                st.markdown(msg)

    asyncio.run(collect_messages())
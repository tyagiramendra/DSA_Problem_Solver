from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from config import constants as co
from config.model_clients import get_openai_model_client
from agents.code_executer_agent import get_code_executer_agent
from agents.dsa_problem_solver_agent import get_dsa_solver_agent
from teams.dsa_solver_team import get_dsa_solver_team
from utils.docker import start_docker_executor,stop_docker_executor, docker


async def get_team():
    model_client = get_openai_model_client()
    code_executer_agent = get_code_executer_agent(docker)
    dsa_solver_agent = get_dsa_solver_agent(model_client)
    team = get_dsa_solver_team(dsa_solver_agent,code_executer_agent)
    return team

async def main(task,team):
    
    try:
        await start_docker_executor()
        team = await get_team()
        async for message in team.run_stream(task = task):
            print('='*100)
            if isinstance(message, TextMessage):
                print("Message from:", message.source)
                print("Content:", message.content)
            elif isinstance(message, TaskResult):
                print (message.stop_reason)
            print('='*100)
    except Exception as e:
        print(f"An Error Occurred: {e}")
    finally:
        await stop_docker_executor()
        print("Code executor stopped.")
    


if __name__ == "__main__":
    import asyncio
    task = "Write a program to add two numbers."
    asyncio.run(main(task))
    

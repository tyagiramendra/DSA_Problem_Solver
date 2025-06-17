from autogen_agentchat.agents import AssistantAgent, CodeExecutorAgent

def get_code_executer_agent(docker):
    
    code_executor_agent = CodeExecutorAgent("code_executor", code_executor=docker)

    return code_executor_agent
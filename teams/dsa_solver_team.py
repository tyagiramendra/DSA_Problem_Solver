from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from config import constants as co

term_condition = TextMentionTermination(co.TERMINATION_TEXT)

def get_dsa_solver_team(dsa_solver_agent,code_executer_agent):
    return RoundRobinGroupChat(participants=[dsa_solver_agent,code_executer_agent],max_turns=co.MAX_TURN, termination_condition=term_condition)
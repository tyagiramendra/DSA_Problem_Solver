# DSA Solver

This project aims to create an AI agent capable of solving Data Structures and Algorithms (DSA) problems.

## Features

- **Problem Understanding:** The agent can parse and understand DSA problem statements.
- **Solution Generation:** It can generate code solutions in various programming languages (currently Python).
- **Test Case Generation:** The agent can generate test cases for the given problem.
- **Solution Verification:** It can verify the correctness of the generated solution against test cases.

## Technologies Used

- **AutoGen:** For orchestrating the multi-agent system.
- **Large Language Models (LLMs):** For understanding problems, generating code, and reasoning.
- **Python:** The primary programming language for development and solution generation.

## Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:tyagiramendra/DSA_Problem_Solver.git
   cd DSA_Problem_Solver
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys:**
   Create a `.env` file in the root directory and add your API keys for the LLMs you want to use. For example:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Run the main script:**
   ```bash
   streamlit run app.py
   ```

2. **Provide the DSA problem:**
   The script will prompt you to enter the DSA problem statement.

3. **Observe the agent's process:**
   The agents will work together to understand the problem, generate a solution, and verify it.

## Project Structure

```
DSA_Problem_Solver/
├── agents/
│   ├── code_executer_agent.py
│   ├── dsa_problem_solver_agent.py
├── teams/
│   ├── dsa_solver_team.py
├── utils/
│   └── docker.py
├── config/
│   └── constants.py
│   └── model_clients.py
├── main.py
├── app.py
├── requirements.txt
└── README.md

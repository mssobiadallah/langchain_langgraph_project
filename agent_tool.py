from langchain_classic.hub import hub
from langchain_classic.agents.agent import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_deepseek import ChatDeepSeek
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from langsmith import Client
import os

load_dotenv()
LANGSMITH_API_KEY = os.environ.get("LANGSMITH_API_KEY")
client = Client(api_key=LANGSMITH_API_KEY)
react_prompt = client.pull_prompt("hwchase17/react", include_model=True)



tools =[TavilySearch()]

llm =ChatDeepSeek(temperature= 0 , model='deepseek-chat')

agent =create_react_agent(llm= llm ,tools =tools ,prompt= react_prompt)

agent_executor =AgentExecutor(agent=agent ,tools= tools ,verbose= True)


chain =agent_executor


def main():
    result  = chain.invoke(input= {
        "input" :"search for 3 job posting for an AI engineer "
    })
    print(result)



if __name__ == "__main__":
    main()
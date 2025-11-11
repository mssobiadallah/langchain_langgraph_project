from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_classic.agents.agent import AgentExecutor
from prompt import react_prompt
from schema import AgentResponse
from langchain_classic.agents.react.agent import create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from langsmith import Client
import os


load_dotenv()
LANGSMITH_API_KEY = os.environ.get("LANGSMITH_API_KEY")
client = Client(api_key=LANGSMITH_API_KEY)

output_parser = PydanticOutputParser(pydantic_object =AgentResponse)

react_prompt_with_format =PromptTemplate(
    template= react_prompt ,
    input_variables= ['input','agent_scratchpad',"tool_names"]).partial(
    format_instructions = output_parser.get_format_instructions()
    )
tools =[TavilySearch()]

llm =ChatDeepSeek(temperature= 0 , model='deepseek-chat')

agent =create_react_agent(llm= llm ,tools =tools ,prompt= react_prompt_with_format)

agent_executor =AgentExecutor(agent=agent ,tools= tools ,verbose= True)
extract_output = RunnableLambda(lambda x : x['output'])
parse_output = RunnableLambda(lambda x : output_parser.parse(x))



chain =agent_executor | extract_output | parse_output


def main():
    result  = chain.invoke(input= {
        "input" :"search for 3 job posting for an AI engineer "
    })
    print(result)



if __name__ == "__main__":
    main()
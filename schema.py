from typing import List
from pydantic import BaseModel,Field

class source(BaseModel):
    """schema for a sourse used by the agent 
    """
    url:str =Field (description= "The URL of the source")

class AgentResponse(BaseModel):
    """ schema for the agent response with answer & sourses 
    """
    answer : str = Field(description= "the agent that answer the query")
    sources: List[source] = Field(
        default_factory=List,
        description= "List of sources used to gereate the answer"
    )
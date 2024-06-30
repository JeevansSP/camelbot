from langchain_openai import ChatOpenAI
from langchain.chains.conversation.memory import (
    ConversationBufferMemory,
)
from langchain.agents import OpenAIFunctionsAgent
from langchain.prompts import MessagesPlaceholder
from langchain.agents import AgentExecutor
from typing import List, Optional, Callable
from langchain.schema import SystemMessage

from langchain.tools import Tool


class BaseAgent:
    def __init__(
        self,
        system_messge: SystemMessage,
        tools: List[Callable],
        base_url: str,
        api_key: str,
        history: Optional[bool] = False
    ):
        """
        Initializes an instance of the BaseAgent class.

        Args:
            system_messge (SystemMessage): The system message to be used in the conversation prompt.
            tools (List[Callable]): A list of tools (callables) to be used in the agent.
            history (Optional[bool], optional): Flag indicating whether to enable conversation history. Defaults to False.
        """
        self.tools = tools
        self.llm = ChatOpenAI(
            base_url=base_url,
            api_key=api_key,
            temperature=1,
            model="gpt-4-turbo",
        )

         # For mathematical calculations

        if history:
            self.agent_kwargs = {
                "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")]
            }

            memory = ConversationBufferMemory(
                llm=self.llm,
                memory_key="memory",
                return_messages=True,
            )

            self.prompt = OpenAIFunctionsAgent.create_prompt(
                system_message=system_messge,
                extra_prompt_messages=[MessagesPlaceholder(variable_name="memory")],
            )
        else:
            memory = None
            self.prompt = OpenAIFunctionsAgent.create_prompt(
                system_message=system_messge,
            )

        agent = OpenAIFunctionsAgent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt,
        )
        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            # verbose=True,
            memory=memory,
            max_iterations=20,
            max_execution_time=520,
            handle_parsing_errors=True,
        )

    def run(self, query: str) -> str:
        """
        Executes the given prompt and returns the response.

        Args:
            query (str): The prompt query.

        Returns:
            str: The prompt response.
        """
        response = self.agent_executor.invoke(query)
        return response["output"]

    async def arun(self, query: str):
        """async version of the `run` func"""
        response = await self.agent_executor.arun(query)
        return response["output"]



from LLM.BaseChain import BaseAgent
from Guidelines import guidelines
from langchain_experimental.tools import PythonREPLTool
from langchain.tools import Tool
from langchain.schema import SystemMessage

class ChatAgent(BaseAgent):
    def __init__(self, base_url, api_key):
        
        system_message = SystemMessage(f'''
        You are a highly qualified financial auditor. 
        
        The following guidelines are provided for you to audit the financial data:
        {guidelines}
        ''')
        
        python_repl = PythonREPLTool()

        python_reply_tool = Tool.from_function(
            func=python_repl,
            name=python_repl.name,
            description=python_repl.description,
        )
        
        super().__init__(system_messge=system_message, base_url=base_url, api_key=api_key, history=True, tools=[python_reply_tool])
        
        

        
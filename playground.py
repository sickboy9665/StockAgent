
from agno.agent import Agent
import agno.api
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
from agno.models.groq import Groq
from agno.storage.agent.sqlite import SqliteAgentStorage
import os
import agno
from agno.playground import Playground, serve_playground_app
# Load environment variables from .env file
load_dotenv()
groqkey = os.getenv("GROQ_API_KEY")
agno.api=os.getenv("AGNO_API_KEY")
agent_storage: str = "tmp/agents.db"
## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="deepseek-r1-distill-llama-70b",api_key=groqkey),
    tools=[DuckDuckGoTools()],
    instructions=["Alway include sources"],
    show_tool_calls=True,
    markdown=True,
    storage=SqliteAgentStorage(table_name="web_agent", db_file=agent_storage),
)

## Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="deepseek-r1-distill-llama-70b",api_key=groqkey),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
    storage=SqliteAgentStorage(table_name="finance_agent", db_file=agent_storage),
)

app=Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)
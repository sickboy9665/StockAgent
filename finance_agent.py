
# from phi.agent import Agent
# from phi.model.google import Gemini
# from phi.tools.yfinance import YFinanceTools
# from phi.tools.duckduckgo import DuckDuckGo




# ## web search agent
# web_search_agent=Agent(
#     name="Web Search Agent",
#     role="Search the web for the information",
#     model=Gemini(id="gemini-1.5-flash",api_key=geminikey),
#     tools=[DuckDuckGo()],
#     instructions=["Alway include sources"],
#     show_tools_calls=True,
#     markdown=True,

# )

# ## Financial agent
# finance_agent=Agent(
#     name="Finance AI Agent",
#     model=Gemini(id="gemini-1.5-flash", api_key=geminikey),
#     tools=[
#         YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
#                       company_news=True),
#     ],
#     instructions=["Use tables to display the data"],
#     show_tool_calls=True,
#     markdown=True,

# )

# multi_ai_agent=Agent(
#     team=[web_search_agent,finance_agent],
#     instructions=["Always include sources","Use table to display the data"],
#     model = Gemini(id="gemini-1.5-flash", api_key=geminikey),
#     show_tool_calls=True,
#     markdown=True,
# )

# multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream=True,
#                              show_full_reasoning=True )


from agno.agent import Agent
# from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.models.google import Gemini
import os
from dotenv import load_dotenv
load_dotenv()
geminikey = os.getenv("GOOGLE_GEMINI_KEY")

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Gemini(id="gemini-2.0-flash-exp",api_key=geminikey),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Gemini(id="gemini-2.0-flash-exp",api_key=geminikey),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Gemini(id="gemini-2.0-flash-exp",api_key=geminikey),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Summarize analyst recommendation and share the latest news for NVDA and also give me current stock price for the same.",stream=True,
                          show_full_reasoning=True)
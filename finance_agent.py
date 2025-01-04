import os
from dotenv import load_dotenv
load_dotenv()
geminikey = os.getenv("GOOGLE_GEMINI_KEY")
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo




## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Gemini(id="gemini-1.5-flash",api_key=geminikey),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)

## Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Gemini(id="gemini-1.5-flash", api_key=geminikey),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    instructions=["Always include sources","Use table to display the data"],
    model = Gemini(id="gemini-1.5-flash", api_key=geminikey),
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream=True)





## SAMPLE TESTING GEMINI RESPONSE

# from dotenv import load_dotenv

# load_dotenv()
# import os
# from phi.agent import Agent, RunResponse
# from phi.model.google import Gemini
# geminikey = os.getenv("GOOGLE_GEMINI_KEY")
# agent = Agent(
#     model=Gemini(id="gemini-1.5-flash", api_key=geminikey),
#     markdown=True,
# )

# # Get the response in a variable
# # run: RunResponse = agent.run("Share a 2 sentence horror story.")
# # print(run.content)

# # Print the response in the terminal
# agent.print_response("Share a 2 sentence horror story.")

import os
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_openai import OpenAI
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
load_dotenv()

my_APIkey = os.environ["OPENAI_API_KEY"]

#Database INFO
userName = "postgres"
password = "984138o35o"
host = "localhost"
port = "5432"
mydatabase = "master"
pg_uri = f"postgresql+psycopg2://{userName}:{password}@{host}:{port}/{mydatabase}"
db = SQLDatabase.from_uri(pg_uri)

#Loading model
llm = OpenAI(model = "gpt-3.5-turbo-0613")
print(db.get_usable_table_names()) # Printing namesto see if we loaded right 
llm = OpenAI(temperature=0, verbose=True, openai_api_key=my_APIkey)

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent_executor.run(
    "who is the least paid employee"
)
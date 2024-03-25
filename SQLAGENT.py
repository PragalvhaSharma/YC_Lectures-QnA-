import os
from llama_index.core import SQLDatabase
from sqlalchemy import create_engine, text
from llama_index.llms.openai import OpenAI
from llama_index.core.query_engine import NLSQLTableQueryEngine
from dotenv import load_dotenv
load_dotenv()

my_API_key = os.environ["OPENAI_API_KEY"]
llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo")

userName = "postgres"
password = "984138o35o"
host = "localhost"
port = "5432"
mydatabase = "master"
pg_uri = f"postgresql+psycopg2://{userName}:{password}@{host}:{port}/{mydatabase}"
sql_engine = create_engine(pg_uri)


sql_database = SQLDatabase(sql_engine)
print(list(sql_database._all_tables))

Sqlquery_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,llm=llm
)
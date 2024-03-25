# For the CSV FILE
from llama_index.core import PromptTemplate

#instructions to the language model
instruction_LLM = """
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression."""

#a question to the language model.
new_prompt = PromptTemplate(
    """\
    Your name is Hermes.
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    
    Query: {query_str}

    Expression: """
)



contextForLlm = "Your name is Hermes. Your primary role is to assist users by providing accurate information about their business"

#MISSING ---  set of few shot examples to help the language model generate a better response,

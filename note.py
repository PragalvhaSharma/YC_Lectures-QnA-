
#wrapper
from llama_index.tools import FunctionTool
import os

note_file = "/Users/pragalvhasharma/Downloads/Prag GO to Documents/Comp Sci/MY Projects/LLamaIndexRag Agent/env/Data/notes.txt"

#Can define any type of function
def save_note(note):
    #If notefile doesnt exist
    if not os.path.exists(note_file):
        open(note_file, "w")
    with open(note_file, "a") as f:
        f.writelines([note + "\n"])
    return "note saved"

#Creating engine-- Parmeters[   ]
note_engine = FunctionTool.from_defaults(
    fn = save_note,
    name = "note_saver",
    # Description tells what the tool does so the model can pick between different tools depending on the situation
    description = "Saves text based note to a file for user",
)
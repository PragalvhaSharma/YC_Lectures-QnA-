# Using a Vector Store Index for unstructured data. 
import os
from dotenv import load_dotenv
load_dotenv()

#FAISS is a vectorstore Index. They are for Quick Prototyping Efficient for rapid prototyping with focused capabilities. Databases are for scailing (enterprise)
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage

#General Reader from llamaindex. There are many for different usecases -- https://llamahub.ai/?tab=all .
# SimpleDirectoryreader -- Vectorizes the entire directory for any type of data
from llama_index.core import SimpleDirectoryReader

pdfPath = "/Users/pragalvhasharma/Downloads/Prag GO to Documents/Comp Sci/MY Projects/Yc-Agent-Opensource/YC_Lectures-QnA-/Data/lectures.pdf"


#Creating a function to get vector store index
def get_index(data, index_name):
    index = None
    #Check if it exists
    if not os.path.exists(index_name):
        print("Building index:", index_name)

        #Creating index
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        #Storing the index in a folder
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
            )

    return index

reader = SimpleDirectoryReader(
    input_files=[pdfPath]
)
lecturesPDF = reader.load_data()

#Call function 
startup_index = get_index(lecturesPDF, "Yc-Embeddings")

#Create engine for agent (.query() to test)
startup_engine = startup_index.as_query_engine()
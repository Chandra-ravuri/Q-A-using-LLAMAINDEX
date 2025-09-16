pip install llama-index
from llama_index.readers import SimpleWebPageReader
from llama_index import VectorStoreIndex
import os
from dotenv import load_dotenv

# Example: Load a webpage using llama_index's SimpleWebPageReader
SimpleWebPageReader = download_loader("SimpleWebPageReader")

load_dotenv()

def main(url: str)-> None:
    document = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    query_engine = VectorStoreIndex.from_documents(documents=document)
    response=query_engine.query("what is KNN")
    print(response)
# Example usage:
if __name__ == "__main__":
    main("https://www.geeksforgeeks.org/machine-learning/k-nearest-neighbours/")
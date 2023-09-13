from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain import HuggingFaceHub
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
import sys
#from langchain import FAISS

# Page to skip
pages_to_skip = [2, 3]
# Example: text to exclude
text_to_exclude = [
    "Learn English through story",
    "English Short Stories for Beginners",
    "By: learnenglish-new.com",
    "By: learnenglish -new.com",
    "The source of the story: newsinlevels.com",
    "Brought the story from: learnenglish-new.com",
    "If you want to read this book online: newsinlevels.com",
    "If you want to download the book: learnenglish-new.com",
    "Robinson Crusoe level-1",
    "Robinson Crusoe - Level 1",
    "Brought the story from: learnenglish -new.com",
    "If you want to download the book:    learnenglish -new.com"
]

def main():
    load_dotenv()
    reader = PdfReader("robinson-crusoe.pdf")
    text = ""
    for page_number, page in enumerate(reader.pages, start=1):
        if page_number in pages_to_skip:
            continue  # Skip the page if it is pages_to_skip list
        #text += page.extract_text()
        page_text = page.extract_text()
        # Verify if text is not empty o composed by only spaces
        if page_text.strip():
            # Exclude undesired lines from the text
            for line_to_exclude in text_to_exclude:
                page_text = page_text.replace(line_to_exclude, "")
            
            # Add the filtered page text to the variable 'text'
            text += page_text

    text = "\n".join(line for line in text.splitlines() if line.strip())
    # spilit ito chuncks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len)
    chunks = text_splitter.split_text(text)
    #for chunk in chunks:
    #    print(chunk)
    #    print("--------------------------------------------------------------------------------")

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_texts(chunks, embeddings)
    #db = FAISS.from_texts(chunks, embeddings)
    while True:
        query = input("you> ")
        if query:
            if query.lower() in ["exit", "quit", "q"]:
                print('Exiting')
                sys.exit()            
            docs = db.similarity_search(query, k=5)
            #print(docs)
            #for doc in docs:
            #    print(doc.page_content)
            #    print("--------------------------------------------------------------------------------")
            llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":5, "max_length":64})
            #llm = HuggingFaceHub(repo_id="meta-llama/Llama-2-7b", model_kwargs={"temperature":5, "max_length":64})
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=docs, question=query)
            print("chatpdf> " + response)

if __name__ == '__main__':
    main()

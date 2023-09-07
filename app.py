from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain import HuggingFaceHub
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from sentence_transformers import SentenceTransformer, util
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

def main():
    load_dotenv()
    reader = PdfReader("robinson-crusoe.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    # spilit ito chuncks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len)
    chunks = text_splitter.split_text(text)

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_texts(chunks, embeddings)
    while True:
        query = input("Ask Question about your PDF: ")
        if query:
            docs = db.similarity_search(query, k=5)
            llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":5, "max_length":64})
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=docs, question=query)
            print(response)

if __name__ == '__main__':
    main()

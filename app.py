from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain import HuggingFaceHub
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
import chromadb
from sentence_transformers import SentenceTransformer, util
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

def main():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    load_dotenv()
    reader = PdfReader("robinson-crusoe.pdf")
    number_of_pages = len(reader.pages)
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
    for chunk in chunks:
        print("################################################################################")
        print(chunk)

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_texts(chunks, embeddings)
    while True:
        query = input("Ask Question about your PDF: ")
        if query:
            docs = db.similarity_search(query, k=5)
            #print("Retrieved docs:")
            #for doc in docs:
            #    print(doc)
            #    print()
            llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":5, "max_length":64})
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=docs, question=query)
            print(response)




#db.persist()
#embeddings = model.encode(chunks, convert_to_tensor=True)
#db = chromadb.create("embedding_db")
#for i, embedding in enumerate(embeddings):
#    db.put(str(i), embedding.numpy())
#db.close()
#database_path = "my_embedding_db"
#embedding_db = EmbeddingDB(database_path, create=True)
#for chunk in chunks:
#    embedding = calculate_embedding(chunk)  # Sostituisci con il tuo metodo per calcolare l'embedding
#    embedding_db.add_embedding(embedding)
#embedding_db.close()



#embeddings = HuggingFaceEmbeddings()
#knowledge_base = FAISS.from_texts(chunks, embeddings)
#while True:
#    query = input("Ask Question about your PDF: ")
#    if query:
#        docs = knowledge_base.similarity_search(query)
#        llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":5, "max_length":64})
#        chain = load_qa_chain(llm,chain_type="stuff")
#        response = chain.run(input_documents=docs,question=query)
#        print(response)

if __name__ == '__main__':
    main()

class Database:
    def get_context(self, question):
        raise NotImplementedError("Subclasses must implement the get_context method")

    def store(self, chunks, embeddings):
        raise NotImplementedError("Subclasses must implement the store method")
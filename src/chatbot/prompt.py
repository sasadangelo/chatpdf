from langchain.prompts import PromptTemplate

class Prompt:
    PROMPT_TEMPLATE = """
    Use the following pieces of context enclosed by triple backquotes to answer the question at the end.
    
    Context:
    ```
    {context}
    ```
    
    Question: [][][][]{question}[][][][]
    
    Answer:
    """

    @classmethod
    def get_prompt(cls, context, question):
        if context is None:
            return question
        else:
            user_input_w_context = PromptTemplate(
                template=Prompt.PROMPT_TEMPLATE,
                input_variables=["context", "question"]) \
                .format(
                    context=context, question=question)
            #user_input_w_context = cls.PROMPT_TEMPLATE.format(context=context, question=question)
            return user_input_w_context

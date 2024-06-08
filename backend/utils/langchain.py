from langchain.prompts import ChatPromptTemplate
from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import (
    RunnableLambda,
    RunnablePassthrough,
    RunnableParallel,
)


class MyLangChain:
    def generate_prompts_chain(self, base_retriever):
        template = """You are an AI assistant and expert.

        Your will have to generate {num_of_prompts_to_generate} prompts from the provided context and prompt .

        Use the below format to output the prompts.

        example:
        ["prompt1", "prompt2", "prompt3"]


        The generated prompt must satisfy the rules given below:
        0. The generated prompted should only contain the prompt
        1.The promp should be clear, concise and simple eglish.
        2.The prompt shouldn;t be outisde of the given context.
        4.The prompt must be reasonable and must be understood and responded by humans.
        5.Do no use phrases like 'As an AI model' 'based on your input', 'provided context',etc in the prompt
        6.The prompt should not contain more than 15 words, make of use of abbreviation wherever possible.
            
        ### CONTEXT
        {context}

        ### User Prompt
        User Prompt: {user_prompt}
        """

        prompt = ChatPromptTemplate.from_template(template)

        primary_qa_llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

        retriever = RunnableParallel(
            {
                "context": itemgetter("user_prompt") | base_retriever,
                "user_prompt": itemgetter("user_prompt"),
                "num_of_prompts_to_generate": itemgetter("num_of_prompts_to_generate"),
            }
        )

        retrieval_augmented_qa_chain = retriever | {
            "response": prompt | primary_qa_llm,
            "context": itemgetter("context"),
        }
        return retrieval_augmented_qa_chain
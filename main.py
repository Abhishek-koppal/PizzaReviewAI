from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriver

model = OllamaLLM(model="llama3.2")

template = """
you are expert in pizza reviews

here are some reviews:
{reviews}

here are the questions:
{questions}

"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n------------------------------------")
    question = input("Enter a question (or 'q' to quit): ")
    print("\n\n")
    if question == 'q':
        break
    
    reviews = retriver.invoke(question)
    results = chain.invoke({
    "reviews": reviews, "questions":question})

    print(results)
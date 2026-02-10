#app.py
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
import gradio as gr

hf_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", encode_kwargs={"normalize_embeddings": True})
vector_store = FAISS.load_local(
    "gita_faiss_index",
    hf_embeddings,
    allow_dangerous_deserialization=True
)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
prompt = PromptTemplate(
    template="""
    You are a spiritual guide who explains concepts logically using the Bhagavad Gita.

    Bhagavad Gita relevant context:
    {verses}

    user aked question: {question}

    Task:
    - Answer the user's question using ONLY the meaning of the context above.
    - If question is out of the relevant context, then just say "I couldn’t find a relevant teaching in the Bhagavad Gita for this question."
    - note that verses or context not provided by the user instead internal system fetching it from the Bhagavad Gita
    - dont say "Based on the context or verse you’ve provided."
    - Avoid blind faith; instead, give a thoughtful and rational explanation.
    - If appropriate, cite chapter and verse numbers naturally.
    """,
    input_variables = ['question', 'verses']
)
def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

def answer_question(question):
    parallel_chain = RunnableParallel({
    'verses': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
    })
    parser = StrOutputParser()
    main_chain = parallel_chain | prompt | model | parser
    response = main_chain.invoke(question)
    return response

demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(
        label="Ask a question",
        placeholder="Ask a life or spiritual question...",
        lines=2
    ),
    outputs=gr.Textbox(
        label="Answer",
        lines=12,          # height of output box
        max_lines=20       # optional: allow expansion
    ),
    flagging_mode="never",
    title="Bhagavad Gita – Practical Life Guidance",
    description="A simple chatbot that explains the Bhagavad Gita in a clear and practical way."
)


if __name__ == "__main__":
    demo.launch()

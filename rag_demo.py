import os
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document


# 1. 加载文档
# 这里用一个简单的文本文件演示，实际可替换为 .txt / .md / .pdf 等

def load_documents(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return [Document(page_content=text, metadata={"source": file_path})]


# 2. 分割文本

def split_documents(docs, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    return splitter.split_documents(docs)


# 3. 向量化 + 存入向量库

def build_vector_store(chunks):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com"
    )
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store


# 4. 检索相关片段

def retrieve_context(vector_store, query, k=3):
    docs = vector_store.similarity_search(query, k=k)
    return docs


# 5. 组装 prompt，并调用大模型

def call_llm(prompt: str) -> str:
    llm = ChatOpenAI(
        model="deepseek-chat",
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com"
    )
    result = llm.invoke(prompt)
    return result.content


# 6. 主流程

def rag_answer(file_path: str, question: str):
    # 加载
    docs = load_documents(file_path)
    # 分割
    chunks = split_documents(docs)
    # 向量化并存库
    vector_store = build_vector_store(chunks)
    # 检索
    related_docs = retrieve_context(vector_store, question, k=3)

    context = "\n\n".join([doc.page_content for doc in related_docs])

    prompt = f"""
你是一个知识问答助手。请基于以下参考资料回答用户问题。

参考资料：
{context}

用户问题：
{question}

请用中文回答，并仅基于参考资料进行回答。
"""

    answer = call_llm(prompt)
    return answer


if __name__ == "__main__":
    file_path = os.path.join("data", "sample.txt")

    # 如果没有 sample.txt，先创建一个示例文档
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("""
Python 是一种高级编程语言，适合学习编程入门。
它具有语法简洁、易读、适合自动化脚本和数据分析。
LangChain 是一个用于构建大语言模型应用的框架。
它可以帮助开发者把检索、调用模型、处理上下文等能力串起来。
RAG 是 Retrieval-Augmented Generation 的缩写，意思是“检索增强生成”。
它通常先从知识库中找相关资料，再把这些资料交给大模型回答。
""".strip())

    q = "LangChain 是什么？"
    result = rag_answer(file_path, q)
    print(result)

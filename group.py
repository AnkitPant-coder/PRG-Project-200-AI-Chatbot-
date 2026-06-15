import chromadb
from pypdf import PdfReader

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="knowledge_base"
)


def chunk_text(text, chunk_size=1000):

    return [
        text[i:i + chunk_size]
        for i in range(
            0,
            len(text),
            chunk_size
        )
    ]


def add_document(name, text):

    try:
        delete_document(name)
    except:
        pass

    chunks = chunk_text(text)

    ids = [
        f"{name}_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        documents=chunks,
        ids=ids
    )

from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from dotenv import load_dotenv
from getpass import getpass
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os

# Load environment variables
load_dotenv()

if not os.getenv("PINECONE_API_KEY"):
    PINECONE_API_KEY = getpass("Enter your Pinecone API key: ")
    os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
else:
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone using the Pinecone class
pc = Pinecone(api_key=PINECONE_API_KEY)

# Define index name and dimension
index_name = "medicalbot"
dimension = 384  # Ensure this matches your embedding model's output size

# Check if the index exists, else create it
existing_indexes = pc.list_indexes()
if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    print(f"Index '{index_name}' created.")
else:
    print(f"Index '{index_name}' already exists.")

# Extract and preprocess documents
extracted_data = load_pdf_file(data='Data/')
text_chunks = text_split(extracted_data)

# Download embeddings
embeddings = download_hugging_face_embeddings()

# Load the index
index = pc.Index(index_name)

# Add data to the Pinecone vector store
vector_store = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,  # Ensure the correct index name is used here
    embedding=embeddings
)

print("Data added to the Pinecone Vector Store successfully!")

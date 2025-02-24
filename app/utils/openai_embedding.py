from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI()

def get_embedding(text: str) -> list[float]:
    """
    Get an embedding vector for a text string using OpenAI's text-embedding-3-large model.
    
    Args:
        text (str): The text to embed
        
    Returns:
        list[float]: The embedding vector with 1536 dimensions
    """
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-large"
    )
    
    # Extract the embedding vector from the response
    embedding = response.data[0].embedding
    
    return embedding    
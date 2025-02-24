from app.config.settings import settings
from app.database.std_sql_db import (
    get_connection,
    search_similar_chunks
)

from openai import OpenAI

client = OpenAI(api_key=settings.openai.api_key)

def format_context(similar_chunks):
    """Format the chunks into a single context string"""
    context_parts = []
    for chunk in similar_chunks:
        text = chunk["text"]
        metadata = chunk["metadata"]
        source = metadata.get("filename", "Unknown")
        title = metadata.get("title", "Untitled")
        context_parts.append(
            f"Content: {text}\n"
            f"Source: {source}\n"
            f"Title: {title}\n"
            f"Similarity: {chunk['similarity']:.3f}\n"
        )
    return "\n".join(context_parts)

def get_chat_response(query: str, context: str) -> str:
    """Get a chat completion from OpenAI"""
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that answers questions based on the provided context. "
                      "If you cannot find the answer in the context, say so clearly."
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {query}"
        }
    ]
    
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=messages,
        temperature=0.7,
    )
    
    return response.choices[0].message.content




query_text = "what safety training will I need to use cns?"
conn = get_connection()
similar_chunks = search_similar_chunks(conn, query_text)

context = format_context(similar_chunks)
print("\nRelevant Context:")
print(context)

response = get_chat_response(query_text, context)
print("\nAI Response:")
print(response)
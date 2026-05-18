from sentence_transformers import SentenceTransformer
import numpy as np
from src.config.settings import EMBEDDING_MODEL

# Load embedding model
model = SentenceTransformer(EMBEDDING_MODEL)

def get_embedding(text: str) -> np.ndarray:
    """Generates embedding for the given text."""
    if not text:
        return np.zeros(384) # Assuming all-MiniLM-L6-v2 size
    return model.encode(text)

def get_similarity(embedding1: np.ndarray, embedding2: np.ndarray) -> float:
    """Computes cosine similarity between two embeddings."""
    from sklearn.metrics.pairwise import cosine_similarity
    if embedding1.ndim == 1:
        embedding1 = embedding1.reshape(1, -1)
    if embedding2.ndim == 1:
        embedding2 = embedding2.reshape(1, -1)
    
    return cosine_similarity(embedding1, embedding2)[0][0]

import numpy as np



def cosine_similarity(vec1, vec2):
    # Ensure the vectors are non-zero
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return 0.0  # Avoid division by zero
    
    # Calculate cosine similarity
    cosine_sim = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    cosine_round = round(cosine_sim, 2)
    return cosine_round
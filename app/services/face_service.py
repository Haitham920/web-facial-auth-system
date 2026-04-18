import face_recognition
import numpy as np

def extract_embedding(image):
    encodings = face_recognition.face_encodings(image, model="hog")
    if len(encodings) == 0:
        return None
    return encodings[0]

def compare_faces(known_embeddings, test_embedding, threshold=0.6):
    if len(known_embeddings) == 0:
        return False, None

    distances = face_recognition.face_distance(known_embeddings, test_embedding)
    best_match = min(distances)

    return best_match < threshold, float(best_match)
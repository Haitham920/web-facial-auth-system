from database import get_db
import numpy as np

def store_embedding(user_id, embedding):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO faces (user_id, embedding) VALUES (?, ?)",
        (user_id, embedding.tobytes())
    )
    conn.commit()
    conn.close()

def get_user_embeddings(username):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    if not user:
        return None, []

    user_id = user[0]

    cursor.execute("SELECT embedding FROM faces WHERE user_id=?", (user_id,))
    rows = cursor.fetchall()

    embeddings = [np.frombuffer(row[0]) for row in rows]

    conn.close()
    return user_id, embeddings

def log_attempt(username, outcome, score):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO logs (username, outcome, score) VALUES (?, ?, ?)",
        (username, outcome, score)
    )

    conn.commit()
    conn.close()
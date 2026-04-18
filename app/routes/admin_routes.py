from flask import Blueprint, request, render_template
import cv2
from database import get_db
from services.face_service import extract_embedding
from services.auth_service import store_embedding

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/enroll", methods=["GET", "POST"])
def enroll():
    if request.method == "POST":
        username = request.form["username"]

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, role) VALUES (?, ?)", (username, "user"))
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()

        cap = cv2.VideoCapture(0)
        frame = None

        while True:
            ret, temp_frame = cap.read()
            if not ret:
                break

            cv2.imshow("Enrollment - Press SPACE to capture", temp_frame)

            if cv2.waitKey(1) & 0xFF == 32:
                frame = temp_frame
                break

        cap.release()
        cv2.destroyAllWindows()

        if frame is not None:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            embedding = extract_embedding(rgb)
            
            if embedding is not None:
                store_embedding(user_id, embedding)
                return "User enrolled successfully"
        
        return "Enrollment failed: No face captured"

    return render_template("enroll.html")
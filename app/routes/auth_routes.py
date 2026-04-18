from flask import Blueprint, request, render_template, redirect, session
import cv2
from services.face_service import extract_embedding, compare_faces
from services.auth_service import get_user_embeddings, log_attempt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET"])
def login_page():
    return render_template("login.html")

@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    cap = cv2.VideoCapture(0)
    frame = None

    while True:
        ret, temp_frame = cap.read()
        if not ret:
            break

        cv2.imshow("Camera - Press SPACE to capture", temp_frame)
        
        # Check if SPACE (32) is pressed
        if cv2.waitKey(1) & 0xFF == 32:
            frame = temp_frame
            break

    cap.release()
    cv2.destroyAllWindows()

    if frame is None:
        return "Failed to capture image"

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    embedding = extract_embedding(rgb)

    if embedding is None:
        print("❌ No face detected")
        return "No face detected"

    user_id, known_embeddings = get_user_embeddings(username)
    match, score = compare_faces(known_embeddings, embedding)

    if match:
        session["user"] = username
        log_attempt(username, "success", score)
        return redirect("/dashboard")
    match, score = compare_faces(known_embeddings, embedding)

    print("Match:", match)
    print("Score:", score)
    print("Stored embeddings:", len(known_embeddings))
    log_attempt(username, "failure", score)
    return "Authentication failed"
# from flask import Flask, render_template, request, jsonify
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
# from flask_cors import CORS
# from werkzeug.utils import secure_filename
# import os, json, base64
# from flask_sqlalchemy import SQLAlchemy
# from groq import Groq
# import pandas as pd



# app = Flask(__name__)
# CORS(app)  # Allows frontend requests
# app.config["JWT_SECRET_KEY"] = "your_secret_key"  # Change this to a secure key
# jwt = JWTManager(app)

# # Dummy user database
# USER_CREDENTIALS = {"username": "admin", "password": "password"}
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://whatsapp_bot_ph2f_user:wpMzB8LI6XupW62hTY9MIdWo2qnJpKoZ@dpg-cv340tgfnakc738hhj2g-a.oregon-postgres.render.com/whatsapp_bot_ph2f'
# #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:deep@localhost/test1'

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# db = SQLAlchemy(app)



# # @app.route('/')
# # def index():
# #     return render_template('upload.html')

# @app.route('/upload', methods=['POST', 'GET'])
# def upload_file():
#     if request.method == 'GET':
#         return render_template('upload.html')

#     if 'file' not in request.files:
#         return jsonify({'error': 'No file uploaded'}), 400

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     try:
#         # Read CSV file
#         df = pd.read_csv(file, header=None)  # Assuming no header row
#         if df.shape[1] != 2:
#             return jsonify({'error': 'CSV must have exactly 2 columns'}), 400

#         # Convert to dictionary with first column as key, second as value
#         data_dict = dict(zip(df[0], df[1]))

#         return jsonify(data_dict)

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500



# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# # Define Models
# class Bot(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     menu_file = db.Column(db.String(200), nullable=False)  # Filepath of uploaded menu
#     menu_json = db.Column(db.Text, nullable=True)  # Store menu data as JSON
#     created_by = db.Column(db.String(100), nullable=False)  # Store the username of the creator
#     is_auto = db.Column(db.Boolean, default=False)  # New boolean field
#     questions = db.relationship('Question', backref='bot', lazy=True, cascade="all, delete")
#     type = db.Column(db.String(100), nullable=True, default=True)


# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     question_text = db.Column(db.Text, nullable=False)
#     answer_text = db.Column(db.Text, nullable=False)
#     bot_id = db.Column(db.Integer, db.ForeignKey('bot.id'), nullable=False)

# # Create Tables (Run only once)
# with app.app_context():
#     db.create_all()

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/current-user", methods=["GET"])
# @jwt_required()
# def get_current_user():
#     current_user = get_jwt_identity()
#     return jsonify({"username": current_user})

# # @app.route("/login", methods=["POST"])
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "GET":
#         return render_template("login.html")  # ✅ Serve login form for GET requests

#     # Process login for POST request
#     data = request.json
#     username = data.get("username")
#     password = data.get("password")

#     if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
#         access_token = create_access_token(identity=username)
#         return jsonify({"access_token": access_token})  # ✅ Return JWT token

#     return jsonify({"error": "Invalid credentials!"}), 401

# # @app.route('/get-bots', methods=['GET'])
# # def get_bots():
# #     bots = Bot.query.all()
# #     bots_data = []
# #     for bot in bots:
# #         bots_data.append({
# #             "id": bot.id,
# #             "name": bot.name,
# #             "menu_file": bot.menu_file,
# #             "questions": [{"question": q.question_text, "answer": q.answer_text} for q in bot.questions]
# #         })
# #     return jsonify(bots_data)

# # Route to Render Bot List Page
# @app.route('/bot-list', methods=['GET'])
# def bot_list():
#     return render_template('bot_list.html')

# # @app.route('/create-bot', methods=['GET', 'POST'])
# # def create_bot():

# #     if request.method == 'GET':
# #         return render_template("create_bot.html")
# #     try:
# #         bot_name = request.form['bot_name']
# #         menu_file = request.files['menu_file']
# #         questions = request.form.getlist('questions[]')
# #         answers = request.form.getlist('answers[]')

# #         # Save Menu File
# #         menu_filename = f"uploads/{menu_file.filename}"
# #         menu_file.save(os.path.join("static", menu_filename))
# #         menu_json = extract_menu_from_image([os.path.join("static", menu_filename)])
# #         # Create Bot Entry
# #         new_bot = Bot(name=bot_name, menu_file=menu_filename)
# #         db.session.add(new_bot)
# #         db.session.commit()

# #         # Save Questions & Answers
# #         for question, answer in zip(questions, answers):
# #             new_question = Question(question_text=question, answer_text=answer, bot_id=new_bot.id)
# #             db.session.add(new_question)

# #         db.session.commit()

# #         return jsonify({"message": "Bot created successfully!"}), 201
# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500

# # @app.route('/create-bot', methods=['GET', 'POST'])
# # def create_bot():
# #     if request.method == 'GET':
# #         return render_template("create_bot.html")

# #     try:
# #         bot_name = request.form['bot_name']
# #         menu_file = request.files['menu_file']
# #         questions = request.form.getlist('questions[]')
# #         answers = request.form.getlist('answers[]')

# #         # Save Menu File
# #         menu_filename = f"uploads/{secure_filename(menu_file.filename)}"
# #         menu_file.save(os.path.join("static", menu_filename))

# #         # Extract Menu JSON
# #         menu_json = extract_menu_from_image([os.path.join("static", menu_filename)])

# #         # Convert menu_json to a string before saving
# #         menu_json_str = json.dumps(menu_json, ensure_ascii=False)

# #         # Create and Save Bot Entry
# #         new_bot = Bot(name=bot_name, menu_file=menu_filename, menu_json=menu_json_str)
# #         db.session.add(new_bot)
# #         db.session.commit()

# #         # Save Questions & Answers
# #         for question, answer in zip(questions, answers):
# #             new_question = Question(question_text=question, answer_text=answer, bot_id=new_bot.id)
# #             db.session.add(new_question)

# #         db.session.commit()

# #         return jsonify({"message": "Bot created successfully!"}), 201

# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500


# @app.route('/create-bot_page', methods=['GET', 'POST'])
# def create_bot1():
#     if request.method == 'GET':
#         return render_template("create_bot.html")
    
# from flask_jwt_extended import jwt_required, get_jwt_identity
# @app.route('/create-bot', methods=['GET', 'POST'])
# @jwt_required()  # Ensure user is authenticated
# def create_bot():
#     if request.method == 'GET':
#         return render_template("create_bot.html")

#     try:
#         current_user = get_jwt_identity()  # Get the logged-in user's name

#         bot_name = request.form['bot_name']
#         menu_file = request.files['menu_file']
#         questions = request.form.getlist('questions[]')
#         answers = request.form.getlist('answers[]')

#         # Handle 'is_auto' (default to False if not provided)
#         is_auto = request.form.get('is_auto', 'false').lower() == 'on'

#         # Save Menu File
#         menu_filename = f"uploads/{secure_filename(menu_file.filename)}"
#         menu_file.save(os.path.join("static", menu_filename))

#         # Extract Menu JSON
#         menu_json = extract_menu_from_image([os.path.join("static", menu_filename)])
#         menu_json_str = json.dumps(menu_json, ensure_ascii=False)

#         # Create and Save Bot Entry with username and is_auto flag
#         new_bot = Bot(name=bot_name, menu_file=menu_filename, menu_json=menu_json_str, created_by=current_user, is_auto=is_auto)
#         db.session.add(new_bot)
#         db.session.commit()

#         # Save Questions & Answers
#         for question, answer in zip(questions, answers):
#             new_question = Question(question_text=question, answer_text=answer, bot_id=new_bot.id)
#             db.session.add(new_question)

#         db.session.commit()

#         return jsonify({"message": "Bot created successfully!", "created_by": current_user, "is_auto": is_auto}), 201

#     except Exception as e:
#         print(e)
#         return jsonify({"error": str(e)}), 500




# @app.route('/get-bots', methods=['GET'])
# def get_bots():
#     bots = Bot.query.all()
#     bots_data = []
#     for bot in bots:
#         bots_data.append({
#             "id": bot.id,
#             "name": bot.name,
#             "is_auto": "auto" if bot.is_auto else "manual",
#             "menu_file": bot.menu_file,
#             "menu_json": json.loads(bot.menu_json) if bot.menu_json else {},  # Convert back to dict
#             "questions": [{"question": q.question_text, "answer": q.answer_text} for q in bot.questions],
#             "type": bot.type.title()
#         })
#         print(json.loads(bot.menu_json))
#     return jsonify(bots_data)

# @app.route("/update-menu/<int:bot_id>", methods=["POST"])
# def update_menu(bot_id):
#     try:
#         data = request.json
#         menu_json = data.get("menu_json")

#         bot = Bot.query.get(bot_id)
#         if not bot:
#             return jsonify({"error": "Bot not found"}), 404

#         bot.menu_json = json.dumps(menu_json, ensure_ascii=False)  # Update menu JSON
#         db.session.commit()

#         return jsonify({"message": "Menu updated successfully!"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # API to Fetch All Bots
# # @app.route('/get-bots', methods=['GET'])
# # def get_bots():
# #     bots = Bot.query.all()
# #     bots_data = []
# #     for bot in bots:
# #         bots_data.append({
# #             "id": bot.id,
# #             "name": bot.name,
# #             "menu_file": bot.menu_file,
# #             "questions": [{"question": q.question_text, "answer": q.answer_text} for q in bot.questions]
# #         })
# #     return jsonify(bots_data)


# @app.route("/dashboard")
# @jwt_required()
# def dashboard():
#     current_user = get_jwt_identity()
#     return jsonify({"message": f"Welcome {current_user} to your dashboard!"})


# #@app.route('/extract_menu', methods=['GET'])
# def extract_menu_from_image(image_paths=None):
#     print(123)
#     # Print results
#     try:
#         menu = []
#         print(image_paths)
#         for image_path in image_paths:
#             client = Groq(api_key="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")
#             base64_image = encode_image(image_path)
#             print(client)
#             chat_completion = client.chat.completions.create(
#                 messages=[
#                     {
#                         "role": "user",
#                         "content": [
#                             {"type": "text", "text": """

#                             your need to extract the menu item is json format with category item and price in string format,

#                             example: 
#                             {
#                             "category1":{
#                                 "item1":"100",
#                                 "item2":"200"
#                             },
#                             "category2":{
#                                 "item3":"300",
#                                 "item4":"400"
#                             },
#                                 "category3":{
#                                 "item5":"500",
#                                 "item6":"600"
#                                 }
                            
#                             }

#                             please refer example for better reposne don't return in any other format
#                             always return in this format only never return in any other format
#                             make sure the json format is correct as simiar as above example
#                             always return json in correct syntax as above example only

#                             """},
#                             {"type": "image_url", "image_url": {"url": f"data:image/jpg;base64,{base64_image}"}},
#                         ],
#                     }
#                 ],
#                 model="llama-3.2-11b-vision-preview",
#             )

#             response_content = chat_completion.choices[0].message.content.replace('Here is the JSON response as requested:', '').replace('[', '').replace(']', '').replace('.', '').replace('.00', '')
#             print(response_content)
#             if not response_content:
#                 return {"error": "No response received from Groq API."}

#             try:
#                 menu.append(json.loads(response_content[response_content.find('{'):response_content.rfind('}')+2]))
#             except json.JSONDecodeError as error:
#                 print(error)
#         return menu
#     except Exception:
#         return {}

# @app.route('/get-bot/<int:bot_id>', methods=['GET'])
# def get_bot(bot_id):
#     try:
#         # Fetch the bot by ID
#         bot = Bot.query.get(bot_id)

#         if not bot:
#             return jsonify({"error": "Bot not found"}), 404

#         # Convert menu JSON from string to dictionary
#         menu_data = json.loads(bot.menu_json) if bot.menu_json else {}

#         # Fetch questions & answers for the bot
#         question_data = {}
#         for question in bot.questions:
#             question_data[question.question_text] = question.answer_text

#         # Response format
#         bot_data = {
#             "id": bot.id,
#             "name": bot.name,
#             "menu": menu_data,  # Menu in JSON format
#             "questions": question_data,  # List of questions & answers
#             "isauto": bot.is_auto,  # New field
#             "type": bot.type
#         }

#         return jsonify(bot_data), 200  # Return bot details

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# import requests
# @app.route('/send-messages', methods=['POST'])
# def send_msg():
#     data = request.get_json()
#     API_URL = "https://whatsapp-backend-kmum.onrender.com/send-messages"
#     payload = {
#     "session": data.get('session'),  # Replace with your actual session name
#     "messages": data.get('messages')
# }
#     headers = {"Content-Type": "application/json"}
#     response = requests.post(API_URL, data=json.dumps(payload), headers=headers)

#     # Print response
#     if response.status_code == 200:
#         print("✅ Messages sent successfully:", response.text)
#     else:
#         print("❌ Failed to send messages:", response.status_code, response.text)
#     return {}




from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from pydantic import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound

# Database setup
DATABASE_URL = "postgresql://whatsapp_bot_ph2f_user:wpMzB8LI6XupW62hTY9MIdWo2qnJpKoZ@dpg-cv340tgfnakc738hhj2g-a.oregon-postgres.render.com/whatsapp_bot_ph2f"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Secret key for JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User model
class UserDB(Base):
    __tablename__ = "users_table"
    email = Column(String, primary_key=True, index=True)
    password = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

class User(BaseModel):
    email: str
    password: str

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_user(db, email: str):
    try:
        return db.execute(select(UserDB).where(UserDB.email == email)).scalar_one()
    except NoResultFound:
        return None

@app.post("/signup")
def signup(user: User, db=Depends(SessionLocal)):
    if get_user(db, user.email):
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_password = hash_password(user.password)
    db_user = UserDB(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    return {"message": "User registered successfully"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(SessionLocal)):
    user = get_user(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"message": "Access granted", "user": payload["sub"]}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

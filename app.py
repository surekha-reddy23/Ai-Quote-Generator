from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import mysql.connector
load_dotenv()
import os

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("api"))
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="python_db"
    )
@app.route("/quote",methods=["GET","POST"])
def index():
    quote = []
    if request.method == "POST":
        topic = request.form["topic"]
        prompt = f"""
        Generate 5 short inspirational quotes about {topic}.

        """
        response = client .models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt
        )
        quote = response.text.strip().split("\n")
    return render_template("index.html",quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
    
   

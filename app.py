from flask import Flask, render_template, request
from google import genai
app = Flask(__name__)

client = genai.Client(api_key="AIzaSyAj2D1bdvrdRwQsi1ZRQpWyG7oXvcd9eT4")
@app.route("/",methods=["GET","POST"])
def index():
    quote = ""
    if request.method == "POST":
        topic = request.form["topic"]
        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=f"Generate a short inspirational quote about {topic}"

        )
        quote = response.text
    return render_template("index.html",quote=quote)

if __name__ == "__main__":
    app.run(debug=True)

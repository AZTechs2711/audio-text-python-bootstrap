from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
import speech_recognition as sr

app = Flask(__name__)
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    if request.method == "POST":
        print('form data recieved')

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            r = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as src:
                data = r.record(src)
            text = r.recognize_google(data, key=None)
            print('coverting...')

    return render_template('index.html', text=text)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

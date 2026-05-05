from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    meaning = None
    if request.method == 'POST':
        word = request.form['word'].strip()
        if not word or word.strip() == "":
            meaning = "Please enter a word"
        else:
            url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                try:
                    meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
                except:
                    meaning = "Meaning not found"
            else:
                meaning = "Word not found"

    return render_template('index.html', meaning=meaning)



if __name__ == '__main__':
    app.run(debug=True, port=5002)
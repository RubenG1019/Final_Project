import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def home():
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': 'apple',
        },
        headers={'api-key': 'bbcea0ef-9684-48ed-b9b3-d2533812214e'}
    )   
    r = r.json()
    return render_template("texttoimage.html",text = r["output_url"])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

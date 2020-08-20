from flask import Flask, request, render_template
from textSummarizer import summary

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        final_summary = summary.call_summary(text)

        return render_template('index.html', final_summary=final_summary)

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

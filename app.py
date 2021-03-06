from pymongo import MongoClient
from flask import Flask, request, render_template
from extractiveTextSummarizer import generateWeight, simpleMaths, tfidf
import wikipedia

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            search = request.form['search']
            page = wikipedia.page(search)
            text = page.content

            weight = request.form['level']
            calculated_weight = generateWeight.weight_range(weight)

            simple_summary = simpleMaths.call_summary(text, calculated_weight)
            tf_idf_summary = tfidf.call_Summary(text, calculated_weight)

            return render_template('index.html', simple=simple_summary, tf_idf=tf_idf_summary)

        except wikipedia.WikipediaException as e:
            return render_template('error.html', error=e)
        
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

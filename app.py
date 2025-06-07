from flask import Flask, request, render_template
from parser import extract_text_from_file
from matcher import calculate_similarity

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume = request.files['resume']
        jd_text = request.form['job_description']
        file_path = f"uploads/{resume.filename}"
        resume.save(file_path)

        resume_text = extract_text_from_file(file_path)
        score = calculate_similarity(resume_text, jd_text)

        return render_template('result.html', score=round(score * 100, 2))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

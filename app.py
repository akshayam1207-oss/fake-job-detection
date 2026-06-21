from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Red flags for fake job postings
FAKE_JOB_INDICATORS = {
    'payment_upfront': ['upfront payment', 'pay first', 'wire transfer', 'bitcoin'],
    'poor_grammar': ['plz', 'ur', 'u need', 'dont'],
    'urgency': ['urgent', 'asap', 'immediately'],
    'too_good': ['no experience needed', 'work from home guaranteed'],
    'suspicious': ['part time ceo', 'email only', 'no interview'],
    'personal_info': ['ssn', 'bank account', 'credit card']
}

def analyze_job_posting(text):
    text_lower = text.lower()
    found_flags = {}
    risk_score = 0
    
    for category, keywords in FAKE_JOB_INDICATORS.items():
        found_flags[category] = []
        for keyword in keywords:
            if keyword in text_lower:
                found_flags[category].append(keyword)
                risk_score += 1
    
    if risk_score == 0:
        risk_level = "Low Risk"
        color = "green"
    elif risk_score <= 2:
        risk_level = "Medium Risk"
        color = "yellow"
    else:
        risk_level = "High Risk"
        color = "red"
    
    return {
        'risk_level': risk_level,
        'risk_score': risk_score,
        'color': color,
        'flags': found_flags
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    job_text = request.form.get('job_text', '')
    
    if not job_text or len(job_text) < 10:
        return jsonify({'error': 'Please enter valid job posting'}), 400
    
    result = analyze_job_posting(job_text)
    return render_template('result.html', result=result, job_text=job_text)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
# 🔍 Fake Job Detection System

A **Flask-based web application** that detects fraudulent job postings using pattern recognition and keyword analysis. This tool helps job seekers identify scam job opportunities and protect themselves from fake job listings.

---

## ✨ Features

- **Smart Analysis:** Analyzes job postings for common scam indicators
- **Risk Assessment:** Returns risk level as Low, Medium, or High
- **Red Flag Detection:** Identifies specific warning signals found in the posting
- **Simple Interface:** Clean, user-friendly web interface
- **Instant Results:** Get analysis results in seconds

---

## 🛠️ Tech Stack

- **Backend:** Python 3.9+ with Flask 2.3.0
- **Frontend:** HTML5, CSS3, JavaScript
- **Pattern Recognition:** Keyword and grammar analysis

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/akshayam1207-oss/fake-job-detection.git
   cd fake-job-detection
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```

3. **Install Flask**
   ```bash
   pip install Flask
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

---

## 📖 How to Use

1. Visit http://localhost:5000
2. Paste a job posting in the text area
3. Click **"Analyze Job"**
4. View the risk assessment and red flags found

---

## 🎯 Red Flags Detected

The system checks for:
- **Payment Upfront:** Requests for wire transfer, Bitcoin, etc.
- **Poor Grammar:** Typos and spelling mistakes
- **Urgency Tactics:** "ASAP", "Very Urgent", "Immediate"
- **Unrealistic Promises:** "No experience needed", "Guaranteed work-from-home"
- **Suspicious Requests:** "Email only", "No interview", "Part-time CEO"
- **Personal Information:** Requests for SSN, bank account, credit card

---

## 📁 Project Structure

```
fake-job-detection/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML files
│   ├── index.html        # Home page
│   └── result.html       # Results page
└── static/               # CSS and static files
    └── style.css         # Styling
```

---

## 💡 How It Works

The application analyzes job postings by:
1. Converting text to lowercase
2. Scanning for known scam keywords
3. Assigning risk scores based on red flags found
4. Displaying warnings with specific indicators identified

---

## 🎓 Skills Demonstrated

- Flask web development
- Python programming
- Pattern recognition and data analysis
- Frontend development (HTML/CSS)
- User interface design




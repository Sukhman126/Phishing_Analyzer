# Phishing Website Detection & URL Safety Analyzer

*Submitted By:* Sukhmanpreet Kaur (URN: 23303324)  
*Submitted To:* Dipika Sharma (Assistant Professor)  
*Institution:* Sardar Beant Singh State University, Gurdaspur  

---

## 1. Project Idea
This is a web-based application designed to analyze website URLs and determine whether they are safe or suspicious based on predefined security parameters.

## 2. Working Algorithm
The system evaluates a URL through the following security checks:
* *Protocol Check:* Identifies the presence of HTTPS.
* *Length Analysis:* Flags URLs longer than 75 characters as suspicious.
* *IP Address Detection:* Detects if an IP address is used instead of a domain name.
* *Keyword Detection:* Scans for suspicious words like "login", "bank", and "update".

## 3. Technology Stack
* *Language:* Python 3 (Backend)
* *Web Framework:* Flask (Backend Platform)
* *Frontend:* HTML5 and CSS3 (No JavaScript used)
* *Environment:* Python Virtual Environment (venv)

---

## 4. How to Run
1. Open the terminal in VS Code.
2. Activate the virtual environment:
```bash
   venv\Scripts\activate
3. Install Flask: pip install flask
4. Run the application: python app.py
5. Open your browser and go to: http://127.0.0.1:5000

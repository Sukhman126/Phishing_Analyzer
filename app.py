from flask import Flask, render_template, request
import re

app = Flask(__name__)

def analyze_url(url):
    score = 0
    
    # 1. Check HTTPS protocol
    if not url.startswith("https"):
        score += 1

    # 2. Measure length of the URL
    if len(url) > 75:
        score += 1

    # 3. Detect use of IP address instead of domain
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    if re.search(ip_pattern, url):
        score += 2

    # 4. Identify suspicious keywords
    suspicious_words = ["login", "verify", "update", "secure", "account", "bank"]
    for word in suspicious_words:
        if word in url.lower():
            score += 1

    # Classification Module
    if score <= 1:
        result = "Safe"
    elif score == 2:
        result = "Suspicious"
    else:
        result = "Potentially Dangerous"

    return score, result

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    score = 0
    if request.method == "POST":
        # Ensure the form key matches the HTML 'name' attribute
        url = request.form.get("url_input")
        if url:
            score, result = analyze_url(url)

    return render_template("index.html", result=result, score=score)

if __name__ == "__main__":
    app.run(debug=True)
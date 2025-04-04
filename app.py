from flask import Flask, render_template, send_file, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('webpage.html')

@app.route('/Project- Investigating Netflix Movies - DataCamp.pdf', methods=['GET'])
def get_project1():
    return send_file('static/Project- Investigating Netflix Movies - DataCamp.pdf', as_attachment=False)

@app.route('/excelProject', methods=['GET'])
def get_project2():
    return redirect('https://github.com/marishellochan/Financial_Ratios_Trend_Database_Template')

@app.route('/airbnbProject', methods=['GET'])
def get_project3():
    return render_template('AirBnB_Listings.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



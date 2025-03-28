from flask import Flask, send_file

app = Flask(__name__)

@app.route('/Project- Investigating Netflix Movies - DataCamp.pdf', methods=['GET'])
def get_project1():
    return send_file('static/Project- Investigating Netflix Movies - DataCamp.pdf', as_attachment=False)

@app.route('/project2.pdf', methods=['GET'])
def get_project2():
    return send_file('project2.pdf', as_attachment=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



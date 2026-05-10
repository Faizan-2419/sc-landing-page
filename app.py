from flask import Flask,render_template
import webbrowser

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    import webbrowser
    webbrowser.open("http://127.0.0.1:5002")
    app.run(debug=False, port=5002)

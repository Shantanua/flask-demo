from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['ticker']
    #splot(text)
    return render_template('index.html')
   

if __name__ == '__main__':
  app.run(port=33507)

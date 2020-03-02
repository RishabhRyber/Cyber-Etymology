import flask
app=flask(__name__)

if __name__=="__main__":
    app.run(port=8080,debug=True)

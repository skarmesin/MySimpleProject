from flask import Flask

app = Flask(__name__)

def is_number(var):
	try:
		int(var)
		return True
	except Exception:
		return False

@app.route("/foo/<num>")
def got_num(num: str):
    if is_number(num):
        return f"{num} is a number!"
    else:
        return f"{num} is not a number!"

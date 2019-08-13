from find_printers import find_printers_lpinfo
from count_printers import count_printers

from flask import Flask, render_template

# printers = count_printers()

app = Flask(__name__)


@app.route('/')
def hello():
    find_printers_lpinfo()
    printers = count_printers()
    print printers
    return render_template("index.html", printers=printers)

if __name__ == '__main__':
    app.run()
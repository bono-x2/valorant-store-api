from flask import Flask, render_template
from valorantstore import ValorantStore

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<username_api>/<password_api>/<region_api>/")
def get_store(username_api, password_api, region_api):
    valorant_store = ValorantStore(username=username_api, password=password_api, region=region_api, sess_path='./tmp', proxy=None)
    return render_template('store.html', everything=valorant_store.store(True))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8090)
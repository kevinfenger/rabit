from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/<customer_id>/<video_id>') 
def get_image(customer_id, video_id): 
    return jsonify({"1" : "test"})

if __name__ == "__main__":
    app.run()

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def pose_service():
    return 'Hello, I am pose estimation service ok!'

@app.route('/pose', methods = ['POST'])
def do_pose_estimation():
    data = request.json
    print("------------------------------")
    print('Input from object detection service : ' + data['data'])
    print("------------------------------")
    return 'pose estimated'

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)

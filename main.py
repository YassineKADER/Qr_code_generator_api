from flask import Flask, jsonify, request, send_file
import qrcode
from io import BytesIO
app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    if 'data' not in request.json:
        return jsonify({'error': 'No data provided'}), 404

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(request.json['data'])
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')
@app.route('/', methods=['GET'])
def redirect():
    return "The Service Is Running...."
if __name__ == '__main__':
    app.run()
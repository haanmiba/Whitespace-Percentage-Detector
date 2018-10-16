from flask import Flask, render_template, jsonify, request
from PIL import Image
from io import BytesIO
from collections import Counter
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def process():
	raw_img = request.files['file'].read()
	img = Image.open(BytesIO(raw_img))
	pixels = img.getdata()
	num_all_pixels = len(pixels)
	c = Counter(pixels)

	white_pixels = {k: v for k, v in c.items() if k[:3] == (255, 255, 255)}
	num_white_pixels = sum(white_pixels.values())

	ratio = num_white_pixels / float(num_all_pixels)
	return str('{:.2f}%'.format(ratio * 100))


if __name__ == '__main__':
    app.run()

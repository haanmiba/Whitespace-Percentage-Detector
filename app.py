from flask import Flask, render_template, jsonify, request
from PIL import Image
from psd_tools import PSDImage
from io import BytesIO
from collections import Counter
app = Flask(__name__)

posts = [
	{
		'author': 'Hans Bas',
		'title': 'First Post',
		'content': 'First post content',
		'date_posted': 'October 17, 2018'
	},
	{
		'author': 'Hans Bas',
		'title': 'Second Post',
		'content': 'Second post content',
		'date_posted': 'October 17, 2018'
	}	
]

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'psd'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detect-whitespace', methods=['POST'])
def detect_whitespace():
	raw_img = request.files['file'].read()
	img = Image.open(BytesIO(raw_img))
	pixels = img.getdata()
	num_all_pixels = len(pixels)
	c = Counter(pixels)

	white_pixels = {k: v for k, v in c.items() if k[:3] == (255, 255, 255)}
	num_white_pixels = sum(white_pixels.values())

	ratio = num_white_pixels / float(num_all_pixels)
	return str('{:.2f}%'.format(ratio * 100))


@app.route('/about')
def about():
	return '<h1>About</h1>'


@app.route('/blog')
def blog():
	return render_template('blog.html', posts=posts, title='Posts')

if __name__ == '__main__':
    app.run(debug=True)

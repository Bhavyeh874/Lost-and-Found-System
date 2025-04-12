from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(_name_)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# In-memory storage
Lost_items = []
Found_items = []

# Base class
class Vastu:
    def _init_(self, name, description, contact, image_filename=None):
        self.name = name
        self.description = description
        self.contact = contact
        self.image_filename = image_filename

class LostItem(Vastu):
    def _init_(self, name, description, contact, image_filename=None):
        super()._init_(name, description, contact, image_filename)

class FoundItem(Vastu):
    def _init_(self, name, description, contact, image_filename=None):
        super()._init_(name, description, contact, image_filename)

@app.route('/')
def home():
    return render_template('index.html', khoya_items=khoya_items, paaya_items=paaya_items)

@app.route('/report_Lost', methods=['POST'])
def report_Lost():
    try:
        name = request.form['name']
        description = request.form['description']
        contact = request.form['contact']
        image = request.files.get('image')
        filename = None
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        item = LostItem(name, description, contact, filename)
        Lost_items.append(item)
        return redirect(url_for('home'))
    except Exception as e:
        return f"Error while reporting lost item: {e}"

@app.route('/report_Found', methods=['POST'])
def report_paaya():
    try:
        name = request.form['name']
        description = request.form['description']
        contact = request.form['contact']
        image = request.files.get('image')
        filename = None
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        item = FoundItem(name, description, contact, filename)
        Found_items.append(item)
        return redirect(url_for('home'))
    except Exception as e:
        return f"Error while reporting found item: {e}"

if _name_ == '_main_':
    print("\n✨ Welcome to VastuVault! ✨")
    print("Visit: http://0.0.0.0:$PORT\n")

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )

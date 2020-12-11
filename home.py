from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os
from flask_mail import Mail
from werkzeug.utils import secure_filename
import re

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True

app = Flask(__name__)
app.secret_key = 'super-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['username'],
    MAIL_PASSWORD=params['pass']
)
mail = Mail(app)
"""if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']"""

app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
db = SQLAlchemy(app)


class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)


class Posts(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    tagline = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_name = db.Column(db.String(25), nullable=True)


@app.route("/")
@app.route("/home")  # if we write more then one route for function or end point then it is called by both of them
def home():
    page = request.args.get('page')
    if str(page).isnumeric():
        page = 0

    posts = Posts.query.filter_by().all()[0:params['num_post']]
    return render_template('index.html', params=params, posts=posts)

@app.route("/allpost")
def allpost():
    posts = Posts.query.filter_by().all()
    return render_template('allpost.html', params=params, posts=posts)


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    posts = Posts.query.filter_by().all()
    if 'user' in session and session['user'] == params['admin_user']:
        return render_template('dashboard.html', params=params, posts=posts)
    if request.method == "POST":
        name = request.form.get('user')
        passw = request.form.get('pass')
        if name == params['admin_user'] and passw == params['admin_pass']:
            session['user'] = name
            return render_template('dashboard.html', params=params, post=posts)
        else:
            return render_template('login.html', params=params)
    else:
        return render_template('login.html', params=params)


@app.route("/edit/<string:Id>", methods=["GET", "POST"])
def edit(Id):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            title = request.form.get('title')
            tagline = request.form.get('tagline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')

            if Id == '0':
                post = Posts(title=title, tagline=tagline, slug=slug, content=content, date=datetime.now(),
                             img_name=img_file)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(Id=Id).first()
                post.title = title
                post.tagline = tagline
                post.slug = slug
                post.content = content
                post.img_name = img_file
                post.date = datetime.now()
                db.session.commit()
                return redirect('/edit/' + Id)
        post = Posts.query.filter_by(Id=Id).first()
        return render_template('edit.html', params=params, post=post,Id=Id)


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            f = request.files['img']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return redirect("/dashboard")


@app.route("/delete/<string:Id>", methods=["GET", "POST"])
def delete(Id):
    if 'user' in session and session['user'] == params['admin_user']:
        post = Posts.query.filter_by(Id=Id).first()
        db.session.delete(post)
        db.session.commit()
    return redirect("/dashboard")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/dashboard")


@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/post/<string:post_slug>", methods=["GET"])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        msg = request.form.get('msg')
        entry = Contacts(name=name, email=email, phone=phone, date=datetime.now(), msg=msg)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[params['username']],
                          body=msg + "\n" + phone)
        return render_template('contact.html', params=params)
    else:
        return render_template('contact.html', params=params)


# automatic change on template if we use debug
app.run(debug=True)

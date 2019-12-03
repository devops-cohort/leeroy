from flask import render_template, redirect, url_for, redirect, request
from application import app, db
from application.models import Post
from application.forms import PostForm

@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def home():
    if request.form:
        event = Event(title=request.form.get("title"))
        db.session.add(event)
        db.session.commit()
        return render_template('home.html', title='Home')

'''update route is below'''
@app.route('/event', methods=['GET', 'POST'])
def event():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    event = event.query.filter_by(title=oldtitle).first()
    event.title = newtitle
    db.session.commit()
    return redirect(url_for('event'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = cuurent_user.last_name
        form.email.data = current_user.email
        return render_template('account.html', title='Account', form=form)

'''delete route is below'''
@app.route("/delete", methods=['POST'])
def delete():
    title = request.form.get("title")
    event = event.query.filter_by(title=title).first()
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/post', methods=['GET','POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
        title=form.title.data,
        content=form.content.data
        )
        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('post.html',title='Post', form=form)

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = User(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=hashed_pw
                )
        db.session.add(user)
        db.session.commit
        return redirect(url_for('post'))
    return render_templates('register.html', title='RegistrationForm')

'''the function below is for the delete function'''


@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    event = event.query.filter_by(title=title).first()
    db.session.delete(event)
    db.session.commit()
    return redirect("/")

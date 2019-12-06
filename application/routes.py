from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt 
from application.models import Event, User
from application.forms import EventForm, RegistrationForm, LoginForm, UpdateAccountForm, UpdateEventForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
	eventData = Event.query.all()
	return render_template('home.html', title='Home', event=eventData)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, 
                password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('event'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/event', methods=['GET','POST'])
@login_required
def event():
	form = EventForm()
	if form.validate_on_submit():
		eventData = Event(
                        promoter=form.promoter.data,
			location=form.location.data, 
                        user_id=form.user_id.data,
                        event_date=form.event_date.data 
		)
		db.session.add(eventData)
		db.session.commit()
		return redirect(url_for('home'))
	else:
		print(form.errors)
	return render_template('/event.html', title='Event', form=form)


#updating route for the events 
#update route is below
@app.route('/event', methods=['GET', 'POST'])
def update_event():
        form = UpdateEventForm()
        if form.validate_on_submit():  
            current_user.promoter = form.promoter.data
            current_user.location = form.location.data
            current_user.event_date = form.event_date.data
            db.session.commit()
            return redirect(url_for('event'))
        elif request.method == 'GET':
            form.promoter.data = current_user.promoter
            form.location.data = current_user.location
            form.event_date.data = current_user.event_date
            return redirect(url_for('home'))
        return render_template('event.html', title='event', form=form)

@app.route('/account-deleted', methods=['GET'])
@login_required
def account_deleted():
    user = User.query.filter_by(id=request.args.get('id')).one()
    db.session.delete(user)
    db.session.commit()
    logout_user()
    return render_template('account-deleted.html')
        

#help you login with a saved account details from registered user
@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		# print("User : " + user)
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/account', methods=['GET','POST'])
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
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form, user_id=current_user.id)




@app.route('/event/<int:event_id>', methods=['GET', 'POST'])
def view_event(event_id):
	if current_user.is_authenticated:
		event = Event.query.filter_by(id=event_id).first()
		if Event.user_id == current_user.id:
			return redirect(url_for('Home'))
		else:
			return redirect(url_for('register'))
	return render_template('login.html', title='TURN BACK')

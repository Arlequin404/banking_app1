from flask import render_template, redirect, url_for, flash, session, jsonify, current_app
from .forms import LoginForm, RegisterForm
from .models import User
from flask_app.abstract_factory.factory import SQLServerFactoryDB1, SQLServerFactoryDB2
from datetime import datetime

factory_db1 = SQLServerFactoryDB1()
factory_db2 = SQLServerFactoryDB2()

@current_app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@current_app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_dao = factory_db1.create_user_dao()
        user = user_dao.get_user_by_username(form.username.data)
        if user and user.password == form.password.data:
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@current_app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@current_app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_dao = factory_db1.create_user_dao()
        new_user = User(
            username=form.username.data,
            password=form.password.data,
            email=form.email.data,
            full_name=form.full_name.data,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        user_dao.create_user(new_user)
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@current_app.route('/users/<int:user_id>')
def get_user(user_id):
    user_dao = factory_db1.create_user_dao()
    user = user_dao.get_user(user_id)
    if user:
        return jsonify(
            id=user.id,
            username=user.username,
            password=user.password,
            email=user.email,
            full_name=user.full_name,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
    return jsonify(error="User not found"), 404

@current_app.route('/transactions/<int:transaction_id>')
def get_transaction(transaction_id):
    transaction_dao = factory_db2.create_transaction_dao()
    transaction = transaction_dao.get_transaction(transaction_id)
    if transaction:
        return jsonify(
            id=transaction.id,
            user_id=transaction.user_id,
            amount=transaction.amount,
            date=transaction.date,
            description=transaction.description,
            transaction_type=transaction.transaction_type,
            status=transaction.status
        )
    return jsonify(error="Transaction not found"), 404

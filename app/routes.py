#coding=utf-8
from flask import render_template, flash, redirect, url_for
from app import apps
from app.forms import LoginForm

@apps.route("/")
@apps.route("/index")
def index():
    user = {'username': 'cc'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'Beautiful day in china!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home',user=user,posts=posts)
@apps.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for use {}, remember_me={}'.format(form.username.data, form.remember_me.data))
#        return redirect('/index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form) #左边的title和form指的是login.html里的变量，右边的form是上面的实例


if __name__ == '__main__':
    apps.run()

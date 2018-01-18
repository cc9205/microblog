from flask import render_template
from app import apps

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
if __name__ == '__main__':
    apps.run()

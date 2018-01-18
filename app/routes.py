from app import apps

@apps.route("/")
@apps.route("/index")
def index():
    return "Hello,World!"

if __name__ == '__main__':
    apps.run()

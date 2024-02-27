###MVC
# モデル
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# ビュー
class UserView:
    def display_user(self, user):
        print(f"Name: {user.name}, Email: {user.email}")

# コントローラー
class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_user(self, user_id):
        user = self.model.get_user(user_id)
        self.view.display_user(user)

# メイン
if __name__ == "__main__":
    user = User("John Doe", "john.doe@example.com")
    view = UserView()
    controller = UserController(user, view)
    controller.get_user(1)

exit()

### ADR
from flask import Flask, render_template, request

# モデル
class UserADR(db.Model):
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<User name={self.name}, email={self.email}>"

# レスポンダー
class HtmlResponder:
    def __init__(self, template):
        self.template = template

    def respond(self, payload):
        return render_template(self.template, **payload)

# アクション
class IndexAction:
    def __init__(self, responder):
        self.responder = responder

    def __call__(self):
        users = UserADR.query.all()
        return self.responder.respond({'users': users})

class ShowAction:
    def __init__(self, responder):
        self.responder = responder

    def __call__(self, user_id):
        user = UserADR.query.get(user_id)
        if user is None:
            return "Not Found", 404
        else:
            return self.responder.respond({'user': user})

# アプリケーション
app = Flask(__name__)

@app.route('/')
def index():
    action = IndexAction(HtmlResponder('users/index.html'))
    return action()

@app.route('/users/<int:user_id>')
def show(user_id):
    action = ShowAction(HtmlResponder('users/show.html'))
    return action(user_id)

if __name__ == '__main__':
    app.run()

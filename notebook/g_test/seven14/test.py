###MVC
class User:                                                     # Model
    def __init__(self, name): self.name = name

class UserView:                                                 # View
    def display_user(self, user): print(f"Name: {user.name}")

class UserController:                                           # Controller
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_user(self, user_id):
        user = self.model
        self.view.display_user(user)

if __name__ == "__main__":                                      # Main
    user = User("John Doe")
    view = UserView()
    controller = UserController(user, view)
    controller.get_user(0)
exit()



###ADR
class GetUserAction:                                            # Action
    def __init__(self, user_id, model):
        self.user_id = user_id
        self.model = model

    def execute(self):
        user = self.model
        return user

class UserModel:                                                # Domain
    def __init__(self):
        self.users = []

class UserResponder:                                            # Responder
    def display_user(self, user):
        if user is not None:
            print(f"Name: {user.name}")
        else:
            print("User not found")

if __name__ == "__main__":                                      # Main
    user_model = UserModel()
    user_model.users.append(User("John Doe"))

    action = GetUserAction(0, user_model)
    user = action.execute()

    responder = UserResponder()
    responder.display_user(user)

exit()

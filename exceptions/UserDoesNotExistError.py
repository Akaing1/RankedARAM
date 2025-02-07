class UserDoesNotExistError(Exception):
    def __init__(self, name, msg="User does not exist"):
        self.msg = msg
        self.name = name
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.msg}: {self.name}'

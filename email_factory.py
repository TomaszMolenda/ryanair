from entity import Definition, Email


class EmailFactory:
    __instance = None

    @staticmethod
    def get_instance():
        if EmailFactory.__instance is None:
            EmailFactory()
        return EmailFactory.__instance

    def __init__(self):
        if EmailFactory.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            EmailFactory.__instance = self

    @staticmethod
    def create_email(request):
        email_from = request.form['email_from'].strip()
        email_to = request.form['email_to'].strip()
        passwrod = request.form['password'].strip()
        server_smtp = 'smtp.gmail.com:587'

        assert email_from
        assert email_to
        assert passwrod
        assert server_smtp

        return Email(email_from, email_to, passwrod, server_smtp)

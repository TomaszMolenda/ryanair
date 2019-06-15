import smtplib
import logging

from email_factory import EmailFactory
from email_repository import EmailRepository


class EmailApplicationService:
    __instance = None

    @staticmethod
    def get_instance():
        if EmailApplicationService.__instance is None:
            EmailApplicationService()
        return EmailApplicationService.__instance

    def __init__(self):
        if EmailApplicationService.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            EmailApplicationService.__instance = self

    @staticmethod
    def set_email(request):
        email_factory = EmailFactory.get_instance()
        email_repository = EmailRepository.get_instance()

        email = email_factory.create_email(request)
        email_repository.save(email)

        logging.info('saved email: %s', email.asdict())

        pass

    @staticmethod
    def send_email(email_content):

        email_repository = EmailRepository.get_instance()
        email = email_repository.get()
        fromx = email['email_from']
        to = email['email_to']
        password = email['password']
        subject = 'Mam wycieczkę!'  # Line that causes trouble
        msg = 'Subject:{}\n\n{}'.format(subject, email_content)
        server = smtplib.SMTP(email['server_smtp'])
        server.starttls()
        server.ehlo()
        server.login(fromx, password)
        server.sendmail(fromx, to, msg.encode('utf-8').strip())
        server.quit()

        logging.info('send email: %s', email_content)

        pass

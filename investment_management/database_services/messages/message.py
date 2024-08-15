from investment_management.models import Message


class MessageService:

    def __init__(self) -> None:
        pass


    def post_message(self, email_id, message_text):
        new_message = Message(email_id=email_id, message=message_text)
        new_message.save()

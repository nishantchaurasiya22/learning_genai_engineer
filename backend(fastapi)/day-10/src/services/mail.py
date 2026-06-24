from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from typing import List
from src.config.settings import settings

conf = ConnectionConfig(
    MAIL_USERNAME = settings.MAIL_USERNAME,
    MAIL_PASSWORD = settings.MAIL_PASSWORD,
    MAIL_FROM = settings.MAIL_FROM,
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="fastapi learning",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)
async def send_email(emails:List[str]):
    html = """<p>Hi thanks for Registration.Our Team will connect you soon!</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=emails,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return {"message": "email has been sent"}
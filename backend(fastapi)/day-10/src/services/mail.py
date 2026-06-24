from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List

conf = ConnectionConfig(
    MAIL_USERNAME = "nishantchaurasiya1108@gmail.com",
    MAIL_PASSWORD = "pgmslvksqrizgctx",
    MAIL_FROM = "nishantchaurasiya1108@gmail.com",
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
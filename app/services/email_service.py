from fastapi_mail import (
    FastMail,
    MessageSchema,
    ConnectionConfig,
    MessageType,
    NameEmail,
)
from app.core.config import settings
from pathlib import Path

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=True,
)


class EmailService:

    @staticmethod
    async def send_email(
        subject: str,
        recipients: list[NameEmail],
        body: str,
        attachments: list[str] | None = None,
    ):
        message = MessageSchema(
            subject=subject,
            recipients=recipients,
            body=body,
            subtype=MessageType.html,
            attachments=attachments or [],  # type: ignore
        )

        fm = FastMail(conf)
        await fm.send_message(message)

    @staticmethod
    async def send_otp_email(email: NameEmail, otp: str):
        body = f"""
        <h2>Verify Your Account</h2>
        <p>Your OTP code is:</p>
        <h1>{otp}</h1>
        <p>This code expires in 5 minutes.</p>
        """
        BASE_DIR = Path(__file__).resolve().parent.parent  # go up to app/
        await EmailService.send_email(
            subject="OTP Verification",
            recipients=[email],
            body=body,
            attachments=[str(BASE_DIR / "assets" / "demo.xlsx")],
        )

    @staticmethod
    async def send_reset_password_email(email: NameEmail, link: str):
        body = f"""
        <h2>Reset Password</h2>
        <p>Click below to reset:</p>
        <a href="{link}">Reset Password</a>
        """

        await EmailService.send_email(
            subject="Reset Password", recipients=[email], body=body
        )

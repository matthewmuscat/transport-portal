import os
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

from django.template.loader import get_template

USERNAME = os.environ.get("MAIL_USER")
PASSWORD = os.environ.get("MAIL_PASS")


def send_mail(send_to, subject, html, send_from=USERNAME,
              server="smtp.office365.com", attachments: dict = None,
              port=587, tls=True):
    """
    Sends an html email using smtplib.

    This should be configured by setting certain environment variables,
    see the constants in utils/email.py.
    """

    # Set up the message
    msg_root = MIMEMultipart('related')
    msg_root['From'] = send_from
    msg_root['To'] = (send_to if isinstance(send_to, str) else COMMASPACE.join(send_to))
    msg_root['Date'] = formatdate(localtime=True)
    msg_root['Subject'] = Header(subject, 'utf-8')

    # Build the message root
    msg = MIMEMultipart('mixed')
    msg_root.attach(msg)
    html_message = MIMEText(html, "html", "utf-8")

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(html_message)

    # Attach any attachments
    for attachment in attachments.values():
        part = MIMEApplication(
            attachment.read(),
            Name=attachment.name,
            _subtype=attachment.content_type
        )
        part['Content-Disposition'] = f"attachment; filename={attachment.name}"
        msg.attach(part)

    # Send the mail
    smtp = smtplib.SMTP(server, int(port))

    if tls:
        smtp.starttls()

    if USERNAME is not None:
        smtp.login(USERNAME, PASSWORD)

    smtp.sendmail(send_from, send_to, msg_root.as_string())
    smtp.quit()


def send_mail_from_template(send_to, subject, template_path, context, attachments: dict = None):
    """
    Takes a template, renders it with the context,
    and then sends an html email using send_email().

    This allows us to use DTL for sending beautiful html emails.

    Remember that html emails should use inline css!
    """

    template = get_template(template_path)
    html_email = template.render(context)
    send_mail(send_to, subject, html_email, attachments=attachments)

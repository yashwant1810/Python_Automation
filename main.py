# all of the stoopid (actually needed) import statements
import os
import time
from email.message import EmailMessage
import ssl
import smtplib
import certifi
import mimetypes
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set environment variables or run config variables in your ide
appkey_email = os.environ["appkey_email"]
email_sender = os.environ["email_sender"]
email_receiver = "decoyspotify@gmail.com"

# Path to the directory on your macOS
directory_path = os.environ["shared_folder"]

# Allowed file extensions
allowed_extensions = {'.txt', '.pdf', '.jpg', '.png'}


# Define the event handler class
class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        _, file_extension = os.path.splitext(file_path)

        if file_extension in allowed_extensions:
            self.send_email_with_attachment(file_path)


    def send_email_with_attachment(self, file_path):
        # this function sends he email duh

        # Get the current date and time
        now = datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

        # Set the subject with the current date and time or anything you want
        subject = f"{formatted_datetime} : Check out these files from your macOS"
        # set some content/body to it
        body = """
        Hello,

        Please find the attached files from the specified directory.

        Regards,
        Yashu
        """

        # Create the email message
        email_message = EmailMessage()
        email_message["Subject"] = subject
        email_message["From"] = email_sender
        email_message["To"] = email_receiver
        email_message.set_content(body)

        # Guess the MIME type of the file
        mime_type, _ = mimetypes.guess_type(file_path)
        mime_type = mime_type or 'application/octet-stream'
        main_type, sub_type = mime_type.split('/', 1)
        # so basically the above lines guess the type and storage the maintype and subtype eg. image/png
        # if mime cannot resolve for a filetype the code just assigns it as generic binary data

        with open(file_path, 'rb') as file:
            # opens the file and attaches it to the email
            email_message.add_attachment(file.read(), maintype=main_type, subtype=sub_type,
                                         filename=os.path.basename(file_path))

        # Use certifi for SSL context ( parameter/arguement is optional i.e only add if it doesnt work without it
        # and gives a certificate error
        context = ssl.create_default_context(cafile=certifi.where())

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            # login and send it
            smtp.login(email_sender, appkey_email)
            smtp.sendmail(email_sender, email_receiver, email_message.as_string())

        # Delete the file after sending the email
        os.remove(file_path)
        print(f"Email sent and file {file_path} deleted.")


# Set up the observer and run
event_handler = NewFileHandler()
observer = Observer()
observer.schedule(event_handler, path=directory_path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
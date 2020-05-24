from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def init():
    root = Tk()
    root.resizable(width=False, height=False)
    root.geometry('290x320')
    root.title('Email sender')
    root['bg'] = 'white'

    mail_var = StringVar()
    pass_var = StringVar()
    mail_entry = Entry(root, width=25, bg='white', textvariable=mail_var)
    mail_entry.insert(END, 'Enter your\' email')
    mail_entry.place(x=0, y=15)
    password_button = Entry(root, width=25, bg='white', textvariable=pass_var)
    password_button.insert(END, 'Enter you\'r password')
    password_button.place(x=0, y=50)
    but_accept = Button(root, width=10, text='Eccept', command=lambda: save_init(mail_var, pass_var))
    but_accept.place(x=0, y=150)
    root.mainloop()


def save_init(mail_var, pass_var):
    mail_get = str(mail_var.get())
    pass_get = str(pass_var.get())
    root = Tk()
    root.resizable(width=False, height=False)
    root.geometry('290x320')
    root.title('Email sender')
    root['bg'] = 'white'
    recipient_var = StringVar(root)
    subject_var = StringVar(root)
    text_var = StringVar(root)
    recipient = Entry(root, width=25, bg='white', textvariable=recipient_var)
    recipient.insert(END, 'Enter subject email')
    recipient.place(x=0, y=50)
    subject_entry = Entry(root, width=25, bg='white', textvariable=subject_var)
    subject_entry.insert(END, 'Enter recipient of  email')
    subject_entry.place(x=0, y=15)
    text_entry = Entry(root, width=25, bg='white', textvariable=text_var)
    text_entry.insert(END, 'Enter text of  email')
    text_entry.place(x=0, y=150)
    but_send = Button(root, width=10, text='Accept', command=lambda: send_mail(mail_get, pass_get, recipient_var,
                                                                               subject_var, text_var))
    but_send.place(x=0, y=200)
    root.mainloop()


def send_mail(sender, password, recipient_var, subject_var, text_var):
    recipient_get = str(recipient_var.get())
    subject_get = str(subject_var.get())
    text_get = str(text_var.get())
    msg = MIMEMultipart()
    msg['Subject'] = recipient_get
    msg['From'] = sender
    msg['To'] = subject_get
    msg.attach(MIMEText(text_get, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, msg['To'], msg.as_string())
    server.quit()

    print("successfully sent email to %s:" % (msg['To']))


if __name__ == "__main__":
    init()
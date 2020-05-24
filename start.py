from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

root = Tk()
root.resizable(width=False, height=False)
root.geometry('290x320')
root.title('Email sender')
root['bg'] = 'white'

mail_var = StringVar()
pass_var = StringVar()
recipient_var = StringVar()
subject_var = StringVar()
text_var = StringVar()
mail_entry = Entry(root, width=25, bg='white', textvariable=mail_var)
# mail_entry.insert(END, 'Enter your\' email')
mail_entry.place(x=0, y=15)
password_button = Entry(root, width=25, bg='white', textvariable=pass_var)
# password_button.insert(END, 'Enter you\'r password')
password_button.place(x=0, y=50)
but_accept = Button(root, width=10, text='Eccept', command=lambda: r.save())
but_accept.place(x=0, y=150)

class Send:

    def save(self):
        self.mail = str(mail_var.get())
        self.password = str(pass_var.get())
        r.inst()

    def inst(self):
        root = Tk()
        root.resizable(width=False, height=False)
        root.geometry('290x320')
        root.title('Email sender')
        root['bg'] = 'white'
        recipient = Entry(root, width=25, bg='white', textvariable=recipient_var)
        recipient.place(x=0, y=50)
        subject_entry = Entry(root, width=25, bg='white', textvariable=subject_var)
        subject_entry.place(x=0, y=15)
        text_entry = Entry(root, width=25, bg='white', textvariable=text_var)
        text_entry.place(x=0, y=150)
        self.rg = str(recipient_var.get())
        self.sg = str(subject_var.get())
        self.tg = str(text_var.get())

        def send_mail():
            print(r.rg,r.sg,r.tg)
            msg = MIMEMultipart()
            msg['Subject'] = r.sg
            msg['From'] = r.mail
            msg['To'] = r.rg
            msg.attach(MIMEText(r.tg, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(r.mail, r.password)
            server.sendmail(r.mail, msg['To'], msg.as_string())
            server.quit()

            print("successfully sent email to %s:" % (msg['To']))
        but_send = Button(root, width=10, text='Accept', command=lambda: print(recipient_var.get()))
        but_send.place(x=0, y=200)

# falcone159357bv@gmail.com
# 31.08.1996bV
#     def send_mail(self):
#         msg = MIMEMultipart()
#         msg['Subject'] = self.sg
#         msg['From'] = self.mail
#         msg['To'] = 'falce159357bv@gmail.com'
#         msg.attach(MIMEText(self.tg, 'plain'))
#
#         server = smtplib.SMTP('smtp.gmail.com: 587')
#         server.starttls()
#         server.login(self.mail, r.password)
#         server.sendmail(self.mail, msg['To'], msg.as_string())
#         server.quit()

        # print("successfully sent email to %s:" % (msg['To']))

r = Send()
# #
#
#
# def send_mail():
#     login = str(input('Enter your email: '))
#     password = input('Enter password from post: ')
#     toaddr = str(input('Enter email to send: '))
#     subject = input('Enter subject of mail')
#     massage = input('Enter massange: ')
#
#     msg = MIMEMultipart()
#     msg['Subject'] = subject
#     msg['From'] = login
#     msg['To'] = toaddr
#     msg.attach(MIMEText(massage, 'plain'))
#
#     server = smtplib.SMTP('smtp.gmail.com: 587')
#     server.starttls()
#     server.login(login, password)
#     server.sendmail(login, toaddr, msg.as_string())
#     server.quit()
#     print("successfully sent email to %s:" % (msg['To']))


root.mainloop()

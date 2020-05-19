
from app import mail
from flask_mail import  Message
from flask import current_app, render_template
import threading

def send_async_mail(app,msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            raise e



def send_mail(to,subject,template,**kwargs):
    msg = Message('[鱼书]'+''+subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template,**kwargs)
    app = current_app._get_current_object()
    thr = threading.Thread(target=send_async_mail,args=[app,msg])
    thr.start()




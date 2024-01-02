from threading import Thread
from flask_mail import Messaje
from flask import current_app,render_template


'''def confirmacion_compra(mail,usuario,libro):
    try:
        messaje=Messaje('Confirmación de compra de libro',
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[''])
        messaje.html=render_template('emails/confirmacion_compra.html',usuario=usuario,libro=libro)
        mail.send(messaje)
    except Exception as ex:
        raise Exception(ex)'''
def confirmacion_compra(app,mail,usuario,libro):
    try:
        messaje=Messaje('Confirmación de compra de libro',
        sender=current_app.config['MAIL_USERNAME'],
        recipients=['emailreceptor@gmail.com'])
        messaje.html=render_template('emails/confirmacion_compra.html',usuario=usuario,libro=libro)
        thread=Thread(target=envio_email_async, args=[app,mail,messaje])
        thread.start()
        
    except Exception as ex:
        raise Exception(ex)
    
def envio_email_async(app,mail,messaje):
    with app.app_context():
        mail.send(messaje)
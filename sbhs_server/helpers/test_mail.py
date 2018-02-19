import smtplib

def email(to, subject, message):
    smtpserver = smtplib.SMTP()
    smtpserver.connect('smtp-auth.iitb.ac.in', 25)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.esmtp_features['auth']='LOGIN DIGEST-MD5 PLAIN'
    smtpserver.login('rupakrokade', '*rupak*iit')

    header = 'To: ' + to + '\n' + 'From: ' + 'rupakrokade' + '@iitb.ac.in\n' + 'Subject: ' + subject +' \n'
    msg = header + '\n' + message + '\n\n'
    smtpserver.sendmail('rupakrokade' + '@iitb.ac.in', to, msg)
    smtpserver.close()

email('rupakrokade@gmail.com','hello','hello')

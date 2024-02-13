import random
# Import modules
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
## The pandas library is only for generating the current date, which is not necessary for sending emails
import pandas as pd


def sending_OTP(email_too):
    OTP = random.randint(100000, 999999)
    print(OTP)

    # Password of the email app thing "uomt fapc dpla uowz"

    otp_text = "<h1>{}</h1>".format(OTP)

    # Define the HTML document
    html = '''

    <html>
    <head>
    <style>

    body {
      background-color: #f2f2f2;
      font-family: Arial;  
    }

    h1, h2 {
      color: white;
    }

    h1 {
      font-size: 48px;
      text-align: center; 
      text-transform: uppercase;
      text-shadow: 1px 1px 1px #bbb;
    }

    p {
      font-size: 16px;
      line-height: 1.5;  
    }

    .container {
      max-width: 600px;
      margin: 0 auto; 
      background-color: white;
      padding: 20px;
      border-radius: 5px;
      box-shadow: 2px 4px 16px rgba(0,0,0,.2); 
    }

    </style>  
    </head>

    <body>

    <div class="container">

    <h2>Dear Declan,</h2>

    <p>You recently requested to reset your password for your account on Market Scout.</p>

     <p>To continue resetting your password, please enter the following 6-digit OTP:</p>

              <h1>{}</h1><br>


              <p>This OTP is valid for only 10 minutes. Please enter this code on the reset password page to verify your identity.</p>

                <p>If you did not request a password reset, please ignore this email. </p>

              <p>Regards,</p> 
               <p> Declan (Lead Developer)</p>
              <p>Market Scout Support Team</p> 

    </div>

    </body>
    </html>
        '''

    html = html.replace("{}", otp_text)
    print("100")

    # Set up the email addresses and password. Please replace below with your email address and password
    email_from = 'marketscout2@gmail.com'
    email_password = 'mavv okip gbnj myjb '
    # email_too = 'scarletphantom623@gmail.com'

    # Generate today's date to be included in the email Subject
    date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

    print("120")
    # Create a MIMEMultipart class, and set up the From, To, Subject fields
    email_message = MIMEMultipart()
    email_message['From'] = email_from
    email_message['To'] = email_too
    email_message['Subject'] = f' Password Reset Request - {date_str}'
    print("150")

    # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
    email_message.attach(MIMEText(html, "html"))
    # Convert it as a string
    email_string = email_message.as_string()

    print("200")

    # Connect to the Gmail SMTP server and Send Email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, email_password)
        server.sendmail(email_from, email_too, email_string)
    print("Done")
    return OTP



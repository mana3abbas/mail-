import boto3
from botocore.exceptions import ClientError

def send_email():
    SENDER = "mona.samir.abbas@gmail.com" 
    RECIPIENT = "mona.samir.abbas@gmail.com" 

    
    AWS_REGION = "us-east-1"

    # The subject line for the email.
    SUBJECT = "Caution!!"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Hey Hi...\r\n"
                "This email was sent with Amazon SES using the "
                
                )
                
    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>Hey Hi Reciptient</h1>
    
        <h2>Be aware that a new chnage was made to your terraform state file</h2>
    </body>
    </html>
                """            

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
        
                        'Data': BODY_HTML
                    },
                    'Text': {
        
                        'Data': BODY_TEXT
                    },
                },
                'Subject': {

                    'Data': SUBJECT
                },
            },
            Source=SENDER
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

def lambda_handler(event, context):
    # TODO implement
    send_email()

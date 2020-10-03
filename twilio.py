from twilio.twiml.messaging_response import MessagingResponse

resposnse = MessagingResponse()
msg = response.message()
msg.boby('some text')
#whatsapp_chatbot

You need to install 
 python 3.6 and above, twilio, flask and ngrok in your laptop


mkdir whatsapp-chatbot #create a directory for our chatbot

cd whatsapp-bot #navigate into the chabot directory you created

virtualenv env #create a virtual environment

source env/bin/activate #activate the virtual environment

(env) $ pip3 install twilio flask requests #install twilio inside the virtual environment

#usage

On Twilio Console, click on Programmable SMS, then on WhatsApp, and finally on Sandbox. 
Copy the https:// URL from the ngrok output and then paste it on the “When a message comes in” field.
Our chatbot is exposed under the / URL. Make sure the request method is set to HTTP Post. 
Don’t forget to click the red Save button at the bottom of the page to record these changes.

You can start sending messages to the chatbot from the smartphone that you connected to the sandbox. 

Links
1. https://www.twilio.com/

2. https://flask.palletsprojects.com/

3. https://ngrok.com/

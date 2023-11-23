# Import necessary libraries
import os
import tweepy
import pywhatkit
from twilio.rest import Client
import smtplib
import ssl
from email.message import EmailMessage
import openai
import wikipedia
import pyttsx3
import pygame
import cv2

# Function to fetch and print Twitter trends
def twitter():
    # API keys for Twitter authentication
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""

    # Authorization using Tweepy library
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # WOEID of India for Twitter trends
    woeid = 23424977

    # Fetching trends
    trends = api.get_place_trends(id=woeid)

    # Printing top trends
    print("The top trends for the location are:")
    for value in trends:
        for trend in value['trends']:
            print(trend['name'])

# Function to send WhatsApp message using pywhatkit
def whatsApp():
    phone_number = "+91" + "1234567890"
    pywhatkit.sendwhatmsg(phone_number, "test3", 0, 6)

# Function to send SMS using Twilio
def sms():
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)

    # Creating and sending a message using Twilio
    message = client.messages.create(
        body="This is sent from Python",
        from_="your_twilio_phone_number",
        to="recipient_phone_number",
    )
    print(message.sid)

# Function to send an email using smtplib and ssl
def email():
    # Email configuration
    email_sender = 'xyz@gmail.com'
    email_password = 'abc'  # Sender's email password or app password
    email_receiver = ['farman@gmail.com', 'ayush@gmail.com', 'papnesh@gmail.com', ]  # Recipient's email address

    # Email details
    subject = 'this is a python task '  # Subject of the email
    body = """
        I have completed python task successfully again by setting up environment variable.
    """  # Body of the email (multi-line string)

    # Create an EmailMessage object to construct the email
    em = EmailMessage()
    em['From'] = email_sender  # Set the sender's email address
    em['To'] = email_receiver  # Set the recipient's email address
    em['Subject'] = subject  # Set the subject of the email
    em.set_content(body)  # Set the email body

    # Create an SSL context for secure communication with the SMTP server
    context = ssl.create_default_context()

    # Connect to the Gmail SMTP server using SSL and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)  # Log in to the sender's Gmail account
        smtp.sendmail(email_sender, email_receiver, em.as_string())  # Send the email

# Function to interact with OpenAI GPT-3
def chatgpt():
    # Set your OpenAI API key here
    api_key = "your-api-key"

    # Function to interact with GPT-3
    def chat_with_gpt3(prompt, max_tokens=50):
        openai.api_key = api_key
        response = openai.Completion.create(
            engine="text-davinci-002",  # You can choose a different engine if needed
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text

    # Example usage
    user_input = "Tell me a joke:"
    response = chat_with_gpt3(user_input, max_tokens=100)
    print(response)

# Function to search and read a summary from Wikipedia
def wikipedia():
    command = input("search :")
    response = wikipedia.summary(command)
    pyttsx3.speak(response)

# Function to play a video using OpenCV
def play_video(file_path):
    # Open the video file
    cap = cv2.VideoCapture(file_path)

    # Check if the video file is opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        return

    # Read the video frame by frame and display it
    while True:
        ret, frame = cap.read()

        # Break the loop if the video is finished
        if not ret:
            break

        # Display the frame
        cv2.imshow('Video Player', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()
    

def play_audio(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Add a delay to ensure the program doesn't exit immediately
    pygame.time.delay(5000)  # Delay for 5 seconds (adjust as needed)

    pygame.mixer.quit()
    pygame.quit()


# Main function to provide a menu and call respective functions based on user input
def main():
    print("List of operations you can perform:")
    print("1. Open Notepad")
    print("2. Open Chrome")
    print("3. Send Email")
    print("4. Send WhatsApp")
    print("5. Send SMS")
    print("6. Find trends on Twitter")
    print("7. Connect with GPT")
    print("8. Play Audio")
    print("9. Play Video")

    print("Enter your choice:")
    x = input()

    if "notepad" in x.lower():
        os.system("notepad")
    elif "chrome" in x.lower():
        os.system("chrome")
    elif "whatsapp" in x.lower():
        whatsApp()
    elif "email" in x.lower():
        email()
    elif "twitter" in x.lower():
        twitter()
    elif "wikipedia" in x.lower():
        wikipedia()
    elif "chatgpt" in x.lower():
        chatgpt()
    elif "audio" in x.lower():
        print("enter your audio file path")
        path=input()
        play_audio(path)
    elif "video" in x.lower():
        print("enter your video file path")
        path=input()
        play_video(path)

# Entry point for the script
if __name__ == "__main__":
    main()

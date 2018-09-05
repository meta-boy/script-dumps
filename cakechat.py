import requests


# _HOST_FQDN = '127.0.0.1' will use this on a local instance
# _SERVER_PORT = '8080'

DEFAULT_EMOTION = "neutral"
BASE_URL  = f"https://cakechat.replika.ai/cakechat_api/v1/actions/get_response"

def message_parser(msg:str):
    """This function does the chat-thingy"""
    body = {"context": msg, "emotion": DEFAULT_EMOTION}
    r = requests.post(BASE_URL, data=body)
    json = r.text
    return json #will work on this once i get my own local  instance of cakechat, for now it returns 500


def intializer():
    """Initializes the chat"""
    greeting_msg = "hello" #you can change this to anything
    print(message_parser(greeting_msg))


def repeater():
    while True: #haaaaaaaaaaaaah
        msg = input(">")
        response = message_parser(msg)
        print("\n" + response)


intializer()

repeater()
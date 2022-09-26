# WebEx-Teams Bot Integration for DNAC

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://testing-developer.cisco.com/codeexchange/github/repo/lingjshi/DNAC-Webex-Teams-Bot-App) [![Run in VSCode](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-runable-icon.svg)](https://testing-developer.cisco.com/codespace/?id=devenv-vscode-base&community=true&type=vscode&GITHUB_SOURCE_REPO=https://github.com/lingjshi/DNAC-Webex-Teams-Bot-App)

This application aims to provide a simple integration of the Cisco DNA-Center APIs with Cisco WebEx-Teams's Bot.
The Bot provides a chat like interface to give visibility into your network to run some basic commands and see the result right on the Chat Space (Desktop and Mobile Client)



![Alt text](https://github.com/lingjshi/DNAC-Webex-Teams-Bot-App/blob/master/server/sampleScreen.png?raw=true "Sample Chat Session")


## Making the App work

### Pre-requisites 
1.Python3

2.Requirements `pip install -r requirements.txt`


### Creating and configuring the Bot

#### 1.Create a bot in WebEx Team's Site
https://developer.webex.com/bots.html

To register a Bot, you’ll need to be logged in to WebEx For-Developers Page with a “real” user – each bot needs to be tied to an actual user account. Adding one is extra simple, On the page, select “Create a Bot”; there’s only a couple fields to fill out

Display Name is how you want the bot to show up in a room (like “bot-a-dna”); 
Bot Username is the email address, since every Spark user is registered under an email – this should be similar to the Display Name, but it can be unique.  Note that you are not populating the entire email – they will always end with @sparkbot.io, can’t make on with a gmail.com email or anything similar, so you’re just adding the prefix. The username prefix does need to be unique; if you don’t get a green check at the end of the @sparkbot.io reference, then the username was already taken. The Icon is the avatar for the bot, which will also show inside a room. 

Once the bot is created, you’ll need to save the access token that is provided – keep it someplace safe.  The token effectively never expires (it’s good for 100 years) but if you forget it, you’ll have to generate a new one. There’s no way to get it back.

#### 2.Create an Outbound Webhook

Your webhook URL needs to be accessible on the public Internet – if you want to use your local machine, you can use a service like Ngrok to make your personal machine accessible to the world on a specific port for free.

But that means the webhook only works when you machine is up and live. 

Once you have an endpoint to use, create the webhook using the request on this page.
https://developer.ciscospark.com/endpoint-webhooks-post.html


Make sure that the bearer token used in creating the webhook is the bearer token of the bot. 
You’ll need to know the ‘roomId’ of the room the bot is hanging out in, and you’ll need to know your own ‘targetUrl’ (the Ngrok link etc.); you’ll also want to set the ‘resource’ to messages and the ‘event’ to created. Here’s what the Webhook should look like once it’s been created:
	
```json
{
  "items": [
    {
      "id": "<Bearer-Token>",
      "name": "botaDna",
      "targetUrl": "http://b4bcf212.ngrok.io",
      "resource": "messages",
      "event": "created",
      "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY",
      "createdBy": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lZTY1ZTZiMC1kNzU2LTQxZWMtYjg3MC1hOTNkMjY3OTBhMDk",
      "appId": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL0MyNzljYjMwYzAyOTE4MGJiNGJkYWViYjA2MWI3OTY1Y2RhMzliNjAyOTdjODUwM2YyNjZhYmY2NmM5OTllYzFm",
      "ownedBy": "creator",
      "status": "active",
      "created": "2018-05-11T05:37:18.828Z"
    }
  ]
}
```

### Running the Code in VSCode

#### 1.Open the VSCode DevEnv

This code has been cloned in VSCode automatically.

#### 2.Setup the dependencies in the terminal

```bash
pip install -r requirements.txt
```

#### 3.Run the application using python3 to start the server

```bash
cd server
python3 botADna.py
```


#### Chat in the Webex (with codeexchange@webex.bot)

Common commands:
	
##### hello
	Greets the user and says what next could he do to connect to a cluster to start seeing his network data
##### connect,`<ip>`,`<username>`,`<password>`
	To connect to a cluster to see its data
##### list-devices
	Lists Devices on the network
##### device-by-id `<DEVICE ID>`
	Current information about a network device by device ID.
##### device-by-mac `<MAC Address>`
	Current information about a network device by device MAC address
##### help
	Get the list of commands supported
##### logout
	Logout of the cluster connection. Need to login again to run the commands

### API Information

APIs used in this code:

##### Network Device Detail By Device ID
	GET /dna/intent/api/v1/network-device/{Device ID}
##### Network Device Detail By MAC Address
	GET /dna/intent/api/v1/device-detail?searchBy={MAC Address}&identifier=macAddress
##### Network Device List 
	GET /api/v1/network-device  

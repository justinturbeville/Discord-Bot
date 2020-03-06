from discord_webhook import DiscordWebhook

message = raw_input("Enter a message:")
#This take the users input for a message to be sent

webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/685347391582240850/OrpXYxhJJxvEtXJDEWDUWwNoEtxT2btUBl7-lG9lbv3Zqpg1G4njofypigdcVAc2w-Px', content = message)
#uses the webhook to send the message
#the webhook contains the server and channel information

response = webhook.execute()
#sends the message
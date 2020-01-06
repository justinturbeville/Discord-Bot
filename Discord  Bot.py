from discord_webhook import DiscordWebhook

words = input("enter a message: ")

webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/653764204280545280/q-VOLKVnRppuWa-YWmnhxar36OPiacVPr8JgLoW9Cb82WNBHZ93gbCsVm9bxcwUNshaH", content= words)
response = webhook.execute()

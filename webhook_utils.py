from discord_webhook import DiscordWebhook
import discord 
import traceback as tb




def log_error(guild :discord.Guild, e: Exception, type=-1):
    if type==0:
        err_msg = f"Interserver chat error in {guild.name}, traceback: {''.join(tb.format_exception(None, e, e.__traceback__))}"
    elif type==1:
        err_msg = f"Webhook creation error in {guild.name}, traceback: {''.join(tb.format_exception(None, e, e.__traceback__))}"
    elif type==2:
        err_msg = f"Event/job channel error in {guild.name}, traceback: {''.join(tb.format_exception(None, e, e.__traceback__))}"
    else:
        err_msg = f"Unknown exception in {guild.name}, traceback: {e.with_traceback}"
    webhook = DiscordWebhook(url=r"https://discord.com/api/webhooks/928961413198794752/EZOJqg0DaqSBxUGogtQ7eq1qD2eZLcscDeeihN5x2A6hOH87rCQp1ncu6pGw-qfM1HVP",
     content=err_msg)
    webhook.execute()

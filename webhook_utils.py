from discord.ext.commands import context
from discord_webhook import DiscordWebhook, DiscordEmbed
import discord 
import traceback as tb


async def create_webhook_if_not_exist(client, id: int) -> str: 
    channel = await client.fetch_channel(id)
    try:
        webhooks = await channel.webhooks()
        if not webhooks:
            whook = await channel.create_webhook(name="interserver chat")
            return whook.url
        else:
            return webhooks[0].url
    except Exception as e:
        log_error(channel.guild, e, 1)
def send_with_webhook(url, content, server, name,  avatar_url, attachaments):
     allowed_mentions = {
        "parse": []
    }
    webhook = DiscordWebhook(url=url, content=content, username=f"{name} | {server}", avatar_url=f"{avatar_url}", allowed_mentions=allowed_mentions)
    if attachaments:
        embed = DiscordEmbed()
        embed.set_image(url=attachaments[0].url)
        webhook.add_embed(embed=embed)
    webhook.execute()

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

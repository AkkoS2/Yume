# Bibliotecas utilizadas neste arquivo
from utils.envkeys import typohook, sugghook
from discord import Webhook, SyncWebhook
from discord.ext import commands
from datetime import datetime
import discord
import aiohttp


class TypoModal(discord.ui.Modal, title="Report Yume's Typos"):

    typo_title = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Where did you find the typo?",
        required=True,
        max_length=100,
        placeholder="On which command it happened?")

    typo_message = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label="Can you explain it?",
        required=True,
        max_length=500,
        placeholder="Tell me how it should be improved~"
    )

    async def on_submit(self, interaction: discord.Interaction):

        async with aiohttp.ClientSession() as session:

            webhook = Webhook.from_url(f"https://discord.com/api/webhooks/{typohook()}", session=session)

            now = datetime.now()
            typo_e = discord.Embed(color=discord.Color.random())
            typo_e.set_author(name=self.typo_title.value, icon_url=interaction.user.avatar.url)
            typo_e.add_field(name="Typo Founded:", value=f"{self.typo_message.value}", inline=False)
            typo_e.add_field(name="Submitted By:", value=f"{interaction.user.name}", inline=False)
            typo_e.add_field(name="UserID", value=f"{interaction.user.id}", inline=False)
            typo_e.set_footer(text=f"Submitted at: {now.strftime('%Y/%m/%d - %H:%M:%S')}")

            await webhook.send(embed=typo_e)
            await interaction.response.send_message("Thanks for your help! The typo will be fixed as soon as possible!", ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message("I think something went wrong with me, it's not your fault, don't worry!", ephemeral=True)


class SuggestionModal(discord.ui.Modal, title="Have any suggestion to me?"):

    sugg_title = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="What's the name of your suggestion?",
        required=True,
        max_length=100,
        placeholder="Give it a name!")

    sugg_message = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label="Explain it a little bit to me!",
        required=True,
        max_length=500,
        placeholder="Tell me more about it~"
    )

    async def on_submit(self, interaction: discord.Interaction):

        async with aiohttp.ClientSession() as session:

            webhook = Webhook.from_url(f"https://discord.com/api/webhooks/{sugghook()}", session=session)

            now = datetime.now()
            sugg_e = discord.Embed(color=discord.Color.random())
            sugg_e.set_author(name=self.sugg_title.value, icon_url=interaction.user.avatar.url)
            sugg_e.add_field(name="Suggestion:", value=f"{self.sugg_message.value}", inline=False)
            sugg_e.add_field(name="Submitted By:", value=f"{interaction.user.name}", inline=False)
            sugg_e.add_field(name="UserID", value=f"{interaction.user.id}", inline=False)
            sugg_e.set_footer(text=f"Submitted at: {now.strftime('%Y/%m/%d - %H:%M:%S')}")

            await webhook.send(embed=sugg_e)
            await interaction.response.send_message("Thanks for the suggestion! Yume's gonna take good care of it!", ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message("I think something went wrong with me, it's not your fault, don't worry!", ephemeral=True)

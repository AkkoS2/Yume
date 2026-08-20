import discord


class BannerComponent(discord.ui.LayoutView):
    def __init__(self, yume_phrase, global_banner, server_banner, footer):

        super().__init__()


        components = [
                discord.ui.TextDisplay(content = yume_phrase)
        ]

        if global_banner is not None:
            components.append(
                discord.ui.MediaGallery(
                    discord.MediaGalleryItem(media = global_banner)
                )
            )

        if global_banner is not None and server_banner is not None:
            components.append(
                discord.ui.Separator(visible = True, spacing = discord.SeparatorSpacing.small)
            )

        if server_banner is not None:
            components.append(
                discord.ui.MediaGallery(
                    discord.MediaGalleryItem(media = server_banner)
                )
            )

        components.append(
            discord.ui.TextDisplay(content = footer)
        )

        self.container = discord.ui.Container(*components)
        self.add_item(self.container)
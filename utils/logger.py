# Bibliotecas utilizadas neste arquivo
import logging.handlers
import logging
import discord


class YLogger:

    yume_logger = logging.getLogger('discord')
    yume_logger.setLevel(logging.INFO)
    logging.getLogger('discord.http').setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename='log-yume.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,
        backupCount=5
    )

    date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('%(asctime)s: - %(name)s - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)
    yume_logger.addHandler(handler)

    log_handler = None

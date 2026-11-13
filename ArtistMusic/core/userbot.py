from pyrogram import Client

from ArtistMusic import config, logger


class Userbot:
    """Manages the Telegram assistant account(s) used for voice-chat playback."""

    def __init__(self):
        self.clients = []
        self.one = Client(
            name="DKMusicAssistant1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=config.SESSION1,
        )
        self.two = Client(
            name="DKMusicAssistant2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=config.SESSION2,
        )
        self.three = Client(
            name="DKMusicAssistant3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=config.SESSION3,
        )

    async def boot_client(self, number: int, client: Client):
        try:
            await client.start()
            try:
                await client.send_message(config.LOGGER_ID, f"DK Music assistant {number} started")
            except Exception as exc:
                logger.warning(f"Assistant {number} cannot send to LOGGER_ID: {exc}")
            me = client.me
            client.id = me.id
            client.name = me.first_name
            client.username = me.username
            client.mention = me.mention
            self.clients.append(client)
            logger.info(f"Assistant {number} started as @{client.username}")
        except Exception as exc:
            logger.error(f"Assistant {number} failed to start: {exc}")
            raise

    async def boot(self):
        sessions = [
            (1, self.one, config.SESSION1),
            (2, self.two, config.SESSION2),
            (3, self.three, config.SESSION3),
        ]
        for number, client, session in sessions:
            if session:
                await self.boot_client(number, client)

    async def exit(self):
        for client in (self.one, self.two, self.three):
            try:
                if client.is_connected:
                    await client.stop()
            except Exception as exc:
                logger.warning(f"Error stopping assistant: {exc}")
        logger.info("DK Music assistants stopped.")

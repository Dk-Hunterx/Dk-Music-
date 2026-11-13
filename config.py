from os import getenv
from typing import List
from dotenv import load_dotenv

load_dotenv()


def _int_env(name: str, default: int = 0) -> int:
    try:
        return int(getenv(name, str(default)).strip() or default)
    except (TypeError, ValueError):
        return default


class Config:
    def __init__(self):
        self.API_ID: int = _int_env("API_ID")
        self.API_HASH: str = getenv("API_HASH", "").strip()
        self.BOT_TOKEN: str = getenv("BOT_TOKEN", "").strip()
        self.LOGGER_ID: int = _int_env("LOGGER_ID")
        self.OWNER_ID: int = _int_env("OWNER_ID")

        self.MONGO_URL: str = getenv("MONGO_DB_URI", "").strip()

        self.DURATION_LIMIT: int = _int_env("DURATION_LIMIT", 300) * 60
        self.QUEUE_LIMIT: int = _int_env("QUEUE_LIMIT", 30)
        self.PLAYLIST_LIMIT: int = _int_env("PLAYLIST_LIMIT", 20)

        self.SESSION1: str = getenv("STRING_SESSION", "").strip()
        self.SESSION2: str = getenv("STRING_SESSION2", "").strip()
        self.SESSION3: str = getenv("STRING_SESSION3", "").strip()

        self.SUPPORT_CHANNEL: str = getenv("SUPPORT_CHANNEL", "https://t.me/+PJFhQTIsbdY3YjU1")
        self.SUPPORT_CHAT: str = getenv("SUPPORT_CHAT", "https://t.me/+sEv0qBVqxjc0NDhl")

        self.EXCLUDED_CHATS: List[int] = self._parse_excluded_chats()
        self.AUTO_END: bool = self._str_to_bool(getenv("AUTO_END", "False"))
        self.AUTO_LEAVE: bool = self._str_to_bool(getenv("AUTO_LEAVE", "False"))
        self.THUMB_GEN: bool = self._str_to_bool(getenv("THUMB_GEN", "True"))
        self.VIDEO_PLAY: bool = self._str_to_bool(getenv("VIDEO_PLAY", "True"))
        self.VIDEO_MAX_HEIGHT: int = self._parse_video_height()

        self.ARTISTBOTS_API_URL: str = getenv("ARTISTBOTS_API_URL", "").strip()
        self.ARTISTBOTS_KEY: str = getenv("ARTISTBOTS_KEY", "").strip()
        self.ENABLE_API: bool = self._str_to_bool(getenv("ENABLE_API", "False"))
        self.ENABLE_COOKIES_FALLBACK: bool = self._str_to_bool(getenv("ENABLE_COOKIES_FALLBACK", "True"))
        self.API_TIMEOUT: int = _int_env("API_TIMEOUT", 60)
        self.API_STREAM_TIMEOUT: int = _int_env("API_STREAM_TIMEOUT", 300)
        self.COOKIES_URL: List[str] = self._parse_cookies()
        # Private Netscape-format YouTube cookies supplied as a Railway secret.
        self.YOUTUBE_COOKIES: str = getenv("YOUTUBE_COOKIES", "")

        self.DEFAULT_THUMB: str = getenv("DEFAULT_THUMB", "https://graph.org/file/e9b9081be519f0e1413dd-a0fd9c7fc36c010a1c.mp4")
        self.PING_IMG: str = getenv("PING_IMG", self.DEFAULT_THUMB)
        self.START_IMG: str = getenv("START_IMG", self.DEFAULT_THUMB)
        self.RADIO_IMG: str = getenv("RADIO_IMG", self.DEFAULT_THUMB)
        self.EXCLUDED_USERNAMES: List[str] = getenv("EXCLUDED_USERNAMES", "").split()

    def _parse_video_height(self) -> int:
        height = _int_env("VIDEO_MAX_HEIGHT", 1080)
        return 0 if height <= 0 else max(480, min(height, 2160))

    def _parse_excluded_chats(self) -> List[int]:
        values = getenv("EXCLUDED_CHATS", "")
        return [int(x.strip()) for x in values.split(",") if x.strip().lstrip("-").isdigit()]

    def _parse_cookies(self) -> List[str]:
        values = getenv("COOKIE_URL", "")
        allowed = ("batbin.me", "pastebin.com", "paste.ee", "rentry.co", "raw.githubusercontent.com")
        return [u.strip() for u in values.split() if u.strip() and any(host in u for host in allowed)]

    @staticmethod
    def _str_to_bool(value: str) -> bool:
        return value.lower() in ("true", "1", "yes", "y", "on")

    def check(self) -> None:
        required = {
            "API_ID": self.API_ID,
            "API_HASH": self.API_HASH,
            "BOT_TOKEN": self.BOT_TOKEN,
            "MONGO_DB_URI": self.MONGO_URL,
            "LOGGER_ID": self.LOGGER_ID,
            "OWNER_ID": self.OWNER_ID,
            "STRING_SESSION": self.SESSION1,
        }
        missing = [key for key, value in required.items() if not value]
        if missing:
            raise SystemExit("Missing required environment variables: " + ", ".join(missing))
        if self.ENABLE_API and (not self.ARTISTBOTS_API_URL or not self.ARTISTBOTS_KEY):
            raise SystemExit("ENABLE_API is True but ARTISTBOTS_API_URL or ARTISTBOTS_KEY is missing.")


config = Config()

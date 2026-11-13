from pyrogram import types
from pyrogram.enums import ButtonStyle

from ArtistMusic import app, config


HELP = {
    "music": (
        "<b>🎵 MUSIC COMMANDS</b>\n\n"
        "<blockquote>/play [query or URL] — queue audio\n"
        "/playforce [query or URL] — interrupt and play audio now\n"
        "/cplay [query or URL] — queue audio in linked channel\n"
        "/cplayforce [query or URL] — force audio in linked channel\n"
        "/vplay [query or URL] — queue video\n"
        "/vplayforce [query or URL] — interrupt and play video now\n"
        "/queue — show upcoming tracks\n"
        "/pause · /resume · /skip · /stop — playback controls</blockquote>"
    ),
    "admin": (
        "<b>🔐 GROUP ADMIN COMMANDS</b>\n\n"
        "<blockquote>/auth — authorize a member\n"
        "/unauth — remove authorization\n"
        "/authlist — list authorized members\n"
        "/reload — refresh the group admin cache\n"
        "/channelplay linked — enable linked-channel playback\n"
        "/channelplay disable — disable channel playback</blockquote>"
    ),
    "sudo": (
        "<b>👑 SUDO COMMANDS</b>\n\n"
        "<blockquote>/addsudo · /delsudo · /sudolist · /sudopanel\n"
        "/gban · /ungban · /gbanlist\n"
        "/broadcast — send a message to registered groups</blockquote>"
    ),
    "broadcast": (
        "<b>📢 BROADCAST</b>\n\n"
        "<blockquote>Reply to a text, photo, video, audio, or document with /broadcast. "
        "Inline URL buttons on the replied message are copied too.\n"
        "/broadcast -user — also include users\n"
        "/stop_gcast — stop an active broadcast</blockquote>"
    ),
}


class Inline:
    def __init__(self):
        self.ikm = types.InlineKeyboardMarkup
        self.ikb = types.InlineKeyboardButton

    def cancel_dl(self, text):
        return self.ikm([[self.ikb(text=f"✗ {text}", callback_data="cancel_dl", style=ButtonStyle.DANGER)]])

    def controls(self, chat_id: int, status: str = None, timer: str = None, remove: bool = False):
        keyboard = []
        if status or timer:
            keyboard.append([self.ikb(text=status or timer, callback_data=f"controls status {chat_id}", style=ButtonStyle.PRIMARY)])
        if not remove:
            keyboard.append([
                self.ikb(text="Ⅱ", callback_data=f"controls pause {chat_id}", style=ButtonStyle.PRIMARY),
                self.ikb(text="▶", callback_data=f"controls resume {chat_id}", style=ButtonStyle.PRIMARY),
                self.ikb(text="⏭", callback_data=f"controls skip {chat_id}", style=ButtonStyle.PRIMARY),
                self.ikb(text="■", callback_data=f"controls stop {chat_id}", style=ButtonStyle.DANGER),
            ])
            keyboard.append([self.ikb(text="✕ Close", callback_data=f"controls close {chat_id}", style=ButtonStyle.DANGER)])
        return self.ikm(keyboard)

    def help_markup(self, _lang: dict, back: bool = False):
        if back:
            return self.ikm([[self.ikb(text="‹ Back", callback_data="help_main", style=ButtonStyle.SUCCESS)]])
        rows = [
            [self.ikb(text="🎵 Music", callback_data="help_music", style=ButtonStyle.PRIMARY),
             self.ikb(text="🔐 Group Admin", callback_data="help_admin", style=ButtonStyle.PRIMARY)],
            [self.ikb(text="👑 Sudo", callback_data="help_sudo", style=ButtonStyle.PRIMARY),
             self.ikb(text="📢 Broadcast", callback_data="help_broadcast", style=ButtonStyle.PRIMARY)],
            [self.ikb(text="Support", url=config.SUPPORT_CHAT),
             self.ikb(text="Updates", url=config.SUPPORT_CHANNEL)],
        ]
        return self.ikm(rows)

    def help_text(self, _lang: dict, category: str):
        return HELP.get(category)

    def langs_markup(self):
        return self.ikm([
            [self.ikb(text="🇬🇧 English", callback_data="setlang_en"),
             self.ikb(text="🇳🇵 Nepali", callback_data="setlang_ne")],
            [self.ikb(text="‹ Back", callback_data="start", style=ButtonStyle.SUCCESS)],
        ])

    def ping_markup(self, text: str):
        return self.ikm([
            [self.ikb(text=text, callback_data="ping_refresh", style=ButtonStyle.PRIMARY)],
            [self.ikb(text="Support", url=config.SUPPORT_CHAT),
             self.ikb(text="Updates", url=config.SUPPORT_CHANNEL)],
            [self.ikb(text="Add me to your group", url=f"https://t.me/{app.username}?startgroup=true", style=ButtonStyle.SUCCESS)],
        ])

    def play_queued(self, chat_id: int, item_id: str, _text: str):
        return self.ikm([[
            self.ikb(text="▶", callback_data=f"controls resume {chat_id} {item_id}"),
            self.ikb(text="Ⅱ", callback_data=f"controls pause {chat_id} {item_id}"),
            self.ikb(text="⏭", callback_data=f"controls skip {chat_id} {item_id}"),
            self.ikb(text="■", callback_data=f"controls stop {chat_id} {item_id}"),
        ]])

    def queue_markup(self, chat_id: int, _text: str, playing: bool):
        action = "pause" if playing else "resume"
        return self.ikm([[self.ikb(text=_text, callback_data=f"controls {action} {chat_id} q", style=ButtonStyle.SUCCESS)]])

    def settings_markup(self, lang: dict, admin_only: bool, force_admin: bool, language: str, chat_id: int):
        return self.ikm([[self.ikb(text="Settings are managed by group admins", callback_data=f"controls status {chat_id}")]])

    def start_key(self, lang: dict, private: bool = False):
        return self.ikm([
            [self.ikb(text="➕ Add to Group", url=f"https://t.me/{app.username}?startgroup=true", style=ButtonStyle.SUCCESS)],
            [self.ikb(text="Help", callback_data="help")],
            [self.ikb(text="Support", url=config.SUPPORT_CHAT),
             self.ikb(text="Updates", url=config.SUPPORT_CHANNEL)],
            [self.ikb(text="Developer", url="https://t.me/massom_bacha")],
        ])

    def yt_key(self, link: str):
        return self.ikm([[
            self.ikb(text="Copy link", copy_text=link, style=ButtonStyle.PRIMARY),
            self.ikb(text="Open in YouTube", url=link, style=ButtonStyle.DANGER),
        ]])

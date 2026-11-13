# DK Music Bot

A streamlined Telegram voice-chat music bot based on the supplied Dk-music source. The original repository is not modified.

**Developer:** [@massom_bacha](https://t.me/massom_bacha)  
**Support:** [Support group](https://t.me/+sEv0qBVqxjc0NDhl)  
**Updates:** [Updates channel](https://t.me/+PJFhQTIsbdY3YjU1)

## Features

- Audio playback: `/play`, `/cplay`
- Video playback: `/vplay`
- Force playback: `/playforce`, `/cplayforce`, `/vplayforce`
- Force commands interrupt the current track and start the requested track immediately. Tracks already waiting in the queue remain queued.
- Playback controls: `/pause`, `/resume`, `/skip`, `/stop`, `/queue`
- Group authorization: `/auth`, `/unauth`, `/authlist`, `/reload`
- Sudo controls: `/addsudo`, `/delsudo`, `/sudolist`, `/sudopanel`
- Sudo-only global bans: `/gban`, `/ungban`, `/gbanlist`
- Sudo-only broadcasts to registered groups, including text, photos, videos, audio and documents. Reply to a message with `/broadcast`; inline URL buttons on the replied message are preserved.
- Channel playback is configured by a group admin with `/channelplay linked`.

## Required environment variables

Add these to Railway/Render Variables (or your local `.env`):

| Variable | Description |
|---|---|
| `API_ID` | Telegram API ID from [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | Telegram API hash |
| `BOT_TOKEN` | Bot token from [@BotFather](https://t.me/BotFather) |
| `OWNER_ID` | Your Telegram numeric user ID |
| `LOGGER_ID` | Telegram log group ID; add the bot there as admin |
| `MONGO_DB_URI` | MongoDB Atlas connection URI |
| `STRING_SESSION` | Pyrogram string session for the assistant user account |

Only these seven values are required. `STRING_SESSION2`, `STRING_SESSION3`, and `COOKIE_URL` are optional. See [`.env.example`](.env.example).

**Important:** Keep tokens, API hashes, MongoDB credentials, session strings and cookies private. Never commit a real `.env` file.

## Deploy on Railway

1. Create a Railway project from this repository.
2. Add the seven required variables above in **Variables**.
3. Deploy using the included Dockerfile. Railway will install FFmpeg and Python dependencies.
4. Add the bot to your Telegram log group and make it an administrator.
5. Add the bot and assistant account to your target group; promote the bot with voice-chat permissions.
6. Start a voice chat, then use `/play song name`.

## Deploy on Render

Use the included `render.yaml` blueprint and set the same seven required variables. A free web service may sleep; use a suitable paid plan for continuous operation.

## Local / Termux notes

Install Python dependencies and FFmpeg, copy `.env.example` to `.env`, fill the variables, then run:

```bash
pip install -r requirements.txt
python3 -m ArtistMusic
```

Termux may require the platform-specific FFmpeg and PyTgCalls setup.

## YouTube extraction

Direct yt-dlp extraction is enabled by default. YouTube may change its anti-bot and extraction behavior, so playback is not guaranteed for every video or region. If needed, configure `COOKIE_URL` with a private cookie-host URL. Do not publish or share account cookies. An optional external extractor API can be enabled by setting `ENABLE_API=True` and supplying its endpoint and key.

## Credits and license

This project retains the upstream MIT license. It is a customized derivative of the ArtistMusic / Dk-music codebase; see [LICENSE](LICENSE) for the license terms and copyright notices.

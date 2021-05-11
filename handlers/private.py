from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hello ji, I'm {bn} 🎵

I can play music in your group's voice call.Developed by [❀͜͡𝄟 Cute Baby](https://t.me/Unstoppable_Remix).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ 𝗦𝗼𝗺𝗲𝗼𝗻𝗲'𝘀 𝗖𝗵𝗼𝗺𝘂 𝗛𝗲𝗿𝗲 ✨", url="https://t.me/unstoppable_Remix")
                ],[ 
                    InlineKeyboardButton(
                        "⚙️ 𝗣𝘂𝘀𝗵 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 ⚙️", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Infinity_BOTs")
                ]
            ]
        )
   )



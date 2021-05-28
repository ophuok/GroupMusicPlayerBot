from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Namaste, It's {bn} 

✵ I can play music in your groups voice call. You can add me in your group Freely .
✵ Here are my some extra commands : 
☞︎︎︎ /play «song name»
☞︎︎︎ /song «song name»
☞︎︎︎ /search «query»
☞︎︎︎ other commands you can get in assistant by sending /help.
☞︎︎︎ Developed by [❀͜͡𝄟 Cute Baby](https://t.me/Unstoppable_Remix).
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ 𝗠𝘆 𝗗𝗲𝘃 𝗛𝗲𝗿𝗲 ✨", url="https://t.me/unstoppable_remix")
                ],[ 
                    InlineKeyboardButton(
                        "⚙️ 𝗣𝘂𝘀𝗵 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 ⚙️", url="https://t.me/CuteMonaBot?startgroup=true"
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
                        "Owner🚶", url="https://t.me/Unstoppable_Remix")
                ]
            ]
        )
   )



import asyncio
import importlib
from pyrogram import idle
from SANKIRIGHT import SANKIRIGHT
from SANKIRIGHT.modules import ALL_MODULES

LOGGER_ID = -1002100433415

loop = asyncio.get_event_loop()

async def sanki_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("SANKIRIGHT.modules." + all_module)
    print("𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗌𝗍𝖺𝗋𝗍")
    await idle()
    print("𝖻𝖺𝗁𝖺𝗇𝖼𝗁𝗈𝖽 𝖯𝗂𝗋𝗈 𝖢𝗈𝖽𝖾𝗋 𝗄𝗋𝗅𝗈 𝖾𝖽𝗂𝗍 𝖺𝖺 𝗀𝗒𝖺 𝗇 𝖾𝗋𝗋𝗈𝗋 𝖺𝖺𝖻 𝗃𝖺𝗄𝖾 𝗀𝖺𝗇𝖽 𝗆𝖺𝗋𝗐𝖺𝗈 𝗂𝗌𝗌𝖾 @TSGCODER")
    await SANKIRIGHT.send_message(LOGGER_ID, "**𝖨 𝖺𝗆 𝖺𝗅𝗂𝗏𝖾 𝖡𝖺𝖻𝗒 𝖸𝗈𝗎𝗋 𝖡𝗈𝗍 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝖣𝖾𝗉𝗅𝗈𝗒 \n Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ  [ ⌯ 𝐒 𝐀 𝐍 𝐊 𝐈 🜲 💸 𝐱𝗗 ](https://t.me/TSGCOFER)**")

if __name__ == "__main__":
    loop.run_until_complete(sanki_boot())
    

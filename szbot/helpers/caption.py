from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

imgcaption = """
☘️ **Random Logo Created Successfully**✅
◇───────────────◇
🔥 **Created by** :  [Nipun Contact Bot](https://t.me/NiupunDinujaya_bot)
🌷 **Requestor** : {message.from_user.username}
⚡️ **Powered By **: `【NIPUN】´
◇───────────────◇
©2022  **All Right Reserved**⚠️️
"""
repmark = InlineKeyboardMarkup(
      [
        [
        InlineKeyboardButton(text="➕Add me to your group ➕", url=f"http://t.me/NiupunDinujaya_bot?startgroup=botstart") 
        ],
        [
         InlineKeyboardButton(text="Owner", url=f"https://t.me/NiupunDinujaya") 
        ]
      ]      
    )

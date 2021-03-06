from szbot import sz
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery







START_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("π About π", callback_data="aboutmenu"),
                    InlineKeyboardButton("ποΈ Help ποΈ", callback_data="helpmenu")
                ],
                [
                    InlineKeyboardButton("π» Owner π»", url="https://t.me/NiupunDinujaya"),
                    InlineKeyboardButton("π€¦ββοΈ Support π€¦ββοΈ", url="https://t.me/MrItzme")
                ],
                [
                    InlineKeyboardButton("β Add me to your group β", url="http://t.me/NiupunDinujaya_bot?startgroup=botstart") 
                ]
            ]
        )

GROUP_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ποΈ Help ποΈ", callback_data="helpmenu")
                ],
                [
                    InlineKeyboardButton("π£οΈUpdate channel", url="https://t.me/szteambots")
                ]
            ]
        )

HELP_TEXT = f"""
**ποΈThis is @NiupunDinujaya_bot Help Menu ποΈ**

β οΈοΈRead this before useing me ...

β/logo logo name 
β/logohq logo name 
β/rmbg reply to photo 
β/edit reply to photo 
β/carbon reply to text
β/text reply to text
β/rlogo logo name

Β©2022 βοΈ
"""

BACKTOHOME = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("πBack", callback_data="startmenu")
                ]
            ]
        )

ABOUT_TEXT = """
π**Logo Design Platform in Telegram , 
World First Time With Image Editor tools**π

π₯You Can Create Many Type Of **Logo Design**
For your Dp & More Usage , Remove Background  
With full **Advance image Editor Features** Included 
This Bot Based on @MalithRukshan **Logo Api Key**
& **TroJanzHex Image editor** 
Speacial credits gone **Dα΄α΄α΄Ι΄α΄Κα΄ Jα΄sΙͺΙ΄Ι’Κα΄ & <sz/> Team ** ...π€

πββ**Logo Types & Image editor Features** : 

πApi Based logo Creator
πRando logo Creator 
β£οΈ Carbon maker
πBackground Remover
βText art Genarator 80+ styles
β­οΈImage editor 
           π‘Bright 
           πΌ Mixed 
           π Black & White 
           βͺοΈ Circle 
           π©Έ Blur
           π² Border 
           π― Sticker 
           π Rotate
           π Contrast 
           π Sepia 
           βοΈ Pencil 
           βοΈ Cartoon 
           β¨ Invert 
           π² Glitch
           π Remove Background
ββββββββββββββββββββ
β οΈ **Please Note** β οΈ

β**We have added force sub to image bot  
because of some users spaming our bot 
by sending command  π So now bot works
only for people who are subscribed our channel π 
So If you send /start ,bot will reply you
a message to Subscribe Our Updates Channel , 
So If you recieved that message simply
go the given inline button andJoin our Channel Then /start again π
Then You Can Use Our Bot For limited  To Create logo π«π**

π `Thank you all for following thisΒ΄β₯οΈ
ββββββββββββββββββββ
πTry it Now , Enjoy Unlimited logo creator !!!  π
"""

CLOSE_BTN =  InlineKeyboardMarkup(
        [
        [
        InlineKeyboardButton(text="Owner", url=f"https://t.me/NiupunDinujaya")    
        ]
        ]      
    )

FSUB_TEXT = " **You cant use me untill subscribe our updates channel** βΉοΈ\n\n So Please join our updates channel by the following button and hit on the ` /start ` again π"

FSUB_BTN = InlineKeyboardMarkup(
        [
        [
        InlineKeyboardButton(text="π£ Join our update Channel ", url=f"https://t.me/ankivectorupdates") 
        ]
        ]      
    )

@sz.on_callback_query(filters.regex("startmenu"))
async def startmenu(_, query: CallbackQuery):
    await query.edit_message_text(START_TEXT,
        reply_markup=START_BTN,
     disable_web_page_preview=True
    )

@sz.on_callback_query(filters.regex("helpmenu"))
async def helpmenu(_, query: CallbackQuery):
    await query.edit_message_text(HELP_TEXT,
        reply_markup=BACKTOHOME,
     disable_web_page_preview=True
    )

@sz.on_callback_query(filters.regex("aboutmenu"))
async def aboutenu(_, query: CallbackQuery):
    await query.edit_message_text(ABOUT_TEXT,
        reply_markup=BACKTOHOME,
     disable_web_page_preview=True
    )

@sz.on_callback_query(filters.regex("closeit"))
async def close(_, query: CallbackQuery):
    await query.message.delete()        

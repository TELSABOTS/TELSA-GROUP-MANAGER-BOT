import time
from telegram import Bot, Update, ParseMode
from telegram.ext import run_async
from TELSA import dispatcher
from TELSA.modules.disable import DisableAbleCommandHandler
from TELSA.modules.helper_funcs.chat_status import user_admin

#sleep how many times after each edit in 'police' 
EDIT_SLEEP = 2
#edit how many times in 'police' 
EDIT_TIMES = 6

police_siren = [
            "π΄π΄π΄β¬οΈβ¬οΈβ¬οΈπ΅π΅π΅\nπ΄π΄π΄β¬οΈβ¬οΈβ¬οΈπ΅π΅π΅\nπ΄π΄π΄β¬οΈβ¬οΈβ¬οΈπ΅π΅π΅",
            "π΅π΅π΅β¬οΈβ¬οΈβ¬οΈπ΄π΄π΄\nπ΅π΅π΅β¬οΈβ¬οΈβ¬οΈπ΄π΄π΄\nπ΅π΅π΅β¬οΈβ¬οΈβ¬οΈπ΄π΄π΄"
]

fbi_ig = [
  "\O_O",
  "O_O/"
]

bye_bomb = [
            "βͺοΈβͺοΈβͺοΈβͺοΈ",
            "π£π£π£π£ ",
            "π₯π₯π₯π₯",
            "π΅π΅π΅π΅"
]

love_u = [
            "ππππππβ€οΈβ€οΈβ€οΈ",
            "ππππ§‘π§‘π§‘π€π€π€"
]

moon_animation = [
            "π",
            "π ",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π"
]

earth_an = [
            "π",
            "π",
            "π"
]

@user_admin
@run_async
def police(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('πPOLICE IS HEREπ')
    for x in range(EDIT_TIMES):
        msg.edit_text(police_siren[x%2]) 
        time.sleep(EDIT_SLEEP)
    msg.edit_text('πPOLICE IS HEREπ')

@user_admin
@run_async
def moon(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('πMOON ANIMATIONπ')
    for x in range(EDIT_TIMES):
        msg.edit_text(moon_animation[x%8]) 
        time.sleep(EDIT_SLEEP)
    msg.edit_text('πMOON ANIMATIONπ')

@user_admin
@run_async
def earth(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('πEARTH ANIMATIONπ')
    for x in range(EDIT_TIMES):
        msg.edit_text(earth_an[x%8]) 
        time.sleep(EDIT_SLEEP)
    msg.edit_text('πEARTH ANIMATIONπ')

@user_admin
@run_async
def fbi(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('FBI IS HERE!')
    for x in range(EDIT_TIMES):
        msg.edit_text(fbi_ig[x%2]) 
        time.sleep(EDIT_SLEEP)
    msg.edit_text('FBI IS HERE')

@user_admin
@run_async
def love(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('β€οΈ')
    for x in range(EDIT_TIMES):
        msg.edit_text(love_u[x%2]) 
        time.sleep(EDIT_SLEEP)
    msg.edit_text('I π U')

@user_admin
@run_async
def bomb(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('πBOMBSπ')
    for x in range(EDIT_TIMES):
        msg.edit_text(bye_bomb[x%9]) 
        time.sleep(EDIT_SLEEP)
    msg.edit_text('β°οΈRIPβ°οΈ')
    
__help__ = f"""
*ANIMATIONS *

 /love : SHE LOVES YOU.
 /bomb : YOU REJECTED HER, SO SHE IS GOING TO SUSCIDE .
 /police : POLICE WILL CATCH YOU. 
 /moon : MOON REVOVLES
 /earth : EARTH REVOLVES
"""
    
POLICE_HANDLER = DisableAbleCommandHandler("police", police)
FBI_HANDLER = DisableAbleCommandHandler("fbi", fbi)
LOVE_HANDLER = DisableAbleCommandHandler("love", love)
BOMB_HANDLER = DisableAbleCommandHandler("bomb", bomb)
MOON_HANDLER = DisableAbleCommandHandler("moon", moon)
EARTH_HANDLER = DisableAbleCommandHandler("earth", earth)
dispatcher.add_handler(POLICE_HANDLER)    
dispatcher.add_handler(FBI_HANDLER)
dispatcher.add_handler(LOVE_HANDLER)
dispatcher.add_handler(BOMB_HANDLER)
dispatcher.add_handler(MOON_HANDLER)
dispatcher.add_handler(EARTH_HANDLER)

__mod_name__ = "π€£LOLπ€£"
__command_list__ = ["police", "fbi"]	
__handlers__ = [POLICE_HANDLER, FBI_HANDLER, LOVE_HANDLER, BOMB_HANDLER, MOON_HANDLER, EARTH_HANDLER  ]

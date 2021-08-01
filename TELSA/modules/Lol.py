import time
from telegram import Bot, Update, ParseMode
from telegram.ext import run_async
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.chat_status import user_admin

#sleep how many times after each edit in 'police' 
EDIT_SLEEP = 2
#edit how many times in 'police' 
EDIT_TIMES = 6

police_siren = [
            "🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵",
            "🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴"
]

fbi_ig = [
  "\O_O",
  "O_O/"
]

bye_bomb = [
            "▪️▪️▪️▪️",
            "💣💣💣💣 ",
            "💥💥💥💥",
            "😵😵😵😵"
]

love_u = [
            "💛💛💛💙💙💙❤️❤️❤️",
            "💚💚💚🧡🧡🧡🖤🖤🖤"
]

moon_animation = [
            "🌗",
            "🌔 ",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖"
]

earth_an = [
            "🌍",
            "🌏",
            "🌎"
]

@user_admin
@run_async
def police(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('😓POLICE IS HERE😓')
    for x in range(EDIT_TIMES):
        msg.edit_text(police_siren[x%2]) 
        time.sleep(EDIT_SLEEP)
    msg.edit_text('😓POLICE IS HERE😓')

@user_admin
@run_async
def moon(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('🌖MOON ANIMATION🌖')
    for x in range(EDIT_TIMES):
        msg.edit_text(moon_animation[x%8]) 
        time.sleep(EDIT_SLEEP)
    msg.edit_text('🌖MOON ANIMATION🌖')

@user_admin
@run_async
def earth(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('🌏EARTH ANIMATION🌏')
    for x in range(EDIT_TIMES):
        msg.edit_text(earth_an[x%8]) 
        time.sleep(EDIT_SLEEP)
    msg.edit_text('🌏EARTH ANIMATION🌏')

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
    msg = update.effective_message.reply_text('❤️')
    for x in range(EDIT_TIMES):
        msg.edit_text(love_u[x%2]) 
        time.sleep(EDIT_SLEEP)
    msg.edit_text('I 💘 U')

@user_admin
@run_async
def bomb(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('😓BOMBS😓')
    for x in range(EDIT_TIMES):
        msg.edit_text(bye_bomb[x%9]) 
        time.sleep(EDIT_SLEEP)
    msg.edit_text('⚰️RIP⚰️')
    
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

__mod_name__ = "🤣LOL🤣"
__command_list__ = ["police", "fbi"]	
__handlers__ = [POLICE_HANDLER, FBI_HANDLER, LOVE_HANDLER, BOMB_HANDLER, MOON_HANDLER, EARTH_HANDLER  ]

  
#꧁༒☬𝓣𝓔𝓛𝓢𝓐 𝓑𝓞𝓣𝓢☬༒꧂

from typing import Optional

from telegram import Message, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import BadRequest
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown

import TELSA.modules.sql.rules_sql as sql
from TELSA import dispatcher
from TELSA.modules.helper_funcs.chat_status import user_admin
from TELSA.modules.helper_funcs.string_handling import markdown_parser


@run_async
def get_rules(bot: Bot, update: Update):
    chat_id = update.effective_chat.id
    send_rules(update, chat_id)


# Do not async - not from a handler
def send_rules(update, chat_id, from_pm=False):
    bot = dispatcher.bot
    user = update.effective_user  
    try:
        chat = bot.get_chat(chat_id)
    except BadRequest as excp:
        if excp.message == "Chat not found" and from_pm:
            bot.send_message(user.id, "The rules shortcut for this chat hasn't been set properly! Ask admins to "
                                      "fix this.")
            return
        else:
            raise

    rules = sql.get_rules(chat_id)
    text = "THE RULES FOR *{}* are:\n\n{}".format(escape_markdown(chat.title), rules)

    if from_pm and rules:
        bot.send_message(user.id, text, parse_mode=ParseMode.MARKDOWN)
    elif from_pm:
        bot.send_message(user.id, "NO RULES FOUND"
                                  "IN THIS CHAT...!")
    elif rules:
        update.effective_message.reply_text("Contact me in PM to get this group's rules.",
                                            reply_markup=InlineKeyboardMarkup(
                                                [[InlineKeyboardButton(text="Rules",
                                                                       url="t.me/{}?start={}".format(bot.username,
                                                                                                     chat_id))]]))
    else:
        update.effective_message.reply_text("NO RULES FOUND"
                                            "IN THIS CHAT...!")


@run_async
@user_admin
def add_rules(bot: Bot, update: Update):
    chat_id = update.effective_chat.id
    msg = update.effective_message 
    raw_text = msg.text
    args = raw_text.split(None, 1)  
    if len(args) == 2:
        txt = args[1]
        offset = len(txt) - len(raw_text)  \
        markdown_rules = markdown_parser(txt, entities=msg.parse_entities(), offset=offset)

        sql.add_rules(chat_id, markdown_rules)
        update.effective_message.reply_text("✅DONE RULE ADDED✅")


@run_async
@user_admin
def del_rules(bot: Bot, update: Update):
    chat_id = update.effective_chat.id
    sql.add_rules(chat_id, "")
    update.effective_message.reply_text("🗑DONE DELETED RULES🗑")


def __stats__():
    return "{} chats have rules set.".format(sql.num_chats())


def __import_data__(chat_id, data):
    # set chat rules
    rules = data.get('info', {}).get('rules', "")
    sql.add_rules(chat_id, rules)


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)


def __chat_settings__(chat_id, user_id):
    return "This chat has had it's rules set: `{}`".format(bool(sql.get_rules(chat_id)))


__help__ = """
*ADMIN ONLY:*
/addrules <keyword>:SET RULES FOR THIS CHAT
/delrules: TO DELETE RULES FOR THIS CHAT
[ㅤ](https://telegra.ph/file/67f862e4a591e2ebb159e.mp4)
"""

__mod_name__ = "🧑🏻‍⚖️RULES👩🏻‍⚖️"

GET_RULES_HANDLER = CommandHandler("rules", get_rules, filters=Filters.group)
SET_RULES_HANDLER = CommandHandler("addrules", add_rules, filters=Filters.group)
RESET_RULES_HANDLER = CommandHandler("delrules", del_rules, filters=Filters.group)

dispatcher.add_handler(GET_RULES_HANDLER)
dispatcher.add_handler(SET_RULES_HANDLER)
dispatcher.add_handler(RESET_RULES_HANDLER)

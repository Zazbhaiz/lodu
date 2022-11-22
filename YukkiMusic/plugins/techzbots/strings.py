from YukkiMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MUSIC_BOT_NAME as BOT_NAME

BOT_USERNAME = app.username
START_TEXT = f"""
✨ **Hello {} !**
✪ I'm an music + management bot [✨](https://telegra.ph/file/7ed4a724821b3bd2cc320.jpg)
────────────────────────
× *Uptime:* `{}`
× `{}` *users, across* `{}` *chats.*
────────────────────────
✪ Hit /help to see my available commands.
"""

COMMANDS_TEXT = f"""
✨ **Hello MENTION !**
**Click on the buttons below to know my commands.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="📚 Cᴏᴍᴍᴀɴᴅs", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="⚒ Sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="💌 Cʜᴀɴɴᴇʟ", url="https://t.me/Luv_Holic"
            ),
            InlineKeyboardButton(
                text="🔎 Gʀᴏᴜᴩ", url="https://t.me/xSupport_ies"
            ),                       
        ],
        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="➕ Aᴅᴅ ᴍᴇ Bᴀʙʏ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="📚 Cᴏᴍᴍᴀɴᴅs", callback_data="command_menu"
            ),
                                        
        ],
        [
            InlineKeyboardButton(
                text="💌 Cʜᴀɴɴᴇʟ", url="https://t.me/Zazbhai"
            ),
            InlineKeyboardButton(
                text="🔎 Gʀᴏᴜᴩ", url="https://t.me/Zazbhai"
            ),                       
        ],
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🧃 Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅs", callback_data="admin_cmd"
            ),
             InlineKeyboardButton(
                text="🍹 Bᴏᴛ Cᴏᴍᴍɴᴀᴅs", callback_data="bot_cmd"
            ), 
          
         ],
         [
            InlineKeyboardButton(
                text="🍷 Pʟᴀʏ Cᴏᴍᴍᴀɴᴅs", callback_data="play_cmd"
            ),            
            InlineKeyboardButton(
                text="🥂 Exᴛʀᴀ Cᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/Aviax-Music-Help-Commands-05-16"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🧃 Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅs", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="🍹 Bᴏᴛ Cᴏᴍᴍɴᴀᴅs", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="🍷 Pʟᴀʏ Cᴏᴍᴍᴀɴᴅs", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="🍻 Sᴜᴅᴏ Cᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/Aviax-Sudo-cmds-05-16"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="🥂 Exᴛʀᴀ Cᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/Aviax-Music-Help-Commands-05-16"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🍻 Sᴜᴅᴏ Cᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/Aviax-Sudo-cmds-05-16"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
✅--**Admin Commands:**--
c stands for channel play.
/pause or /cpause - Pause the playing music.
/resume or /cresume- Resume the paused music.
/mute or /cmute- Mute the playing music.
/unmute or /cunmute- Unmute the muted music.
/skip or /cskip- Skip the current playing music.
/stop or /cstop- Stop the playing music.
/shuffle or /cshuffle- Randomly shuffles the queued playlist.
✅--**Specific Skip:**--
/skip or /cskip [Number(example: 3)] 
    - Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.
✅--**Loop Play:**--
/loop or /cloop [enable/disable] or [Numbers between 1-10] 
    - When activated, bot loops the current playing music to 1-10 times on voice chat. Default to 10 times.
"""
AUTH_TEXT = """
✅--**Auth Users:**--
Auth Users can use admin commands without admin rights in your chat.
/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group.
"""

AUTH_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)

BOT_TEXT = """
✅--**Bot Commands:**--
/stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.
/sudolist - Check Sudo Users of Yukki Music Bot
/lyrics [Music Name] - Searches Lyrics for the particular Music on web.
/song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.
c stands for channel play.
/queue or /cqueue- Check Queue List of Music.
"""

PLAY_TEXT = """
✅--**Play Commands:**--
Available Commands = play , vplay , cplay
ForcePlay Commands = playforce , vplayforce , cplayforce
c stands for channel play.
v stands for video play.
force stands for force play.
/play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.
/playforce or /vplayforce or /cplayforce -  Force Play stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.
/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.
✅--**Bot's Server Playlists:**--
/playlist  - Check Your Saved Playlist On Servers.
/deleteplaylist - Delete any saved music in your playlist
/play  - Start playing Your Saved Playlist from Servers.
"""

MISC = """/set_chat_title - Change The Name Of A Group/Channel.
/set_chat_photo - Change The PFP Of A Group/Channel.
/set_user_title - Change The Administrator Title Of An Admin."""

BASIC_TEXT = """
➲ /start : sᴛᴀʀᴛ ᴍᴇ ʙᴀʙʏ , ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ :-)​.
➲ /help  : ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ꜱᴇᴄᴛɪᴏɴ.
  ‣ ɪɴ ᴘᴍ : ᴡɪʟʟ sᴇɴᴅ ʏᴏᴜ ʜᴇʟᴘ​ ꜰᴏʀ ᴀʟʟ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴏᴅᴜʟᴇꜱ.
  ‣ ɪɴ ɢʀᴏᴜᴘ : ᴡɪʟʟ ʀᴇᴅɪʀᴇᴄᴛ ʏᴏᴜ ᴛᴏ ᴘᴍ, ᴡɪᴛʜ ᴀʟʟ ᴛʜᴀᴛ ʜᴇʟᴘ​ ᴍᴏᴅᴜʟᴇꜱ.
"""

ANIMAL = """
/catfacts - To Get Facts About Cat.
/dogfacts - To Get Facts About Dog.
/animalfacts - To Get Facts About Animal.
"""

ANIME =  """

/anime - Get Anime Info.
/manga - Get Manga Info.
/aquote - Get Random Anime Quote.
/aquote anime- Get Anime Quote From An Anime.
/cquote character - Get Quote From A Character.

"""
ANTI = """"Plugin to delete service messages in a chat!
/antiservice [enable|disable]"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🌦 Aᴅᴍɪɴ", callback_data="admin"
            ),
            InlineKeyboardButton(
                text="🌸 Aᴅᴍɪɴ Mɪsᴄ", callback_data="misc"
            ),

            InlineKeyboardButton(
                text="🦄 Aɴɪᴍᴀʟ", callback_data="animal"
            ),
        ],
           [ InlineKeyboardButton(
                text="🦋 Aɴɪᴍᴇ", callback_data="anime"
            ),           

            InlineKeyboardButton(
                text="🐬 Aɴɪᴍᴇ Pɪᴄs", callback_data="picks"
            ),   
             InlineKeyboardButton(
                text="🧃 Aɴᴛɪ-Sᴇʀᴠɪᴄᴇ", callback_data="anti"
            ),           


                   
        ],   


        [ InlineKeyboardButton(
                text="❗️Bʟᴀᴄᴋʟɪsᴛ", callback_data="black"
            ),           

            InlineKeyboardButton(
                text="💣 Bʟᴀᴄᴋʟɪsᴛ cʜᴀᴛs", callback_data="blackc"
            ),   
             InlineKeyboardButton(
                text="🐾 Cᴀᴛs", callback_data="cats"
            ),           


                   
        ],   
        [ InlineKeyboardButton(
                text="👩‍💻 Cʜᴀᴛʙᴏᴛ", callback_data="chat"
            ),           

            InlineKeyboardButton(
                text="🧸 Sʜɪᴘᴘᴇʀɪɴɢ", callback_data="couple"
            ),   
             InlineKeyboardButton(
                text="🏏 Cʀɪᴄᴋɪɴғᴏ", callback_data="crick"
            ),           


                   
        ],   

      
        [
           
            InlineKeyboardButton(
                text="◎ Bᴀᴄᴋ", callback_data="command_menu"
            ),  
            InlineKeyboardButton(
                text="➡", callback_data="next1"
            ),                
        ],                          
    ]
)

NEXT1 = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🥇 Cʀʏᴘᴛᴏ", callback_data="crypto"
            ),
            InlineKeyboardButton(
                text="🎲 Dɪᴄᴇ", callback_data="dice"
            ),

            InlineKeyboardButton(
                text="🎭 Fɪʟᴛᴇʀs", callback_data="filter"
            ),
        ],
           [ InlineKeyboardButton(
                text="❄️ Fʟᴏᴏᴅ", callback_data="flood"
            ),           

            InlineKeyboardButton(
                text="🎉 Fᴜɴ", callback_data="fun"
            ),   
             InlineKeyboardButton(
                text="🎊 Gʀᴇᴇᴛɪɴɢs", callback_data="greet"
            ),           


                   
        ],   


        [ InlineKeyboardButton(
                text="🔍 Iɴғᴏ", callback_data="info"
            ),           

            InlineKeyboardButton(
                text="✨ Kᴀʀᴍᴀ", callback_data="karma"
            ),   
             InlineKeyboardButton(
                text="🔐 Lᴏᴄᴋs", callback_data="lock"
            ),           


                   
        ],   
        [ InlineKeyboardButton(
                text="🎈 Mɪsᴄ", callback_data="misc1"
            ),           

            InlineKeyboardButton(
                text="🎙 Mᴜsɪᴄ", callback_data="music"
            ),   
             InlineKeyboardButton(
                text="📝 Nᴏᴛᴇs", callback_data="notes"
            ),           


                   
        ],   

      
        [
            InlineKeyboardButton(
                text="⬅", callback_data="basic_cmd"
            ),      
            InlineKeyboardButton(
                text="◎ Bᴀᴄᴋ", callback_data="command_menu"
            ),  
                          
        ],                          
    ]
)



ZAZ = InlineKeyboardMarkup(
    [   

      
        [
            InlineKeyboardButton(
                text="◎ Bᴀᴄᴋ", callback_data="basic_cmd"
            ),
               
        ],                          
    ]
)

ZAZ1 = InlineKeyboardMarkup(
    [   

      
        [
            InlineKeyboardButton(
                text="◎ Bᴀᴄᴋ", callback_data="next1"
            ),
               
        ],                          
    ]
)


ADMIN_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🪄 Aᴜᴛʜ Cᴏᴍᴍᴀɴᴅs", callback_data="auth_cmds"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="✨ Mᴀɴᴀɢᴇᴍᴇɴᴛ", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="🎧 Mᴜsɪᴄ", callback_data="advanced_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)

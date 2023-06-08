import json
import os


def get_user_list(config, key):
    with open('{}/YUI/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER=True
    URL=False
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY=""
    DEL_CMDS=False
    BAN_STICKER=""
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB="mongodb+srv://yuiga:erena12@cluster0.awwhgt0.mongodb.net/?retryWrites=true&w=majority"
    WEBHOOK=False
    BOT_API_URL="5885016cd84MooEZgaeFxy5-qFkuMQagk"
    #kacrmdi
    WOLVES=[]
    BOT_ID=6284652932
    SQLALCHEMY_DATABASE_URI="postgres://jympgnps:2_sz2vN3Zz8z5thAssDB9BRhQt8BZRKT@jelani.db.elephantsql.com/jympgnps" 
    JOIN_LOGGER=-1001692375111
    API_HASH="439d58a783f6e7008ba5baa5207" 
    INFOPIC=True
    TIGERS=[]
    STRING_SESSION ="T9ji3c5_QP4_A5pBA9JnfX5-8x1ipHJwiEVkNedPczVb35jMltPTTEJ2yzF9-OTL_ZJsBlspnic-fg62wAl3yNu83VQwR1wh7SDTAR2BnxEcMb-xy8vRITVwfzivX4gII49NWY263b22I8nVntgtjQ-y3YVImjfzk3EQbB_xGYgINyzrTvp2Crd0qCw4ITzyfFvGnc3z28N8nfgCXoV_jqAf2oezRwuKFoTVKz3O94xAiL8UV5KP0dsCP389jIHkVzh-47H5kCnASAjVL07qheS1fazK1vl7PxAU4Su3ewd7K3BQ1m9LNoqMqc5uY79UA15i_bthp3PNmVvk="
    API_ID=28624076
    BL_CHATS=[1]
    DB_URL2="postgres://dpmyesld:reMVuSpnDIcTaIm1B_zGevEe1MIwK5ha@salt.db.elephantsql.com/dpmyesld" 
    TOKEN="5885016551:AAGr6TVgVcd84MooEZgaeFxy5-qFkuMQagk"
    DEV_USERS=[1005344893]
    DRAGONS=[]
    SPAMWATCH_API=""
    WALL_API=""
    DEMONS=[]
    SUPPORT_CHAT="Yuigasupport"
    OWNER_USERNAME="dragoneyegaming"
    DONATION_LINK="https://t.me/dragoneyegaming"
    EVENT_LOGS=-1001692375111 
    OWNER_ID=1936119750 
    TIME_API_KEY=""
    ERROR_LOGS=-1001692375111
    BOT_NAME="YuigaRobot"
    STRICT_GBAN=True
    REDIS_URL="redis://default:e06wyhyZUB0UFKbViNOzbsY5u7X2DoaY@redis-17063.c8.us-east-1-2.ec2.cloud.redislabs.com:17063"
    UPDATE_CHANNEL="x"
    MONGO_DB_URI="mongodb+srv://KanaoVC:KanaoVC@cluster0.shebn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    BOT_USERNAME="YuigaRobot"
    REM_BG_API_KEY=""
    CASH_API_KEY=""
    AI_API_KEY=""
    SPAMWATCH_SUPPORT_CHAT="SpamWatchSupport"
    OPENWEATHERMAP_ID=""
    LOG_GROUP_ID=-1001735328148
    STRICT_GMUTE=True
    SPAMWATCH_API=""
    OWNER_NAME="ZoRo"
    BANCODES=""
    REPOSITORY="GitHub.com/princesssgirlxd/yuigahama"
    ARQ_API_KEY=""
    ARQ_API_URL=""
    COTB=""

class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True

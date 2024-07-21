import os

API_ID = API_ID =  21179966

API_HASH = os.environ.get("API_HASH", "d97919fb0a3c725e8bb2a25bbb37d57c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7130247687:AAH62Amtb4TC2V63iwyNdccxzqL5Jo8gFwY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7326397503))

LOG = -1002076315589,

# UPDATE_GRP = -1002140332321, # bot sat group

# auth_chats = [5219193259,1327415906]

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7326397503").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



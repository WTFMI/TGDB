import time
from telethon import TelegramClient

from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest, ForwardMessagesRequest
from telethon.tl.types import InputChannel

from telethon.tl.types import InputPeerEmpty
import asyncio
from telethon.tl.types import DocumentAttributeVideo
import sys
from telethon.tl.types import FileLocation, ChatPhoto, PeerUser, PeerChat, PeerChannel, Channel

from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
import datetime
import re
import pickle
api_id =  # Use your own values here. https://my.telegram.org
api_hash = ''
phone_number = '+972'

client = TelegramClient('aguda-session', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.start() # logining and connecting to Telegram servers

loop = asyncio.get_event_loop()
auth = loop.run_until_complete(client.is_user_authorized())
if not auth:  # authorization (if there is no .session file created before)
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))


#id = loop.run_until_complete(client.get_entity('https://t.me/AgudaDev'))
#r = loop.run_until_complete(client(GetFullChatRequest(id)))
#from telethon import InteractiveTelegramClient
#from telethon.utils.tl_utils import get_display_name

#client = InteractiveTelegramClient('session_id', 'YOUR_PHONE_NUMBER', api_id=1234YOURAPI_ID, api_hash='YOUR_API_HASH')
def get_channels():
    dialog_count = 900
    q = loop.run_until_complete(client.get_dialogs(dialog_count))
    try:
        for i in q:
            if (i):
                print ("Checking " + i.name)
                if (re.match('.*REPLACE_WITH_PARTIAL_CHANNEL_OR_GROUP_NAME.*', i.name)):
                    print("GOT IT " + i.name , '\n---\n')
                    return i

    except:
        #print("")
        pass
    #sys.exit()
    #for i, entity in enumerate(entities):
    #                i += 1  # 1-based index
    #                print('{}. {}. id: {}'.format(i, entity.username, entity.id))

def get_users(loop):
    offset = 0
    limit = 100
    all_participants = []
    #channel = Channel(1330505769, title='\u2066♥️\u2069Empathogens❄️קהילת🍄אמפתוגנים', photo=ChatPhoto(photo_small=FileLocation(dc_id=4, volume_id=449011102, local_id=3795, secret=5154166241589927286), photo_big=FileLocation(dc_id=4, volume_id=449011102, local_id=3797, secret=-3469345200309841222)))
    channel = get_entity(id=1330505769, title='\u2066♥️\u2069Empathogens❄️קהילת🍄אמפתוגנים', photo=ChatPhoto(photo_small=FileLocation(dc_id=4, volume_id=449011102, local_id=3795, secret=5154166241589927286), photo_big=FileLocation(dc_id=4, volume_id=449011102, local_id=3797, secret=-3469345200309841222)), date=datetime.datetime(2018, 9, 25, 13, 42, 14, tzinfo=datetime.timezone.utc), version=0)
    while True:
        participants = loop.run_until_complete(client(GetParticipantsRequest(
            channel, ChannelParticipantsSearch(''), offset, limit, hash=0
            )))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset += len(participants.users)
        print('Magic Number: ', offset)
        return all_participants
#channel = Channel(id=1330505769, title='\u2066♥️\u2069Empathogens❄️קהילת🍄אמפתוגנים', photo=ChatPhoto(photo_small=FileLocation(dc_id=4, volume_id=449011102, local_id=3795, secret=5154166241589927286), photo_big=FileLocation(dc_id=4, volume_id=449011102, local_id=3797, secret=-3469345200309841222)), date=datetime.datetime(2018, 9, 25, 13, 42, 14, tzinfo=datetime.timezone.utc), version=0)
qq = get_channels()
print('*******\n')
print(qq)
#sys.exit()
r = loop.run_until_complete(client.get_participants(qq, None, aggressive=True))
db = open('users.db', 'wb+')
for x in r:
    print(x)
    #pickle.dump(x, db)
    #db.write(x)
    #db.write()
pickle.dump(r, db)
sys.exit()
##
fh = open('choiceVideo.mp4', 'rb')
msg = loop.run_until_complete(client.send_file('me', fh, attributes=(DocumentAttributeVideo(0, 0, 0),)))

location = 0
max = 2
for x in range(location, r.length():
    print(x.username + '\n')
    location = location + 1
    if location >= max:
        break

    if x.username != 'WTFMI':

        m1 = loop.run_until_complete(client.send_message(x, 'הודעה זו נשלחה באופן אוטומטי, בוקר טוב מהחלל הקיברנט'))
        loop.run_until_complete(client.forward_messages(x, msg))
        #loop.run_until_complete(client(ForwardMessagesRequest(
        #    from_peer='me',  # who sent these messages?
        #    id=msg.id,  # which are the messages?
        #    to_peer=x  # who are we forwarding them to?
        #    )))
    #print(m1)
    #print(m2)
# this was as a test to see how do I fetch stuff
#result = client(ResolveUsernameRequest('@AlonOz'))
#found_chats = result.chats
#found_users = result.users
# end test
#users = client(GetFullChannel(self, 'id'))
#for id in found_chats:

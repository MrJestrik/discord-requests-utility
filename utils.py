import requests, json, time
class Synkronex:
    def __init__(self, token: str = None, username: str = None, password: str = None):
        self.base_url = "https://discord.com/api/v9"
        self.token = token
        self.uname = username
        self.pw = password
        self.headers1 = {'Authorization': token}
        self.headers2 = {'Authorization': token, 'Content-Type': 'application/json'}
        response = requests.get(f'{self.base_url}/users/@me', headers=self.headers2)
        self.status = "Success"
        user_info = response.json()
        self.id = user_info['id']
        self.username = user_info['username']
        self.discriminator = user_info['discriminator']
        self.global_name = user_info['global_name']
        self.mfa = user_info['mfa_enabled']
        self.locale = user_info['locale']
        self.premium_type = user_info['premium_type']
        self.email = user_info['email']
        self.verified = user_info['verified']
        self.phone = user_info['phone']
        self.nsfw = user_info['nsfw_allowed']
        self.headers = {'authorization': self.token, "content-type": "application/json"}
    #message utilities
    def send_message(self, message, channelid):
        req = requests.post(f"{self.base_url}/channels/{channelid}/messages", data={'content': message}, headers=self.headers1)
        print(req.status_code)
        return req.json()
    def edit_message(self, message, channelid, messageid):
        req = requests.patch(f"{self.base_url}/channels/{channelid}/messages/{messageid}", data={'content': message}, headers=self.headers1)
        print(req.status_code)
    def delete_message(self, channelid, messageid):
        req = requests.delete(f"{self.base_url}/channels/{channelid}/messages/{messageid}", headers=self.headers1)
        print(req.status_code)
    def get_messages(self, channelid, amount):
        req = requests.get(f'{self.base_url}/channels/{channelid}/messages?limit={amount}', headers=self.headers1)
        print(req.status_code)
        return req.json()
    def typing(self, channelid):
        req = requests.post(f'https://discord.com/api/v8/channels/{channelid}/typing', headers=self.headers1)
        print(req.status_code)
    def react_to_message(self, channelid, messageid, reaction):
        req = requests.put(f"{self.base_url}/channels/{channelid}/messages/{messageid}/reactions/{reaction}/%40me?location=Message&type=0", headers=self.headers1)
        print(req.status_code)
    def send_command(self, data):
        req = requests.post(f"{self.base_url}/interactions", json=data, headers=self.headers1)
        print(req.status_code)
    def dank_memer_grinder(self, serverid, channelid, beg: bool = True, dig: bool = True, fish: bool = True, hunt: bool = True):
        f = open('../v1/dank_memer.json', 'r')
        data = json.load(f)
        # beg
        if beg:
            data['beg']['guild_id'] = serverid
            data['beg']['channel_id'] = channelid
            self.send_command(data['beg'])
            time.sleep(0.8)
        # dig
        if dig:
            data['dig']['guild_id'] = serverid
            data['dig']['channel_id'] = channelid
            self.send_command(data['dig'])
            time.sleep(0.8)
        # fish
        if fish:
            data['fish']['guild_id'] = serverid
            data['fish']['channel_id'] = channelid
            self.send_command(data['fish'])
            time.sleep(0.8)
        # hunt
        if hunt:
            data['hunt']['guild_id'] = serverid
            data['hunt']['channel_id'] = channelid
            self.send_command(data['hunt'])
    def animate_message(self, message, channelid):
        msg = self.send_message(message, channelid)
        number_of_characters = 1
        while True:
            self.edit_message(message[0:number_of_characters], channelid, msg['id'])
            number_of_characters += 1
            if number_of_characters > len(message):
                number_of_characters = 0
            time.sleep(0.8)
    def ghost_message(self, message, channelid):
        msg = self.send_message(message, channelid)
        self.delete_message(channelid, msg['id'])
    def ghost_ping(self, channelid):
        msg = self.send_message(f"<@{self.id}>", channelid)
        self.delete_message(channelid, msg['id'])
    def ghost_massping(self, channelid):
        msg = self.send_message("@everyone", channelid)
        self.delete_message(channelid, msg['id'])
    def invis_msg(self, channelid): self.send_message("_ _", channelid)
    #user utilities
    def get_user_info(self, user_id): return requests.get(f'{self.base_url}/users/{user_id}', headers=self.headers1).json()
    def get_server_info(self, server_id): return requests.get(f'{self.base_url}/guilds/{server_id}', headers=self.headers1).json()
    def change_hypesquad_house(self, house_id, delete: bool = False):
        if delete:
            req = requests.delete(f"{self.base_url}/hypesquad/online", headers=self.headers1)
            print(req.status_code)
        else:
            req = requests.post(f"{self.base_url}/hypesquad/online", json={'house_id': house_id}, headers=self.headers1)
            print(req.status_code)
    def change_custom_status(self, status):
        req = requests.patch(f"{self.base_url}/users/@me/settings", data=json.dumps({'custom_status':{"text": status}}), headers=self.headers2)
        print(req.status_code)
    def animate_custom_status(self, status):
        ani_status = [i for i in status]
        print(ani_status)
        number_of_characters = 1
        while True:
            if ani_status == None:
                pass
            else:
                print(''.join(ani_status[0:number_of_characters]))
                self.change_custom_status(''.join(ani_status[0:number_of_characters]))
                number_of_characters += 1
                if number_of_characters > len(ani_status):
                    number_of_characters = 0
                time.sleep(0.8)
    def change_status(self, status):
        req = requests.patch(f"{self.base_url}/users/@me/settings", data=json.dumps({'status': status}), headers=self.headers2)
        print(req.status_code)
    def change_display_name(self, name):
        req = requests.patch(f'{self.base_url}/users/@me', data=json.dumps({'global_name': name}), headers=self.headers2)
        print(req.status_code)
    def animate_display_name(self, name):
        ani_name = [i for i in name]
        print(ani_name)
        number_of_characters = 1
        while True:
            print(''.join(ani_name[0:number_of_characters]))
            self.change_display_name(''.join(ani_name[0:number_of_characters]))
            number_of_characters += 1
            if number_of_characters > len(ani_name):
                number_of_characters = 0
            time.sleep(1)
    def change_user_note(self, userid, note):
        print(userid, note)
        req = requests.put(f"{self.base_url}/users/@me/notes/{userid}", json={"note": note}, headers=self.headers1)
        print(req.status_code)
    def animate_user_note(self, userid, note):
        ani_note = [i for i in note]
        print(ani_note)
        number_of_characters = 1
        while True:
            print(''.join(ani_note[0:number_of_characters]))
            self.change_user_note(userid, ''.join(ani_note[0:number_of_characters]))
            number_of_characters += 1
            if number_of_characters > len(ani_note):
                number_of_characters = 0
            time.sleep(0.8)
    def change_pronouns(self, pronoun):
        req = requests.patch(f'{self.base_url}/users/%40me/profile', data=json.dumps({"pronouns": pronoun}), headers=self.headers2)
        print(req.status_code)
# -*- coding: utf-8 -*-

import KRIS
from KRIS.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
#from gtts import gTTS
from googletrans import Translator

cl = KRIS.LINE()
#cl.login(qr=True)
cl.login(token='isi anu')#ranita
cl.loginResult()#

kc = kl = cl
satpam = kk = ki = cl

print "╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ KRIS BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════"
reload(sys)
sys.setdefaultencoding('utf-8')

#album = None
#image_path = 'tmp/tmp.jpg'

helpMessage ="""
╔═════════════
║    ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║      Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠☔Key1
║╠☔Key2
║╠☔Key3
║╠☔Say (txt)
║╠☔Kr say (text)
║╠☔Apakah (text)
║╠☔Kapan (txt)
║╠☔welcome
║╠☔.. (text)
║╠☔Time
║╠☔rate @
║╠☔Gcreator
║╠☔Creator
║╠☔Spam on (jml) (Text)
║╠☔image
║╠☔ig
║╠☔youtube
║╠☔lirik
║╠☔music
║╠☔zodiAK
║╠☔Mimic
║╠☔Getcover @
║╠☔Tag on/off
║╠☔Getpp @
║╠☔Getinfo @
║╠☔Getinfo2
║╠☔Njoin on/off
║╠☔Nleave on/off
║╠☔setview
║╠☔viewseen
║╠☔CCtv
║╠☔Intip
║╠☔Crot (tagall)
║╠☔Absen
║╠☔Gift
║╠☔ranita pergi (ngeluarkan bot)
║╠☔Kr pergi (ngeluarkan bot)
║╚════════════
║   UNTUK PUBLIK
║ SILAHKAN GUNAKAN
╚═════════════
"""

protectMessage ="""
╔═════════════
║    ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║      Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂͜͡⚡➣qr on/oғғ
║╠❂͜͡⚡➣gυeѕт on/oғғ
║╠❂͜͡⚡➣мeмвer on/oғғ
║╠❂͜͡⚡➣groυp on/oғғ
║╠❂͜͡⚡➣ĸιcĸ on/oғғ
║╠❂͜͡⚡➣cancel on/oғғ
║╚════════════
╚═════════════
"""

socmedMessage ="""
╔═════════════
║    ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║      Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂͜͡🌟➣wιĸι [тeхт]
║╠❂͜͡🌟➣ιg [тeхт]
║╠❂͜͡🌟➣ιмage [тeхт]
║╠❂͜͡🌟➣vιdeo [тeхт]
║╠❂͜͡🌟➣zodιaĸ [тeхт]
║╠❂͜͡🌟➣yoυтυвe [тeхт]
║╠❂͜͡🌟➣lιrιĸ [тeхт]
║╠❂͜͡🌟➣ιdlιne [тeхт]
║╠❂͜͡🌟➣мυѕιc [тeхт]
║╠❂͜͡🌟➣тιмe [тιмe]
║╠❂͜͡🌟➣ѕay [тeхт]
║╚════════════
╚═════════════
"""

translateMessage ="""
╔═════════════
║    ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║      Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠☔тr-ιd = ιndoneѕιa
║╠☔тr-мy = мyanмar
║╠☔тr-en = englιѕн
║╠☔тr-тн = тнaιland
║╠☔тr-ja = japaneѕe
║╠☔тr-мѕ = мalayѕιa
║╠☔тr-ιт = ιтalιan
║╠☔тr-тr = тυrĸιѕн
║╠☔тr-aғ = aғrιĸaanѕ
║╠☔тr-ѕq = alвanιan
║╠☔тr-aм = aмнarιc
║╠☔тr-ar = araвιc
║╠☔тr-нy = arмenιan
║╚════════════
╚═════════════
"""

botMessage ="""
╔═════════════
║    ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║      Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂͜͡⚡➣nĸ [naмe]
║╠❂͜͡⚡➣vĸ [naмe]
║╠❂͜͡⚡➣nυĸe
║╠❂͜͡⚡➣lυrĸιng > Cctv
║╠❂͜͡⚡➣тeѕ
║╠❂͜͡⚡➣reѕpon
║╠❂͜͡⚡➣ѕpeed
║╠❂͜͡⚡➣glιѕт
║╠❂͜͡⚡➣тagall/Crot
║╠❂͜͡⚡➣reѕтarт
║╠❂͜͡⚡➣cn [тeхт]
║╠❂͜͡⚡➣cѕ [тeхт]
║╠❂͜͡⚡➣мe
║╠❂͜͡⚡➣craѕн
║╚════════════
╚═════════════
"""

settingMessage ="""
╔═════════════
║    ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║      Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂͜͡🌟➣ѕeт
║╠❂͜͡🌟➣тag on/oғғ
║╠❂͜͡🌟➣тag2 on/oғғ
║╠❂͜͡🌟➣aυтolιĸe on/oғғ
║╠❂͜͡🌟➣add on/oғғ
║╠❂͜͡🌟➣joιn on/oғғ
║╠❂͜͡🌟➣ѕнare on/oғғ
║╠❂͜͡🌟➣coммenт on/oғғ
║╠❂͜͡🌟➣ĸ on/oғғ
║╠❂͜͡🌟➣njoιn on/oғғ
║╠❂͜͡🌟➣nleave on/oғғ
║╚════════════
╚═════════════
"""

giftMessage ="""
╔═════════════
║    ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║      Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂͜͡🌟➣gιғт
║╠❂͜͡🌟➣gιғт 1
║╠❂͜͡🌟➣gιғт 2
║╠❂͜͡🌟➣gιғт 3
║╚════════════
╚═════════════
"""

stealMessage ="""
╔═════════════
║    ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║      Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂͜͡🌟➣geтnaмe @
║╠❂͜͡🌟➣geтвιo @
║╠❂͜͡🌟➣geтιnғo @
║╠❂͜͡🌟➣geтpp @
║╠❂͜͡🌟➣geтcover @
║╠❂͜͡🌟➣geтмιd @
║╠❂͜͡🌟➣geтgroυp
║╠❂͜͡🌟➣ѕeтιмage [lιnĸ]
║╠❂͜͡🌟➣papιмage
║╠❂͜͡🌟➣ѕeтvιdeo [lιnĸ]
║╠❂͜͡🌟➣papvιdeo
║╠❂͜͡🌟➣мycopy @
║╠❂͜͡🌟➣мyвacĸυp
║╚════════════
╚═════════════
"""
KAC=[cl,ki,kk,kc,kl]
mid = cl.getProfile().mid
Smid = satpam.getProfile().mid

Bots=[mid]
owner=["mid lu",mid]
admin=["mid lu",mid]
baby=["mid rekan bot"]#chery/barby/ranita
creator=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1"]
owner=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':True,
    'message':"""👉😊☆º°˚˚☆✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰☆º°˚˚☆（＾ω＾）\n\nby Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««""",
    "lang":"JP",
    "comment":"""👉😊☆º°˚˚☆✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰☆º°˚˚☆（＾ω＾）\n\nby Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««""",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "QrProtect":False,
    "MProtection":False,
    "Protectguest":False,
    "Protectcancel":False,
    "autoKick":False,
    "auto":True,
    "tag":False,
    "tag2":False,
    "likeOn":False,
    "Mimic":False,
    "mimic":False,
    "winvite":False,
    "winvite2":False,
    "Wc":False,
    "Lv":False,
    "pname":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "protectionOn":False,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = cl.getProfile()
profile = cl.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

mulai = time.time()

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def translate(to_translate, to_language="auto", language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':'Mozilla/5.0'}
    cari_hasil = 'class="t0">'
    request = urllib2.Request(url, headers=agent)
    page = urllib2.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

#def autolike():
#			for zx in range(0,100):
#				hasil = cl.activity(limit=100)
#				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#					try:
#						cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#						cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By TobyBots!!\nID LINE : line://ti/p/~tobyg74\nIG : instagram.com/tobygaming74")
#						print "DiLike"
#					except:
#							pass
#				else:
#						print "Sudah DiLike"
#			time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

#def autolike():
#    for zx in range(0,100):
#      hasil = cl.activity(limit=100)
#      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#        try:
#          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
#          print "Like"
#        except:
#          pass
#      else:
#          print "Already Liked"
#time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImage(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.client.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n9§9" + Name
                wait2['ROM'][op.param1][op.param2] = "9§9" + Name
        else:
            pass
    except:
        pass

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }

        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        print r
        if r.status_code != 201:
            raise Exception('Upload audio failure.')


def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e

def sendVoice(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentPreview = None
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'voice_message',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload voice failure.')
        return True



def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "► @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         cl.sendMessage(msg)
    except Exception as error:
        print error

def removeAllMessages(self, lastMessageId):
     return self._client.removeAllMessages(0, lastMessageId)

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if wait["auto"] == True:
                cl.acceptGroupInvitation(op.param1)
                cl.sendText(op.param1, "Terima Kasih Telah Invite 👉😊☆º°˚˚☆✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰☆º°˚˚☆（＾ω＾）\n\nby Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««\n\nSilahkan ketik [Help],dan gunakan dgn bijak")
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                ki.findAndAddContactsByMid(op.param1)
                kc.findAndAddContactsByMid(op.param1)
                kl.findAndAddContactsByMid(op.param1)
                kk.findAndAddContactsByMid(op.param1)

                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    cl.sendText(op.param1,str(wait["message"]))
                    kc.sendText(op.param1,str(wait["message"]))
                    cl.sendText(op.param1,str(wait["message"]))

#------------------NOTIFIED_READ_MESSAGE----------------#
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e

        if op.type == 26:
            msg = op.message

            if msg.text is None:
                return

            if "@"+cl.getProfile().displayName in msg.text:
                if wait["tag"] == True:
                    tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                    jawab = ("Kenapa Tag Si "+cl.getProfile().displayName+"Kangen yah..!!!\nPC aja langsung biar anu hihi..!!\n[autoRespon]by=>SelfBot~Kris\n👉Cyber Army Bot👈","Nah ngetag lagi si "+cl.getProfile().displayName+" mending ajak mojok aja dari pada ngetag mulu.. wkwk...!!!\n[autoRespon]by=>SelfBot~Kris\n👉Cyber Army Bot👈")
                    jawaban = random.choice(jawab)
                    cl.sendText(msg.to,jawaban)

        if op.type == 26:
            msg = op.message

            if msg.text is None:
                return

            if "@"+cl.getProfile().displayName in msg.text:
                if wait["tag2"] == True:
                    tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                    jawab = "Kenapa Tag Si "+cl.getProfile().displayName+"Kangen yah..!!!\nPC aja langsung biar anu hihi..!!\n[autoRespon]by=>SelfBot~Kris\n👉Cyber Army Bot👈","Nah ngetag lagi si "+cl.getProfile().displayName+" mending ajak mojok aja dari pada ngetag mulu.. wkwk...!!!\n[autoRespon]by=>SelfBot~Kris\n👉Cyber Army Bot👈"
                    jawaban = random.choice(jawab)
                    cl.sendText(msg.to,jawaban)
                    cl.kickoutFromGroup(msg.to,[msg.from_])
                else:
                    cl.inviteIntoGroup(op.param1,admin)
                    #cl.sendAudio(msg.to,jawaban)
        #--CANCEL KICK--#
        if op.type == 32:
            if wait["Protectcancel"] == True:
                if op.param2 not in Bots or staff:
                    cl.kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
                  cl.cancelGroupInvitation(op.param1,[op.param3])
                  cl.kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#

        #----MemberProtection------#
        if op.type == 19:
            if wait["MProtection"] == True:
                if op.param2 not in Bots and staff:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param3])
        #------Open QR Kick start------#
        if op.type == 11:
            if wait["QrProtect"] == True:
                if op.param2 not in Bots:
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.kickoutFromGroup(op.param1,[op.param3])
                    cl.updateGroup(G)
        #------Open QR Kick finish-----#

        if op.type == 17:
           if wait["Wc"] == True:
               if op.param2 in Bots:
                 return
               ginfo = cl.getGroup(op.param1)
               cl.sendText(op.param1, "╔═════════════\n║Selamat Datang Di  " + str(ginfo.name) + "\n╠═════════════\n" + "║Founder =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Semoga Betah Kak 😘 \n╠═════════════\n║No Baper,No nakal,No Ngeyel ya..!! \n╚═════════════")
               print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1, "╔═════════════\n║Baper Tuh Orang :v \n╠══════���══════\n║Belum di Anu Kayanya 😊 \n╚═════════════")
                print "MEMBER HAS LEFT THE GROUP"
#-----------------------------------------------
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = cl.getGroup(op.param1)
                        except:
                            try:
                                G = cl.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = kl.getGroup(op.param1)
				    except:
					try:
                                            G = kt.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        kl.updateGroup(G)
                                    except:
                                        try:
                                            kt.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in Bots:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kt.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"please do not change group name-_-")
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin or owner:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break

#--------------NOTIFIED_INVITE_INTO_GROUP----------------
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in creator:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in creator:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in creator:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in creator:
		    kc.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in mid:
		if op.param2 in Amid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Bmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Cmid:
		    cl.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Amid:
		if op.param2 in mid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Bmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Cmid:
		    ki.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Bmid:
		if op.param2 in mid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Amid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Cmid:
		    kk.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Cmid:
		if op.param2 in mid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Amid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Bmid:
		    kc.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner or mid:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"

            if Amid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner or mid:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
#====================================================
	    if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                else:
		    cl.rejectGroupInvitation(op.param1)
	    else:
                if wait["autoCancel"] == True:
		    if op.param3 in admin:
			pass
		    else:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			cl.cancelGroupInvitation(op.param1, [op.param3])
			cl.sendText(op.param1, "Itu kicker jgn di invite!")
		    else:
			pass
#-----------------NOTIFIED_KICKOUT_FROM_GROUP-----------------

        if op.type == 19:
            if op.param3 in admin:
                 cl.kickoutFromGroup(op.param1,[op.param2])
                 cl.inviteIntoGroup(op.param1,admin)
                 cl.inviteIntoGroup(op.param1,[op.param3])
            else:
                pass
        if op.type == 19:
            if op.param3 in baby:
                 cl.kickoutFromGroup(op.param1,[op.param2])
                 cl.inviteIntoGroup(op.param1,baby)
                 cl.inviteIntoGroup(op.param1,[op.param3])
            else:
                pass
        if op.type == 19:
            if op.param3 in baby:
                if op.param2 in baby:
                 cl.inviteIntoGroup(op.param1,baby)
                 cl.inviteIntoGroup(op.param1,[op.param3])
#------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
            if wait["autoKick"] == True:
                    if op.param2 in admin:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
			cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
			    cl.kickoutFromGroup(op.param1,[op.param2])
			    cl.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in admin:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in admin:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
#====================================================
                    if mid in op.param3:
                        if op.param2 in Bots:
                            pass
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                            if op.param2 in wait["blacklist"]:
                                pass
                            else:
                                if op.param2 in Bots:
                                    pass
                                else:
                                    wait["blacklist"][op.param2] = True
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ti = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True

                    if Amid in op.param3:
                        if op.param2 in Bots:
                            pass
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                            if op.param2 in wait["blacklist"]:
                                pass
                            else:
                                if op.param2 in Bots:
                                    pass
                                else:
                                    wait["blacklist"][op.param2] = True

                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
            if op.param3 in admin or owner:
              if op.param2 not in Bots:
                try:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  cl.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
#================================================================
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
#-----------------------------------------
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        cl.sendText(msg.to,"deleted")
                        cl.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        cl.sendText(msg.to,"It is not in the black list")
                        cl.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        cl.sendText(msg.to,"already")
                        cl.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        cl.sendText(msg.to,"aded")
                        cl.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        cl.sendText(msg.to,"deleted")
                        cl.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        cl.sendText(msg.to,"It is not in the black list")
                        cl.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL�0�10��9�0�16�0�69�0�3�0�4\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["help","Help"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key1"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,translateMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key7"]:
                if msg.from_ in admin or owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,botMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key2"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,socmedMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key4"]:
                if msg.from_ in admin or owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,protectMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key5"]:
                if msg.from_ in admin or owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,settingMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key6"]:
                if msg.from_ in admin or owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,stealMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif msg.text in ["Key3"]:
                if msg.from_ in admin or owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,giftMessage)
					else:
						cl.sendText(msg.to,helpt)
#--------------------------------------------------
            elif ("Gn " in msg.text):
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						cl.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")
#--------------------------------------------------
            elif ("Kr1 gn " in msg.text):
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Kr1 gn ","")
						ki.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")
#--------------------------------------------------
            elif ("Kr2 gn " in msg.text):
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Kr2 gn ","")
						kk.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")
#--------------------------------------------------
            elif ("Kr3 gn " in msg.text):
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Kr3 gn ","")
						kc.updateGroup(X)
					else:
						kc.sendText(msg.to,"It can't be used besides the group.")
#--------------------------------------------------
            elif "Kick " in msg.text:
				if msg.from_ in admin or owner:
					midd = msg.text.replace("Kick ","")
					cl.kickoutFromGroup(msg.to,[midd])
#--------------------------------------------------
            elif "Kr1 kick " in msg.text:
				if msg.from_ in admin or owner:
					midd = msg.text.replace("Kr1 kick ","")
					ki.kickoutFromGroup(msg.to,[midd])
#--------------------------------------------------
            elif "Kr2 kick " in msg.text:
				if msg.from_ in admin or owner:
					midd = msg.text.replace("Kr2 kick ","")
					kk.kickoutFromGroup(msg.to,[midd])
#--------------------------------------------------
            elif "Kr3 kick " in msg.text:
				if msg.from_ in admin or owner:
					midd = msg.text.replace("Kr3 kick ","")
					kc.kickoutFromGroup(msg.to,[midd])
#--------------------------------------------------
            elif "Invite " in msg.text:
				if msg.from_ in admin or owner:
					midd = msg.text.replace("Invite ","")
					cl.findAndAddContactsByMid(midd)
					cl.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------
            elif "Kr1 invite " in msg.text:
				if msg.from_ in admin or owner:
					midd = msg.text.replace("Kr1 invite ","")
					ki.findAndAddContactsByMid(midd)
					ki.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------
            elif "Kr2 invite " in msg.text:
				if msg.from_ in admin or owner:
					midd = msg.text.replace("Kr2 invite ","")
					kk.findAndAddContactsByMid(midd)
					kk.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------
            elif "Kr3 invite " in msg.text:
				if msg.from_ in admin or owner:
					midd = msg.text.replace("Kr3 invite ","")
					kc.findAndAddContactsByMid(midd)
					kc.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------
            elif msg.text in ["Me"]:
                if msg.from_ in admin or owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["K1"]:
				if msg.from_ in admin or owner:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Amid}
					ki.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Kr2"]:
				if msg.from_ in admin or owner:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Bmid}
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["cancel","Kr cancel"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						G = k3.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							k3.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								k3.sendText(msg.to,"No one is inviting")
							else:
								k3.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							k3.sendText(msg.to,"Can not be used outside the group")
						else:
							k3.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Ourl","Link on","Urlon"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            elif msg.text in ["Kr1 ourl","Kr1 link on"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done Chivas")
						else:
							cl.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            elif msg.text in ["Kr2 ourl","Kr2 link on"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done Chivas")
						else:
							cl.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            elif msg.text in ["Kr3 ourl","Kr3 link on"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = False
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            elif msg.text in ["Curl","Link off","Urloff"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            elif msg.text in ["Kr1 curl","Kr1 link off"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done Chivas")
						else:
							cl.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            elif msg.text in ["Kr2 curl","Kr2 link off"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done Chivas")
						else:
							cl.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            elif msg.text in ["Kr3 curl","Kr3 link off"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = True
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
#--------------------------------------------------
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            elif "Id" == msg.text:
				if msg.from_ in admin or owner:
					cl.sendText(msg.to,msg.to)
#--------------------------------------------------
            elif "All mid" == msg.text:
				if msg.from_ in admin or owner:
					cl.sendText(msg.to,mid)
					cl.sendText(msg.to,Amid)
					cl.sendText(msg.to,Bmid)
					kc.sendText(msg.to,Cmid)
#--------------------------------------------------
            elif "Mid" == msg.text:
				if msg.from_ in admin or owner:
					cl.sendText(msg.to,mid)
#--------------------------------------------------
            elif "Kr1 mid" == msg.text:
				if msg.from_ in admin or owner:
					cl.sendText(msg.to,Amid)
#--------------------------------------------------
            elif "Kr2 mid" == msg.text:
				if msg.from_ in admin or owner:
					cl.sendText(msg.to,Bmid)
#--------------------------------------------------
            elif "Kr3 mid" == msg.text:
				if msg.from_ in admin or owner:
					kc.sendText(msg.to,Cmid)
#--------------------------------------------------
            elif msg.text in ["Wkwk"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "100",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Hehehe"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "10",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "9",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["You"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "7",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Hadeuh"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "6",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Please"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "4",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Haaa"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "3",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Lol"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "110",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Hmmm"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "101",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Come"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "247",
										"STKPKGID": "3",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["TL "]:
				if msg.from_ in admin or owner:
					tl_text = msg.text.replace("TL ","")
					cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#--------------------------------------------------
            elif msg.text in ["Undang"]:
              if msg.from_ in admin or owner:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
#--------------------------------------------------
            elif msg.text in ["Kr1 rename "]:
				if msg.from_ in admin or owner:
					string = msg.text.replace("Cv1 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = ki.getProfile()
						profile_B.displayName = string
						ki.updateProfile(profile_B)
						cl.sendText(msg.to,"name " + string + " done")
#--------------------------------------------------
            elif msg.text in ["Kr2 rename "]:
				if msg.from_ in admin or owner:
					string = msg.text.replace("Cv2 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = kk.getProfile()
						profile_B.displayName = string
						kk.updateProfile(profile_B)
						cl.sendText(msg.to,"name " + string + " done")
#--------------------------------------------------
            elif msg.text in ["Mc "]:
				if msg.from_ in admin or owner:
					mmid = msg.text.replace("Mc ","")
					msg.contentType = 13
					msg.contentMetadata = {"mid":mmid}
					cl.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Guest On","guest on"]:
              if msg.from_ in admin or owner:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
#--------------------------------------------------
            elif msg.text in ["Guest Off","guest off"]:
              if msg.from_ in admin or owner:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
#--------------------------------------------------
            elif msg.text in ["Ã©â‚¬Â£Ã§ÂµÂ¡Ã¥â�1�7�1�71¤7¦Ë 1�71¤7:Ã£â€šÂªÃ£Æ�1�7�Â�1�7�1�71¤7","K on","Contact on","Ã©Â¡Â¯Ã§Â¤ÂºÃ¯Â¼Å¡Ã©â€�1�7�â�1�7�1�71¤7 1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
#--------------------------------------------------
            elif msg.text in ["Ã©â‚¬Â£Ã§ÂµÂ¡Ã¥â�1�7�1�71¤7¦Ë 1�71¤7:Ã£â€šÂªÃ£Æ�1�7�â�1�7�1�71¤7 1�71¤7","K off","Contact off","Ã©Â¡Â¯Ã§Â¤ÂºÃ¯Â¼Å¡Ã©â€�1�7�Å�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
#--------------------------------------------------
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¥Ââ 1�71¤7šÃ¥Å 1�71¤7 :Ã£â€šÂªÃ£Æ�1�7�Â�1�7�1�71¤7","Join on","Auto join:on","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¥ÂÆ’Ã¥Å�1�7�1�71¤7 Ã¯Â¼Å¡Ã©â€�1�7�â�1�7�1�71¤7 1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
#--------------------------------------------------
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¥Ââ 1�71¤7šÃ¥Å 1�71¤7 :Ã£â€šÂªÃ£Æ�1�7�â�1�7�1�71¤7 1�71¤7","Join off","Auto join:off","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¥ÂÆ’Ã¥Å�1�7�1�71¤7 Ã¯Â¼Å¡Ã©â€�1�7�Å�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
#--------------------------------------------------
            elif msg.text in ["Gcancel:"]:
				if msg.from_ in admin or owner:
					try:
						strnum = msg.text.replace("Gcancel:","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								cl.sendText(msg.to,"Ã¥â€¦Â³Ã¤Âºâ�1�7�1�71¤7 Ã©â 1�71¤7šâ‚¬Ã¨Â¯Â·Ã¦â€¹â 1�71¤7™Ã§Â»ÂÃ£â�1�7�¬â€šÃ¨Â¦ÂÃ¦â 1�71¤7”Â¶Ã¥Â¼â�1�7�¬Ã¨Â¯Â·Ã¦Å�1�7�â€¡Ã¥Â®Å¡Ã¤ÂºÂºÃ¦â 1�71¤7¢Â°Ã¥Ââ 1�71¤7˜Ã©â‚¬Â1�7")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								cl.sendText(msg.to,strnum + "Ã¤Â½Â¿Ã¤ÂºÂºÃ¤Â»Â¥Ã¤Â¸â€¹Ã§Å¡â�1�7�1�71¤7žÃ¥Â°ÂÃ§Â»â 1�71¤7žÃ§â 1�71¤7Â¨Ã¨â 1�71¤7¡ÂªÃ¥Å Â¨Ã©â 1�71¤7šâ‚¬Ã¨Â¯Â·Ã¦â€¹â 1�71¤7™Ã§Â»Â�1�7�1�71¤7")
					except:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Value is wrong")
						else:
							cl.sendText(msg.to,"Bizarre ratings")
#--------------------------------------------------
            elif msg.text in ["Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â 1�71¤7¹â 1�71¤7¢Ã©â‚¬â�1�7�¬Ã¥â�1�7�1�71¤7¡Â 1�71¤7:Ã£â€šÂªÃ£Æ�1�7�Â�1�7�1�71¤7","Leave on","Auto leave:on","Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â 1�71¤7¹â 1�71¤7¢Ã©â‚¬â�1�7�¬Ã¥â�1�7�1�71¤7¡ÂºÃ¯Â¼Å¡Ã©â 1�71¤7“â�1�7�1�71¤7 1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â�1�7�¬Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â 1�71¤7¹â 1�71¤7¢Ã©â‚¬â�1�7�¬Ã¥â�1�7�1�71¤7¡Â 1�71¤7:Ã£â€šÂªÃ£Æ�1�7�â�1�7�1�71¤7 1�71¤7","Leave off","Auto leave:off","Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â 1�71¤7¹â 1�71¤7¢Ã©â‚¬â�1�7�¬Ã¥â�1�7�1�71¤7¡ÂºÃ¯Â¼Å¡Ã©â 1�71¤7”Å�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already")
#--------------------------------------------------
            elif msg.text in ["Ã¥â€¦Â±Ã¦Å�1�7�â�1�7�1�71¤7 1�71¤7:Ã£â€šÂªÃ£Æ�1�7�Â�1�7�1�71¤7","Share on","Share on"]:
				if msg.from_ in admin or owner:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â�1�7�¬Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Ã¥â€¦Â±Ã¦Å�1�7�â�1�7�1�71¤7 1�71¤7:Ã£â€šÂªÃ£Æ�1�7�â�1�7�1�71¤7 1�71¤7","Share off","Share off"]:
				if msg.from_ in admin or owner:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â�1�7�1�71¤7¦Â³Ã¦â 1�71¤7“Â­Ã£â�1�7�¬â€ 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Set","Status"]:
				if msg.from_ in admin or owner:
					md = ""
					if wait["contact"] == True: md+="[􀜁􀇔Mask􏿿] CONTACT : [✅]\n"
					else: md+="[􀜁􀇔Mask􏿿] CONTACT : [❌]\n"
					if wait["autoJoin"] == True: md+="[􀜁􀇔Mask􏿿] AUTOJOIN : [✅]\n"
					else: md +="[􀜁􀇔Mask􏿿] AUTOJOIN : [❌]\n"
					if wait["autoCancel"]["on"] == True:md+="[􀜁􀇔Mask􏿿] GROUP CANCEL :" + str(wait["autoCancel"]["members"]) + "\n"
					else: md+="[􀜁􀇔Mask􏿿􏿿] GROUP CANCEL : [❌]\n"
					if wait["leaveRoom"] == True: md+="[􀜁􀇔Mask􏿿] AUTOLEAVE : [✅]\n"
					else: md+="[􀜁􀇔􀜁􀇔Mask􏿿􏿿] AUTOLEAVE : [❌]\n"
					if wait["timeline"] == True: md+="[􀜁􀇔Mask􏿿] SHARE : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] SHARE : [❌]\n"
					if wait["autoAdd"] == True: md+="[􀜁􀇔Mask􏿿] AUTOADD : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] AUTOADD : [❌]\n"
					if wait["commentOn"] == True: md+="[􀜁􀇔Mask􏿿] COMMENT : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] COMMENT : [❌]\n"
					if wait["likeOn"] == True: md+="[􀜁􀇔Mask􏿿] AUTOLIKE : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] AUTOLIKE : [❌]\n"
					if wait["QrProtect"] == True: md+="[􀜁􀇔Mask􏿿] PROTECT QR : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] PROTECT QR : [❌]\n"
					if wait["MProtection"] == True:md+="[􀜁􀇔Mask􏿿] PROTECT MEMBER : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] PROTECT MEMBER : [❌]\n"
					if wait["Protectguest"] == True:md+="[􀜁􀇔Mask􏿿] PROTECT GUEST : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] PROTECT GUEST : [❌]\n"
					if wait["Protectcancel"] == True:md+="[􀜁􀇔Mask􏿿] PROTECT CANCEL : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] PROTECT CANCEL : [❌]\n"
					if wait["autoKick"] == True:md+="[􀜁􀇔Mask􏿿] PROTECT KICK : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] PROTECT KICK : [❌]\n"
					if wait["Wc"] == True: md+="[􀜁􀇔Mask􏿿] WELCOME : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] WELCOME : [❌]\n"
					if wait["Lv"] == True: md+="[􀜁􀇔Mask􏿿] LEAVE : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] LEAVE : [❌]\n"
					if wait["tag"] == True: md+="[􀜁􀇔Mask􏿿] TAG 1 : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] TAG 1 : [❌]\n"
					if wait["tag2"] == True: md+="[􀜁􀇔Mask􏿿] TAG 2 : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] TAG 2 : [❌]\n"
					if wait["auto"] == True: md+="[􀜁􀇔Mask􏿿] AutoBot Join : [✅]\n"
					else:md+="[􀜁􀇔Mask􏿿] AutoBot Join : [❌]\n"
					cl.sendText(msg.to,md)
#--------------------------------------------------
            elif "album merit " in msg.text:
				if msg.from_ in admin or owner:
					gid = msg.text.replace("album merit ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"Ã§â€ºÂ¸Ã¥â�1�7�1�71¤7 Å’Ã¦Â²Â¡Ã¥Å�1�7�Â¨Ã£â�1�7�¬â€ 1�71¤7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "Ã¤Â»Â¥Ã¤Â¸â€¹Ã¦ËœÂ¯Ã¥Â¯Â¹Ã¨Â±Â¡Ã§Å¡â�1�7�1�71¤7žÃ§â 1�71¤7ºÂ¸Ã¥â 1�71¤7 Å 1�71¤7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
						cl.sendText(msg.to,mg)
#--------------------------------------------------
            elif "album " in msg.text:
				if msg.from_ in admin or owner:
					gid = msg.text.replace("album ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"Ã§â€ºÂ¸Ã¥â�1�7�1�71¤7 Å’Ã¦Â²Â¡Ã¥Å�1�7�Â¨Ã£â�1�7�¬â€ 1�71¤7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "Ã¤Â»Â¥Ã¤Â¸â€¹Ã¦ËœÂ¯Ã¥Â¯Â¹Ã¨Â±Â¡Ã§Å¡â�1�7�1�71¤7žÃ§â 1�71¤7ºÂ¸Ã¥â 1�71¤7 Å 1�71¤7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
#--------------------------------------------------
            elif "album remove " in msg.text:
				if msg.from_ in admin or owner:
					gid = msg.text.replace("album remove ","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Deleted albums")
					else:
						cl.sendText(msg.to,str(i) + "Ã¥Ë 1�7 Ã©â„¢Â¤Ã¤Âºâ�1�7�1�71¤7 Ã¤Âºâ 1�71¤7¹Ã§Å¡â 1�71¤7žÃ§â 1�71¤7ºÂ¸Ã¥â 1�71¤7 Å’Ã£â�1�7�¬â€ 1�71¤7")
            elif msg.text in ["Group id","Ã§Â¾Â¤Ã§Âµâ€žÃ¥â�1�7�1�71¤7¦Â¨id"]:
				if msg.from_ in admin or owner:
					gid = cl.getGroupIdsJoined()
					h = ""
					for i in gid:
						h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
					cl.sendText(msg.to,h)
#--------------------------------------------------
            elif msg.text in ["Clear"]:
				if msg.from_ in admin or owner:
					gid = cl.getGroupIdsInvited()
					for i in gid:
						cl.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"All invitations have been refused")
					else:
						cl.sendText(msg.to,"Ã¦â€¹â�1�7�1�71¤7™Ã§Â»ÂÃ¤Âºâ�1�7�1�71¤7 Ã¥â 1�71¤7¦Â¨Ã©Æ’Â¨Ã§Å¡â�1�7�1�71¤7žÃ©â 1�71¤7šâ‚¬Ã¨Â¯Â·Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif "album removeÃ¢â€ â�1�7�1�71¤7 1�71¤7" in msg.text:
				if msg.from_ in admin or owner:
					gid = msg.text.replace("album removeÃ¢â€ â�1�7�1�71¤7 1�71¤7","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Albums deleted")
					else:
						cl.sendText(msg.to,str(i) + "Ã¥Ë 1�7 Ã©â„¢Â¤Ã¤Âºâ�1�7�1�71¤7 Ã¤Âºâ 1�71¤7¹Ã§Å¡â 1�71¤7žÃ§â 1�71¤7ºÂ¸Ã¥â 1�71¤7 Å’Ã£â�1�7�¬â€ 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¨Â¿Â½Ã¥Å 1�71¤7 :Ã£â€šÂªÃ£Æ�1�7�Â�1�7�1�71¤7","Add on","Auto add:on","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¨Â¿Â½Ã¥Å 1�71¤7 Ã¯Â¼Å¡Ã©â€�1�7�â�1�7�1�71¤7 1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â�1�7�¬Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¨Â¿Â½Ã¥Å 1�71¤7 :Ã£â€šÂªÃ£Æ�1�7�â�1�7�1�71¤7 1�71¤7","Add off","Auto add:off","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¨Â¿Â½Ã¥Å 1�71¤7 Ã¯Â¼Å¡Ã©â€�1�7�Å�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â�1�7�1�71¤7¦Â³Ã¦â 1�71¤7“Â­Ã£â�1�7�¬â€ 1�71¤7")
#--------------------------------------------------
            elif "Message change: " in msg.text:
				if msg.from_ in admin or owner:
					wait["message"] = msg.text.replace("Message change: ","")
					cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
				if msg.from_ in admin or owner:
					wait["message"] = msg.text.replace("Message add: ","")
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message changed")
					else:
						cl.sendText(msg.to,"doneÃ£â‚¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Message","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã¨Â¿Â½Ã¥Å 1�71¤7 Ã¥â€¢ÂÃ¥â�1�7�¬â�1�7�¢Ã¨ÂªÅ¾Ã§Â¢ÂºÃ¨ÂªÂ�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message change to\n\n" + wait["message"])
					else:
						cl.sendText(msg.to,"The automatic appending information is set as followsÃ£â‚¬â�1�7�1�71¤7š\n\n" + wait["message"])
#--------------------------------------------------
            elif "Comment:" in msg.text:
				if msg.from_ in admin or owner:
					c = msg.text.replace("Comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"message changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
#--------------------------------------------------
            elif "Add comment:" in msg.text:
				if msg.from_ in admin or owner:
					c = msg.text.replace("Add comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"String that can not be changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["Ã£â€šÂ³Ã£Æ�1�7�Â¡Ã£Æ�1�7�Â³Ã£Æ�1�7�Ë�1�7�1�71¤7:Ã£â€šÂªÃ£Æ�1�7�Â�1�7�1�71¤7","Comment on","Comment:on","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã©Â¦â 1�71¤7“Ã�1�7�1�71¤7 ÂÃ§â€¢â�1�7�¢Ã¨Â¨â�1�7�¬Ã¯Â¼Å¡Ã©â�1�7�1�71¤7“â�1�7�1�71¤7 1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["commentOn"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already on")
					else:
						wait["commentOn"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â�1�7�¬Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
            elif msg.text in ["Ã£â€šÂ³Ã£Æ�1�7�Â¡Ã£Æ�1�7�Â³Ã£Æ�1�7�Ë�1�7�1�71¤7:Ã£â€šÂªÃ£Æ�1�7�â�1�7�1�71¤7 1�71¤7","Comment on","Comment off","Ã¨â€¡ÂªÃ¥â�1�7�1�71¤7¹â 1�71¤7¢Ã©Â¦â 1�71¤7“Ã�1�7�1�71¤7 ÂÃ§â€¢â�1�7�¢Ã¨Â¨â�1�7�¬Ã¯Â¼Å¡Ã©â�1�7�1�71¤7”Å�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
					if wait["commentOn"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already off")
					else:
						wait["commentOn"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â�1�7�1�71¤7¦Â³Ã¦â 1�71¤7“Â­Ã£â�1�7�¬â€ 1�71¤7")
            elif msg.text in ["Comment","Ã§â€¢â�1�7�¢Ã¨Â¨â�1�7�¬Ã§Â¢ÂºÃ¨ÂªÂ�1�7�1�71¤7"]:
				if msg.from_ in admin or owner:
					cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							cl.updateGroup(x)
						gurl = cl.reissueGroupTicket(msg.to)
						cl.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Kr1 gurl"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							ki.updateGroup(x)
						gurl = ki.reissueGroupTicket(msg.to)
						cl.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Kr2 gurl"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kk.updateGroup(x)
						gurl = kk.reissueGroupTicket(msg.to)
						cl.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Kr3 gurl"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kc.updateGroup(x)
						gurl = kc.reissueGroupTicket(msg.to)
						kc.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
				if msg.from_ in admin or owner:
					wait["wblack"] = True
					cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
				if msg.from_ in admin or owner:
					wait["dblack"] = True
					cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
				if msg.from_ in admin or owner:
					if wait["commentBlack"] == {}:
						cl.sendText(msg.to,"confirmed")
					else:
						cl.sendText(msg.to,"Blacklist")
						mc = ""
						for mi_d in wait["commentBlack"]:
							mc += "" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
				if msg.from_ in admin or owner:
					if wait["clock"] == True:
						cl.sendText(msg.to,"already on")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
				if msg.from_ in admin or owner:
					if wait["clock"] == False:
						cl.sendText(msg.to,"already off")
					else:
						wait["clock"] = False
						cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
				if msg.from_ in admin or owner:
					n = msg.text.replace("Change clock ","")
					if len(n.decode("utf-8")) > 13:
						cl.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
				if msg.from_ in admin or owner:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"Updated")
					else:
						cl.sendText(msg.to,"Please turn on the name clock")


            elif msg.text == "CCtv":
                    cl.sendText(msg.to, "Check sider Eror"),
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Toong":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal \n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n¡¸Cctv¡¹you can send  read point will be created ")
#-----------------------------------------------
            elif msg.text in ["Crot"]:
                              group = cl.getGroup(msg.to)
                              nama = [contact.mid for contact in group.members]
                              nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                              if jml <= 100:
                                 mention(msg.to, nama)
                              if jml > 100 and jml < 200:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 mention(msg.to, nm1)
                                 for j in range (100, len(nama)-1):
                                        nm2 += [nama[j]]
                                 mention(msg.to, nm2)
                              if jml > 200 and jml < 300:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 mention(msg.to, nm1)
                                 for j in range (100, 199):
                                        nm2 += [nama[j]]
                                 mention(msg.to, nm2)
                                 for k in range (200, len(nama)-1):
                                        nm3 += [nama[k]]
                                 mention(msg.to, nm3)
                              if jml > 300 and jml < 400:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 mention(msg.to, nm1)
                                 for j in range (100, 199):
                                        nm2 += [nama[j]]
                                 mention(msg.to, nm2)
                                 for k in range (200, 299):
                                        nm3 += [nama[k]]
                                 mention(msg.to, nm3)
                                 for l in range (300, len(nama)-1):
                                     nm4 += [nama[l]]
                                 mention(msg.to, nm4)
                              cnt = Message()
                              cnt.text = "Hasil Tag : "+str(jml)
                              cnt.to = msg.to
                              cl.sendText(msg.to,"TAGALL SUCCESS")
                              cl.sendMessage(cnt)
#-----------------------------------------------

            elif msg.text in ["Kr"]:
				if msg.from_ in admin or owner:
						G = cl.getGroup(msg.to)
						ginfo = cl.getGroup(msg.to)
						G.preventJoinByTicket = True
						cl.updateGroup(G)
						invsend = 0
						Ticket = cl.reissueGroupTicket(msg.to)
						ki.acceptGroupInvitationByTicket(msg.to,Ticket)
						time.sleep(0.2)
						kk.acceptGroupInvitationByTicket(msg.to,Ticket)
						time.sleep(0.2)
						kc.acceptGroupInvitationByTicket(msg.to,Ticket)
						time.sleep(0.2)
						G = cl.getGroup(msg.to)
						G.preventJoinByTicket = True
						ki.updateGroup(G)
						print "kicker ok"
						G.preventJoinByTicket(G)
						ki.updateGroup(G)

            elif msg.text in ["Kr1 join"]:
				if msg.from_ in admin or owner:
					X = cl.getGroup(msg.to)
					X.preventJoinByTicket = False
					cl.updateGroup(X)
					invsend = 0
					Ti = cl.reissueGroupTicket(msg.to)
					ki.acceptGroupInvitationByTicket(msg.to,Ti)
					G = cl.getGroup(msg.to)
					G.preventJoinByTicket = True
					ki.updateGroup(G)
					Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Kr2 join"]:
				if msg.from_ in admin or owner:
					X = cl.getGroup(msg.to)
					X.preventJoinByTicket = False
					cl.updateGroup(X)
					invsend = 0
					Ti = cl.reissueGroupTicket(msg.to)
					kk.acceptGroupInvitationByTicket(msg.to,Ti)
					G = cl.getGroup(msg.to)
					G.preventJoinByTicket = True
					kk.updateGroup(G)
					Ticket = kk.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Kr3 join"]:
				if msg.from_ in admin or owner:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							print "kicker ok"
							G.preventJoinByTicket = True
							kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Out","out"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							cl.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
							kc.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Ranita pergi"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							cl.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
							cl.leaveGroup(msg.to)
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Ranita bye"]:
                if msg.from_ in admin or owner:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							cl.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
							cl.leaveGroup(msg.to)
							ki.leaveGroup(msg.to)
						except:
							pass
						
            elif msg.text in ["Kr pergi"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							cl.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
							cl.leaveGroup(msg.to)
							ki.leaveGroup(msg.to)
						except:
							pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							cl.sendText(msg.to,"Fuck You")
							cl.sendText(msg.to,"Fuck You")
							return
						for jj in matched_list:
							try:
								klist=[cl]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[jj])
								print (msg.to,[jj])
							except:
								print

            elif "Glist" in msg.text:
                if msg.from_ in owner:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "☄ %s  \n" % (cl.getGroup(i).name + " 👥 ▄ [ " + str(len (cl.getGroup(i).members))+" ]")
                        cl.sendText(msg.to, "     ☄ [ ♡List Grup♄ ] ☜\n"+ h +"Total Group ▄" +"[ "+str(len(gid))+" ]")
            elif "Cium " in msg.text:
                if msg.from_ in admin or owner or mid:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"] [0] ["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendText(msg.to,"Error")
            elif "Ready ah" in msg.text:
				if msg.from_ in owner:
					if msg.toType == 2:
						print "ok"
						_name = msg.text.replace("Ready ah","")
						gs = cl.getGroup(msg.to)
						cl.sendText(msg.to,"Perintah DiLaksanakan Maaf Kan Saya :v Ã´")
						cl.sendText(msg.to,"Group DiBersihkan.")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
						if targets == []:
							cl.sendText(msg.to,"Not found.")
							cl.sendText(msg.to,"Not found.")
						else:
							for target in targets:
								try:
									klist=[cl]
									kicker=random.choice(klist)
									kicker.kickoutFromGroup(msg.to,[target])
									print (msg.to,[g.mid])
								except:
									cl.sendText(msg.to,"Group cleanse")
									cl.sendText(msg.to,"Group cleanse")
            elif msg.text in ["Salam1"]:
                cl.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                cl.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif "Salam3" in msg.text:
              if msg.from_ in owner:
                cl.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Assalamu'alaikum")
                cl.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Salam3","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"maaf kalo gak sopan")
                    cl.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
                    cl.sendText(msg.to,"hehehhehe")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                cl.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                cl.sendText(msg.to,"Nah salamnya jawab sendiri dah")
            elif "Nk " in msg.text:
				if msg.from_ in owner:
						nk0 = msg.text.replace("Nk ","")
						nk1 = nk0.lstrip()
						nk2 = nk1.replace("@","")
						nk3 = nk2.rstrip()
						_name = nk3
						gs = cl.getGroup(msg.to)
						targets = []
						for s in gs.members:
							if _name in s.displayName:
								targets.append(s.mid)
						if targets == []:
							cl.sendMessage(msg.to,"user does not exist")
							pass
						else:
							for target in targets:
									try:
										klist=[cl]
										kicker=random.choice(klist)
										kicker.kickoutFromGroup(msg.to,[target])
										print (msg.to,[g.mid])
									except:
										cl.sendText(msg.to,"Succes Kick")
										cl.sendText(msg.to,"Fuck You"),
            elif "Ndang " in msg.text:
                if msg.from_ in owner:
                    nk0 = msg.text.replace("Ndang ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    gs.preventJoinByTicket = False
                    cl.updateGroup(gs)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    satpam.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    if targets == []:
                       sendMessage(msg.to,"user does not exist")
                       pass
                    else:
                       for target in targets:
                          try:
                            satpam.kickoutFromGroup(msg.to,[target])
                            print (msg.to,[g.mid])
                          except:
                            satpam.leaveGroup(msg.to)
                            gs = cl.getGroup(msg.to)
                            gs.preventJoinByTicket = True
                            cl.updateGroup(gs)
                            gs.preventJoinByTicket(gs)
                            cl.updateGroup(gs)
            elif "Blacklist @ " in msg.text:
				if msg.from_ in admin or owner:
					_name = msg.text.replace("Blacklist @ ","")
					_kicktarget = _name.rstrip(' ')
					gs = ki2.getGroup(msg.to)
					targets = []
					for g in gs.members:
						if _kicktarget == g.displayName:
							targets.append(g.mid)
							if targets == []:
								cl.sendText(msg.to,"Not found")
							else:
								for target in targets:
									try:
										wait["blacklist"][target] = True
										f=codecs.open('st2__b.json','w','utf-8')
										json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
										k3.sendText(msg.to,"Succes Van")
									except:
										cl.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						print "[Ban]ok"
						_name = msg.text.replace("Ban @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = cl.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							cl.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Berhasil Memban")
								except:
									cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						print "[Unban]ok"
						_name = msg.text.replace("Unban @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = cl.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							cl.sendText(msg.to,"Tidak DiTemukan")
							cl.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Berhasil")
								except:
									cl.sendText(msg.to,"Berhasil")
#-----------------------------------------------
            elif msg.text == "Cctv":
                    cl.sendText(msg.to, "Lurking Is Starting!! "+ datetime.today().strftime('%H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text in ["Intip"]:
                 if msg.toType == 2:
                    print "\nRead aktif..."
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "Sider :\n  ===========================                     %s\n===========================\n\nReader :\n%s\n===========================\nIn the last seen point:\n[%s]\n===========================" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "\nReading Point Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "lukers"
                        cl.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik [Lurking] for [Lurkers]")
#-------------------------------------
            elif "Cn " in msg.text:
              if msg.from_ in admin or owner:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"UpdateName => " + string + " <= Success")
#----------------------------
            elif "Vk " in msg.text:
              if msg.from_ in admin or owner:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#-----------------------------------------------
            elif msg.text.lower() == 'crash':
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    cl.sendMessage(msg)
                    cl.sendMessage(msg)
                    cl.sendMessage(msg)
#-----------------------------------------------
            elif msg.text in ["Tes"]:
				if msg.from_ in admin or owner:
					cl.sendText(msg.to,"Kr Hadir Boss!!")
#-----------------------------------------------
            elif msg.text in ["Mode On","mode on"]:
                if msg.from_ in admin or owner:
                    if wait["QrProtect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect QR On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect QR On")
                        else:
                            cl.sendText(msg.to,"done")
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    if msg.to in wait['pname']:
                        cl.sendText(msg.to,"TURN ON")
                    else:
                        cl.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"proтecт cancel on")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"noтιғ joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"noтιғ leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                    if wait["autoKick"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Kick on")
                    else:
                        wait["autoKick"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                    if wait["tag"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Tag On")
                    else:
                        wait["tag"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tag On")
                        else:
                            cl.sendText(msg.to,"already on")
                    if wait["tag2"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Yang ngeTag Kick on")
                        else:
                            cl.sendText(msg.to,"Yang ngeTag Kick on")
                    else:
                        wait["tag2"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Yang ngeTag Kick on")
                        else:
                            cl.sendText(msg.to,"Yang ngeTag Kick on")
                    if wait["Protectguest"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Guest Stranger On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Guest Stranger On")
                        else:
                            cl.sendText(msg.to,"done")
#=================================================
            elif msg.text in ["Mode Off","mode off"]:
                if msg.from_ in admin or owner:
                    if wait["QrProtect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect QR Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect QR Off")
                        else:
                            cl.sendText(msg.to,"done")
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    if msg.to in wait['pname']:
                        cl.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        cl.sendText(msg.to,"ALREADY OFF")
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"proтecт cancel oғғ")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect already oғғ")
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"noтιғ joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Nayapa yg gabung already oғғ")
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"noтιғ leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Nayapa yg left already oғғ")
                    if wait["autoKick"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Kick oғғ")
                    else:
                        wait["autoKick"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Kick already oғғ")
                    if wait["tag"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already Tag off")
                        else:
                            cl.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tag Off")
                        else:
                            cl.sendText(msg.to,"Already Tag off")
                    if wait["tag2"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Yang ngeTag Kick off")
                        else:
                            cl.sendText(msg.to,"Yang ngeTag Kick off")
                    else:
                        wait["tag2"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Yang ngeTag Kick off")
                        else:
                            cl.sendText(msg.to,"Yang ngeTag Kick off")
                    if wait["Protectguest"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Guest Stranger Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Guest Stranger Off")
                        else:
                            cl.sendText(msg.to,"done")
#===================================================
            elif msg.text in ["Qr On","qr on"]:
              if msg.from_ in admin or owner:
                if wait["QrProtect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["QrProtect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr Off","qr off"]:
              if msg.from_ in admin or owner:
                if wait["QrProtect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["QrProtect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
#-----------------------------------------------
            elif msg.text in ["Member On"]:
                if msg.from_ in admin or owner:
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection On")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Member Off"]:
                if msg.from_ in admin or owner:
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
#-----------------------------------------------
            elif "Kr say " in msg.text:
					bctxt = msg.text.replace("Kr say ","")
					cl.sendText(msg.to,(bctxt))
					cl.sendText(msg.to,(bctxt))
            elif ".. " in msg.text:
					bctxt = msg.text.replace(".. ","")
					cl.sendText(msg.to,(bctxt))
					cl.sendText(msg.to,(bctxt))
            elif msg.text in ["Creator"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u31ef22df7f538df1d74dc7f756ef1a32"}
					cl.sendText(msg.to,"MyCreator")
					ki.sendMessage(msg)
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u9cc2323f5b84f9df880c33aa9f9e3ae1"}
					cl.sendText(msg.to,"MyCreator")
					cl.sendText(msg.to,"Simanis madu ya!!")
					ki.sendMessage(msg)
#-------------Fungsi Creator Finish-----------------#
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                #Vicky Kull~
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
#----------------------------------------------------
            elif "Cs " in msg.text:
              if msg.from_ in admin or owner:
                string = msg.text.replace("Cs","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                else:
                    cl.sendText(msg.to,"Done")
#-----------------------------------------------
#            elif "say " in msg.text.lower():
#                say = msg.text.lower().replace("say ","")
#                lang = 'id'
#                tts = gTTS(text=say, lang=lang)
#                tts.save("hasil.mp3")
#                cl.sendAudio(msg.to,"hasil.mp3")
#--------------------
            elif 'wiki ' in msg.text.lower():
                try:
                    wiki = msg.text.lower().replace("wiki ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=3)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    cl.sendText(msg.to, pesan)
                except:
                        try:
                            pesan="Over Text Limit! Please Click link\n"
                            pesan+=wikipedia.page(wiki).url
                            cl.sendText(msg.to, pesan)
                        except Exception as e:
                            cl.sendText(msg.to, str(e))
#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Bisa Jadi","Mungkin")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
                cl.sendText(msg.to,jawaban)
                cl.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif "Rate " in msg.text:
                tanya = msg.text.replace("Rate ","")
                jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif "Getname @" in msg.text:
                if msg.from_ in admin or owner:
                    _name = msg.text.replace("Getname @","")
                    _nametarget = _name.rstrip(" ")
                    gs = cl.getGroup(msg.to)
                    for h in gs.members:
                      if _nametarget == h.displayName:
                          cl.sendText(msg.to,"[DisplayName]:\n" + h.displayName )
                      else:
                        pass

            elif "Getbio @" in msg.text:
                if msg.from_ in admin or owner:
                    _name = msg.text.replace("Getbio @","")
                    _nametarget = _name.rstrip(" ")
                    gs = cl.getGroup(msg.to)
                    for h in gs.members:
                      if _nametarget == h.displayName:
                          cl.sendText(msg.to,"[Status]:\n" + h.statusMessage )
                      else:
                        pass
#-----------------------------------------------
#-----------------------------------------------
            elif "zodiak " in msg.text:
                tanggal = msg.text.replace("zodiak ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
#-----------------------------------------------
            elif msg.text in ["Invite creator"]:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass

            elif msg.text in ["Gcreator:kick"]:
	           if msg.from_ in admin or owner:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.kickoutFromGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass

#----------------------------------------------
            elif "Stalk " in msg.text:
                 print "[Command]Stalk executing"
                 stalkID = msg.text.replace("Stalk ","")
                 subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])
                 files = glob.glob("tmp/*.jpg")
                 for file in files:
                     os.rename(file,"tmp/tmp.jpg")
                 fileTmp = glob.glob("tmp/tmp.jpg")
                 if not fileTmp:
                     cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                     print "[Command]Stalk,executed - no image found"
                 else:
                     image = upload_tempimage(client)
                     cl.sendText(msg.to, format(image['link']))
                     subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                     print "[Command]Stalk executed - succes"
#-------------------------------------------------------------
            elif "Gbc " in msg.text:
                if msg.from_ in admin or owner:
                    bctxt = msg.text.replace("Gbc ", "")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendText(manusia, (bctxt))
            elif "Pm cast " in msg.text:
                if msg.from_ in admin or owner:
					bctxt = msg.text.replace("Pm cast ", "")
					t = cl.getAllContactIds()
					for manusia in t:
						cl.sendText(manusia,(bctxt))
            elif "Fbc " in msg.text:
                if msg.from_ in admin or owner:
                    bctxt = msg.text.replace("Fbc ", "")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendText(manusia, (bctxt))
#----------------------------------------------------------
            elif "Meikarta: " in msg.text:
                if msg.from_ in admin or owner:
                    gid = msg.text.replace("Meikarta: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#------------------------------------------------------
            elif "Getcover @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getcover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#-----------------------------------------------
            elif "Getpp @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getpp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#--------------------------------------------
            elif msg.text in ["Autolike on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Autolike off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")
#------------------------------------------------------------------
            elif "Group On" in msg.text:
                if msg.from_ in admin or owner:
                    if msg.to in wait['pname']:
                        cl.sendText(msg.to,"TURN ON")
                    else:
                        cl.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Group Off" in msg.text:
                if msg.from_ in admin or owner:
                    if msg.to in wait['pname']:
                        cl.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        cl.sendText(msg.to,"ALREADY OFF")
            elif "Turn off" in msg.text:
               if msg.from_ in admin or owner:
                 try:
                     import sys
                     sys.exit()
                     cl.sendText(msg.to, "Bot is Turn Off")
                 except:
                     pass
#------------------------------------------------------------------
            elif msg.text in ["Cancel On"]:
                if msg.from_ in admin or owner:
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"proтecт cancel on")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
            elif msg.text in ["Cancel Off"]:
                if msg.from_ in admin or owner:
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"proтecт cancel oғғ")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already oғғ")
#--------------------------
            elif msg.text in ["Njoin on"]:
                if wait["Wc"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ joιn on")
                else:
                    wait["Wc"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Njoin off"]:
                if wait["Wc"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ joιn oғғ")
                else:
                    wait["Wc"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already oғғ")
#--------------------------
            elif msg.text in ["Nleave on"]:
                if wait["Lv"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ leave on")
                else:
                    wait["Lv"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Nleave off"]:
                if wait["Lv"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ leave oғғ")
                else:
                    wait["Lv"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already oғғ")
##--------------------------
            elif msg.text in ["Kick On"]:
                if msg.from_ in admin or owner:
                    if wait["autoKick"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Kick on")
                    else:
                        wait["autoKick"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
            elif msg.text in ["Kick Off"]:
                if msg.from_ in admin or owner:
                    if wait["autoKick"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Kick oғғ")
                    else:
                        wait["autoKick"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already oғғ") #----------------------------------------------------------------
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
#------------------------------------------------
            elif 'lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
#-----------------------------------
            elif "idline " in msg.text:
                id = msg.text.replace("idline ", "")
                find = cl.findContactsByUserId(id)
                for findid in find:
                    try:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': findid.mid}
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error
#-----------------------------------
            elif "Getgroup" in msg.text:
                group = cl.getGroup(msg.to)
                path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                cl.sendImageWithURL(msg.to, path)
#----------------------------------
            elif "reinvite" in msg.text.split():
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        try:
                            grCans = [contact.mid for contact in group.invitee]
                            cl.findAndAddContactByMid(msg.to, grCans)
                            cl.cancelGroupInvitation(msg.to, grCans)
                            cl.inviteIntoGroup(msg.to, grCans)
                        except Exception as error:
                            print error
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No Invited")
                        else:
                            cl.sendText(msg.to,"Error")
                else:
                    pass
#----------------------------------
            elif "Leavegroup " in msg.text.split():
                if msg.from_ in admin or owner:
                    ng = msg.text.split().replace("Leavegroup ","")
                    gid = cl.getGroupIdsJoined()
                    if msg.from_ in admin or owner:
                        for i in gid:
                            h = cl.getGroup(i).name
                    if h == ng:
                        cl.sendText(i,"Bot di paksa keluar oleh owner!")
                        cl.leaveGroup(i)
                        ki.leaveGroup(i)
                        kk.leaveGroup(i)
                        kc.leaveGroup(i)
                        cl.sendText(msg.to,"Success left ["+ h +"] group")
                #else:
                    #pass
            #else:
                #cl.sendText(msg.to,"Khusus Creator/Admin")
            elif msg.text in ["LG"]: #Melihat List Group
                if msg.from_ in admin or owner:
                    gids = cl.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                        #####gn = cl.getGroup(i).name
                        h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
                        cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))

            elif msg.text in ["LG2"]: #Melihat List Group + ID Groupnya (Gunanya Untuk Perintah InviteMeTo:)
                if msg.from_ in owner:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                        cl.sendText(msg.to,h)
      #--------------List Group------------
            elif "Asupka: " in msg.text:
                if msg.from_ in owner:
                    gid = msg.text.replace("Asupka: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#----------------------------------
            elif "Getcontact " in msg.text:
              if msg.from_ in admin or owner:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
#----------------------------------
            elif "youtube " in msg.text.lower():
                 query = msg.text.lower().replace("youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                             cl.sendText(msg.to,'Judul : ' + a['title'] + '\nLink : ' + 'http://www.youtube.com' + a['href'])
#---------------------------------
#-----------------------------------------
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,van)
#-----------------------------------------
            elif msg.text in ["Restart"]:
                if msg.from_ in owner:
                    cl.sendText(msg.to, "Bot has been restarted")
                    restart_program()
                    print "@Restart"
#-----------------------------------------
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin or owner:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e
#-----------------------------------------
            elif "Getinfo @" in msg.text:
                nama = msg.text.replace("Getinfo @","")
                target = nama.rstrip(' ')
                van = cl.getGroup(msg.to)
                for linedev in van.members:
                    if target == linedev.displayName:
                        mid = cl.getContact(linedev.mid)
                        #./linedev/ervan
                        try:
                            cover = cl.channel.getCover(linedev.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + mid.displayName + "\n[Mid]:\n" + linedev.mid + "\n[BIO]:\n" + mid.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + mid.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass

            elif "Getinfo2 " in msg.text:
                mid = msg.text.replace("Getinfo2 ","")
                anu = cl.getContact(mid)
                try:
                    cover = cl.channel.getCover(mid)
                except:
                    cover = ""
                cl.sendText(msg.to,"[Display Name]:\n" + anu.displayName + "\n[Mid]:\n" + mid + "\n[BIO]:\n" + anu.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + anu.pictureStatus + "\n[Cover]:\n" + str(cover))
#-----------------------------------------
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName

                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
#-----------------------------------------------
            elif msg.text in ["Tag on"]:
                if wait["tag"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Tag On")
                else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag On")
                    else:
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Tag off"]:
                if wait["tag"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Tag Off")
                else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag Off")
                    else:
                        cl.sendText(msg.to,"Already off")

            elif msg.text in ["Tag2 on"]:
                if msg.from_ in admin or owner:
                    if wait["tag2"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Tag On")
                    else:
                        wait["tag2"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tag On")
                        else:
                            cl.sendText(msg.to,"already on")
            elif msg.text in ["Tag2 off"]:
                if msg.from_ in admin or owner:
                    if wait["tag2"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already off")
                        else:
                            cl.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag2"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tag Off")
                        else:
                            cl.sendText(msg.to,"Already off")

            elif msg.text in ["Auto on"]:
                if msg.from_ in admin or owner:
                    if wait["auto"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Bot join on")
                        else:
                            cl.sendText(msg.to,"Bot join On")
                    else:
                        wait["auto"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Bot join On")
                        else:
                            cl.sendText(msg.to,"Bot join On")
            elif msg.text in ["Auto off"]:
                if msg.from_ in admin or owner:
                    if wait["auto"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Bot join off")
                        else:
                            cl.sendText(msg.to,"Bot join off")
                    else:
                        wait["auto"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Bot join off")
                        else:
                            cl.sendText(msg.to,"Bot join off")
#-----------------------------------------------
            elif "Admadd @" in msg.text:
                if msg.from_ in admin or owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admadd @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Telah Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command Di Tolak Jangan Sedih")
                    cl.sendText(msg.to,"Sudah Menjadi Admin Maka Tidak Bisa Menjadi Admin Lagi")

            elif "Admrem @" in msg.text:
                if msg.from_ in admin or owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admrem @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Telah Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin Tidak Bisa Menggunakan")

            elif msg.text in ["Adminlist",".alist"]:
              if msg.from_ in admin or owner:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Sabar Dikit Mamang.....")
                    mc = ""
                    for mi_d in admin:
                        mc += "☄1�7 " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------------------------------
            elif "Setimage " in msg.text:
                wait["Pap"] = msg.text.replace("Setimage ","")
                cl.sendText(msg.to,"Image Has Ben Set To")

            elif msg.text in ["Papimage","/Papim"]:
                cl.sendImageWithURL(msg.to,wait["Pap"])
            elif "Setvideo " in msg.text:
                wait["Vid"] = msg.text.replace("Setvideo ","")
                cl.sendText(msg.to,"Video Has Ben Set To")

            elif msg.text in ["Papvideo","/Papvid"]:
                cl.sendVideoWithURL(msg.to,wait["Vid"])
#-----------------------------------------------
#-----------------------------------------------
            elif ("Ban " in msg.text):
              if msg.from_ in admin or owner:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass
#-----------------------------------------------
            elif "Kapan " in msg.text:
                tanya = msg.text.replace("Kapan ","")
                jawab = ("Besok","Tahun Depan","Minggu Depan","Satu Abad")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin or owner:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.CloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e

            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#--------------------------------------
            elif msg.text in ["Time"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)
                #client.sendText(msg.to, rst)
#-----------------------------------------------
            elif "image " in msg.text:
                search = msg.text.replace("image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
#-----------------------------------------------
            elif 'ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
#-----------------------------------------------
            elif "Tr-id " in msg.text:
                nk0 = msg.text.replace("Tr-id ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'id')
                cl.sendText(msg.to,str(trans))
            elif "Tr-th " in msg.text:
                nk0 = msg.text.replace("Tr-th ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'th')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ja " in msg.text:
                nk0 = msg.text.replace("Tr-ja ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ja')
                cl.sendText(msg.to,str(trans))
            elif "Tr-en " in msg.text:
                nk0 = msg.text.replace("Tr-en ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'en')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ms " in msg.text:
                nk0 = msg.text.replace("Tr-ms ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ms')
                cl.sendText(msg.to,str(trans))
            elif "Tr-it " in msg.text:
                nk0 = msg.text.replace("Tr-it ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'it')
                cl.sendText(msg.to,str(trans))
            elif "Tr-tr " in msg.text:
                nk0 = msg.text.replace("Tr-tr ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'tr')
                cl.sendText(msg.to,str(trans))
            elif "Tr-my " in msg.text:
                nk0 = msg.text.replace("Tr-my ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'my')
                cl.sendText(msg.to,str(trans))
            elif "Tr-af " in msg.text:
                nk0 = msg.text.replace("Tr-af ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'af')
                cl.sendText(msg.to,str(trans))
            elif "Tr-sq " in msg.text:
                nk0 = msg.text.replace("Tr-sq ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'sq')
                cl.sendText(msg.to,str(trans))
            elif "Tr-am " in msg.text:
                nk0 = msg.text.replace("Tr-am ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'am')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ar " in msg.text:
                nk0 = msg.text.replace("Tr-ar ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ar')
                cl.sendText(msg.to,str(trans))
            elif "Tr-hy " in msg.text:
                nk0 = msg.text.replace("Tr-hy ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'hy')
                cl.sendText(msg.to,str(trans))
#----------------UpdateFotoProfil----------------#
            elif "Cpp" in msg.text:
                if msg.from_ in admin or owner:
                    path = "syn.jpg"
                    cl.sendText(msg.to,"Update PP :")
                    cl.sendImage(msg.to,path)
                    cl.updateProfilePicture(path)
#----------------------------------------
#----------------------------------------------------------------------------
            elif "Steal @" in msg.text:
                if msg.from_ in admin or owner:
                    _name = msg.text.replace("Steal @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendImageWithURL(msg.to, path)
                            except:
                                pass
#-----------------------------------------------
            elif "Steal " in msg.text:
                if msg.from_ in admin or owner:
                    salsa = msg.text.replace("Steal ","")
                    Manis = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)
#--------------------------CEK SIDER------------------------------

            elif "setview" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Checkpoint checked!")
                print "@setview"

            elif "viewseen" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "List Viewer\n*"
                        grp = '\n* '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        cl.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"
#--------------------------CEK SIDER------------------------------
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			cl.sendMessage(msg)
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			cl.sendMessage(msg)
            elif "Mimic:" in msg.text:
            		cmd = msg.text.replace("Mimic:","")
            		if cmd == "on":
            			if mimic["status"] == False:
            				mimic["status"] = True
            				cl.sendText(msg.to,"Mimic on")
            			else:
            				cl.sendText(msg.to,"Mimic already on")
            		elif cmd == "off":
            			if mimic["status"] == True:
            				mimic["status"] = False
            				cl.sendText(msg.to,"Mimic off")
            			else:
            				cl.sendText(msg.to,"Mimic already off")
            		elif "Add:" in cmd:
            			target0 = msg.text.replace("Add:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						mimic["target"][target] = True
            						cl.sendText(msg.to,"Success added target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed")
            						break
            		elif "Del:" in cmd:
            			target0 = msg.text.replace("Del:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						del mimic["target"][target]
            						cl.sendText(msg.to,"Success deleted target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed!")
            						break
            		elif cmd == "ListTarget":
            			if mimic["target"] == {}:
            				cl.sendText(msg.to,"No target")
                    	else:
                    		lst = "<<Lit Target>>"
                    		total = len(mimic["target"])
                    		for a in mimic["target"]:
                				if mimic["target"][a] == True:
                					stat = "On"
                				else:
                					stat = "Off"
                				lst += "\n☄1�7" + cl.getContact(mi_d).displayName + " | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
#----------------------------------------------------------------
#--------------------------------
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)

#------------------------------
#--------------------------------------
            elif msg.text in ["hmm"]:
					cl.sendText(msg.to,"Waduh kenapa gatel tenggorokan ya")
            elif msg.text in ["welcome","Kam"]:
					cl.sendText(msg.to,"Selamat datang di Group")
					cl.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
#-------------- Add Friends ------------
            elif "botadd @" in msg.text:
                if msg.from_ in admin or owner:
                  if msg.toType == 2:
                    if msg.from_ in admin or owner:
                      print "[Command]Add executing"
                      _name = msg.text.replace("botadd @","")
                      _nametarget = _name.rstrip('  ')
                      gs = cl.getGroup(msg.to)
                      gs = cl.getGroup(msg.to)
                      gs = cl.getGroup(msg.to)
                      gs = kc.getGroup(msg.to)
                      targets = []
                      for g in gs.members:
                        if _nametarget == g.displayName:
                          targets.append(g.mid)
                      if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                      else:
                        for target in targets:
                          try:
                            cl.findAndAddContactsByMid(target)
                            ki.findAndAddContactsByMid(target)
                            kk.findAndAddContactsByMid(target)
                            kc.findAndAddContactsByMid(target)
                            cl.senText(msg.to, "Berhasil Menambah Kan Teman")
                          except:
                            cl.sendText(msg.to,"Error")
                  else:
                    cl.sendText(msg.to,"Perintah Ditolak")
                    cl.sendText(msg.to,"Perintah ini Hanya Untuk Admin")
#-----------------------------------------------
            elif msg.text in ["Respon"]:
				if msg.from_ in admin or owner:
					cl.sendText(msg.to,"Bot 1")
					cl.sendText(msg.to,"Bot 2")
					cl.sendText(msg.to,"Bot 3")
            elif msg.text in ["Absen"]:
                    cl.sendText(msg.to,"👉★★★")
                    cl.sendText(msg.to,"👉★★★★")
                    cl.sendText(msg.to,"👉★★★★★")
                    cl.sendText(msg.to,"👉★★★★★★")
                    cl.sendText(msg.to,"👉★★★★★★★")
                    cl.sendText(msg.to,"👉Semua Hadir Boss...!!!\n\n[✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰]")
#-------------------------------------------------
            elif "Getmid @" in msg.text:
                if msg.from_ in admin or owner:
                  _name = msg.text.replace("Getmid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          cl.sendText(msg.to, g.mid)
                      else:
                          pass
#--------------------------
            elif msg.text in ["Bot kemari"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in admin or owner:
                gid = cl.getGroupIdsJoined()
                for i in gid:
                  cl.leaveGroup(i)
                  ki.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                  cl.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
#--------------------------
            elif "Bcast " in msg.text:
                if msg.from_ in admin or owner:
                    bc = msg.text.replace("Bcast ","")
                    gid = cl.getGroupIdsJoined()
                    for i in gid:
                        cl.sendText(i,"======[BROADCAST]======\n\n"+bc+"\n\n#BROADCAST!!")
#--------------------------------------------------------
            elif msg.text in ["Sp","Speed",".sp"]:
				if msg.from_ in admin or owner:
					start = time.time()
					cl.sendText(msg.to, "Lagi Proses...")
					cl.sendText(msg.to, "Santai...")
					elapsed_time = time.time() - start
					cl.sendText(msg.to, "%s/Detik" % (elapsed_time))
#------------------------------------------------------------------
            elif msg.text in ["Clearban"]:
               if msg.from_ in admin or owner:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"clear")
            elif msg.text in ["Ban"]:
				if msg.from_ in admin or owner:
					wait["wblacklist"] = True
					cl.sendText(msg.to,"Kirim Kontak")
            elif msg.text in ["Unban"]:
				if msg.from_ in admin or owner:
					wait["dblacklist"] = True
					cl.sendText(msg.to,"Kirim Kontak")
            elif msg.text in ["Banlist"]:
				if msg.from_ in admin or owner:
					if wait["blacklist"] == {}:
						cl.sendText(msg.to,"Tidak Ada")
					else:
						cl.sendText(msg.to,"Tunggu Sebentar Memuat Data")
						mc = ""
						for mi_d in wait["blacklist"]:
							mc += "☄1�7 " +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						cocoa = ""
						for mm in matched_list:
							cocoa += mm + "\n"
						cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							cl.sendText(msg.to,"There was no blacklist user")
							return
						for jj in matched_list:
							cl.kickoutFromGroup(msg.to,[jj])
						cl.sendText(msg.to,"Bye...")
            elif "Cancel" in msg.text:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							cl.cancelGroupInvitation(msg.to, gInviMids)
            elif "/Random:" in msg.text:
				if msg.from_ in admin or owner:
					if msg.toType == 2:
						strnum = msg.text.replace("/Random:","")
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						try:
							num = int(strnum)
							group = cl.getGroup(msg.to)
							for var in range(0,num):
								name = "".join([random.choice(source_str) for x in xrange(10)])
								time.sleep(0.01)
								group.name = name
								cl.updateGroup(group)
						except:
							cl.sendText(msg.to,"Error")
            elif "album" in msg.text:
				if msg.from_ in admin or owner:
					try:
						albumtags = msg.text.replace("album","")
						gid = albumtags[:6]
						name = albumtags.replace(albumtags[:34],"")
						cl.createAlbum(gid,name)
						cl.sendText(msg.to,name + "created an album")
					except:
						cl.sendText(msg.to,"Error")
            elif "fakecÃ¢â€ â�1�7�1�71¤7 1�71¤7" in msg.text:
				if msg.from_ in admin or owner:
					try:
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						name = "".join([random.choice(source_str) for x in xrange(10)])
						anu = msg.text.replace("fakecÃ¢â€ â�1�7�1�71¤7 1�71¤7","")
						cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
					except Exception as e:
						try:
							cl.sendText(msg.to,str(e))
						except:
							pass

            elif "ranita cium " in msg.text:
                if msg.from_ in admin or owner or mid:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"] [0] ["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendText(msg.to,"Error")

            elif msg.text in ["ranita glist"]: #Melihat List Group
                if msg.from_ in owner:
                    gids = cl.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                      #####gn = cl.getGroup(i).name
                      h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
                      cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))

            elif msg.text in ["ranita glist2"]:
                if msg.from_ in owner:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                      h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                      cl.sendText(msg.to,h)

            elif "ranita asupka " in msg.text:
                if msg.from_ in owner:
                    gid = msg.text.replace("barby asupka ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                            cl.sendText(msg.to,"succes di invite boss, silahkan masuk...!!")
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")

            elif "ranita bye" in msg.text:
                if msg.from_ in owner:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                        except:
                            pass
            elif "ranita megs " in msg.text:
                if msg.from_ in owner:
                    gName = msg.text.replace("ranita megs ","")
                    ap = cl.getGroups([msg.to])
                    semua = [contact.mid for contact in ap[0].members]
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        cl.createGroup(gName, semua)
                        cl.createGroup(gName, semua)
                        cl.createGroup(gName, semua)
                        cl.createGroup(gName, semua)
                        cl.createGroup(gName, semua)
                        cl.createGroup(gName, semua)
                        cl.createGroup(gName, semua)
            elif "#rmegs " in msg.text:
                if msg.from_ in owner:
                    gName = msg.text.replace("#rmegs ","")
                    ap = cl.getGroups([msg.to])
                    semua = findAndAddContactsByMid(Mi_d)
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        klis=[cl]
                        team=random.choice(klis)
                        cl.findAndAddContactsByMid(Mi_d)
                        cl.createGroup(gName, semua)
                        cl.createGroup(gName, semua)
                        cl.createGroup(gName, semua)
                        cl.createGroup(gName, semua)
                        cl.createGroup(gName, semua)
                        cl.createGroup(gName, semua)
                        team.findAndAddContactsByMid(Mi_d)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
            elif "Rrecover" in msg.text:
                if msg.from_ in owner:
                    thisgroup = cl.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    cl.createGroup("Rrecover", mi_d)
                    cl.sendText(msg.to,"Success recover")
            elif "ranita spin" in msg.text:
                if msg.from_ in owner:
                    thisgroup = cl.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.createGroup("Nah kan", mi_d)
                    cl.sendText(msg.to,"Success...!!!!")
            elif msg.text in ["Remove all chat"]:
                if msg.from_ in owner:
                    cl.removeAllMessages(op.param2)
                    ki.removeAllMessages(op.param2)
                    cl.sendText(msg.to,"Removed all chat Finish")
            elif msg.text in ["ranita muach"]:
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    cl.sendMessage(msg)
            elif msg.text in ["ranita","Ranita"]:
                if msg.from_ in owner:
                    cl.sendText(msg.to,"Ranita masih aktif Yank...!!!")

        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n-> " + Nama
                        wait2['ROM'][op.param1][op.param2] = "-> " + Nama
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    cl.sendText
            except:
                pass


        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True


def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

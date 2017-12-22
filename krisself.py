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
#JANGAN LUPA =>  sudo pip install bs4 => sudo pip install BeautifulSoup => sudo pip install urllib

kr = KRIS.LINE()
#kr.login(qr=True)
kr.login(token='')#r
kr.loginResult()

print "╔════════════════════════════════════════════════════\n╠❂➣[KRIS BERHASIL LOGIN]\n╚════════════════════════════════════════════════════"
reload(sys)
sys.setdefaultencoding('utf-8')

helpmsg ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣google (text)
║╠❂➣playstore (text)
║╠❂➣instagram (username)
║╠❂➣wikipedia (text)
║╠❂➣idline (text)
║╠❂➣time
║╠❂➣image (text)
║╠❂➣runtime
║╠❂➣Restart
║╠❂➣lirik (text)
║╠❂➣nah (mention)
║╠❂➣cctv on/off (Lurk)
║╠❂➣toong (Lurker)
║╠❂➣protect on/off
║╠❂➣qr on/off
║╠❂➣invite on/off
║╠❂➣Cancel on/off
║╠❂➣Simisimi:on/off
║╠❂➣Read on/off
║╠❂➣Getinfo @
║╠❂➣Getcontact @
║╠❂➣Cium @
║╠❂➣speed
║╠❂➣Friendlist
║╠❂➣id@en
║╠❂➣en@id
║╠❂➣id@jp
║╠❂➣keybot
║╚════════════
╚═════════════"""

keymsg ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣keypro
║╠❂➣keyself
║╠❂➣keygrup
║╠❂➣keyset
║╠❂➣keytran
║╠❂➣mode on/off
║╚════════════
╚═════════════"""

helppro ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣mode on/off
║╠❂➣protect on/off
║╠❂➣qr on/off
║╠❂➣invite on/off
║╠❂➣cancel on/off
║╚════════════
╚═════════════"""

helpself ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣Me
║╠❂➣Myname:
║╠❂➣Mybio:
║╠❂➣Mypict
║╠❂➣Mycover
║╠❂➣My copy @
║╠❂➣My backup
║╠❂➣Getgroup image
║╠❂➣Getmid @
║╠❂➣Getprofile @
║╠❂➣Getinfo @
║╠❂➣Getname @
║╠❂➣Getbio @
║╠❂➣Getpict @
║╠❂➣Getcover @
║╠❂➣nah (Mention)
║╠❂➣cctv on/off (Lurking)
║╠❂➣intip/toong (Lurkers)
║╠❂➣Micadd @
║╠❂➣Micdel @
║╠❂➣Mimic on/off
║╠❂➣Miclist
║╚════════════
╚═════════════"""

helpset ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣contact on/off
║╠❂➣autojoin on/off
║╠❂➣auto leave on/off
║╠❂➣autoadd on/off
║╠❂➣like friend
║╠❂➣link on
║╠❂➣respon on/off
║╠❂➣read on/off
║╠❂➣simisimi on/off
║╠❂➣Sambut on/off
║╠❂➣Pergi on/off
║╠❂➣Respontag on/off
║╠❂➣Kicktag on/off
║╚════════════
╚═════════════"""

helpgrup ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣Link on
║╠❂➣Url
║╠❂➣Cancel
║╠❂➣Gcreator
║╠❂➣Kick @
║╠❂➣Cium @
║╠❂➣Gname:
║╠❂➣Gbroadcast:
║╠❂➣Cbroadcast:
║╠❂➣Infogrup
║╠❂➣Gruplist
║╠❂➣Friendlist
║╠❂➣Blacklist
║╠❂➣Ban @
║╠❂➣Unban @
║╠❂➣Clearban
║╠❂➣Banlist
║╠❂➣Contact ban
║╠❂➣Midban
║╚════════════
╚═════════════"""

helptranslate ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : Kris
║ line://ti/p/~krissthea
╠═════════════
║╔════════════
║╠❂➣Id@en
║╠❂➣En@id
║╠❂➣Id@jp
║╠❂➣Jp@id
║╠❂➣Id@th
║╠❂➣Th@id
║╠❂➣Id@ar
║╠❂➣Ar@id
║╠❂➣Id@ko
║╠❂➣Ko@id
║╠❂➣Say-id
║╠❂➣Say-en
║╠❂➣Say-jp
║╚════════════
╚═════════════"""

KAC=[kr]
mid = kr.getProfile().mid

Bots=[mid]
admin=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1",mid]

wait = {
    "likeOn":False,
    "alwayRead":False,
    "detectMention":True,    
    "kickMention":False,
    "steal":True,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":5},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"""Thx for add""",
    "lang":"JP",
    "comment":"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"",
    "cNames":"",
    "Wc":False,
    "Lv":False,
    'MENTION':True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    }

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

contact = kr.getProfile()
backup = kr.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage                        
backup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
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

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       kr.sendMessage(msg)
    except Exception as error:
       print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                kr.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    kr.sendText(op.param1,str(wait["message"]))
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        kr.sendText(msg.to,text)
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in admin:
		    kr.acceptGroupInvitation(op.param1)
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or admin:
                  kr.acceptGroupInvitation(op.param1)
                else:
                  kr.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
        if op.type == 19:
            if op.param3 in admin:
                kr.kickoutFromGroup(op.param1,[op.param2])
                kr.inviteIntoGroup(op.param1,admin)
                kr.inviteIntoGroup(op.param1,[op.param3])
            else:
                pass
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                kr.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                kr.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            kr.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = kr.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            kr.updateGroup(G)
                        except:
                            kr.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    kr.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                kr.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        kr.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                kr.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))
                                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = kr.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Don't Tag Me! iam Bussy!, ",cName + "Ada perlu apa, ?",cName + " pc aja klo urgent! sedang sibuk,", "kenapa, ", cName + " kangen?","kangen bilang gak usah tag tag, " + cName, "knp?, " + cName, "apasi?, " + cName + "?", "pulang gih, " + cName + "?","aya naon, ?" + cName + "Tersangkut -_-"]
                     ret_ = "." + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  kr.sendText(msg.to,ret_)
                                  break            
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = kr.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy, ",cName + " Ngapain Ngetag?, ",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja, ", "-_-, ","Kris lagi off, ", cName + " Kenapa Tag saya?, ","SPAM PC aja, " + cName, "Jangan Suka Tag gua, " + cName, "Kamu siapa, " + cName + "?", "Ada Perlu apa, " + cName + "?","Tag doang tidak perlu., "]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  kr.sendText(msg.to,ret_)
                                  kr.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = kr.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             kr.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 kr.findAndAddContactsByMid(target)
                                 kr.inviteIntoGroup(msg.to,[target])
                                 kr.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      kr.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break
            
            #if msg.contentType == 13:
            #    if wait["steal"] == True:
            #        _name = msg.contentMetadata["displayName"]
            #        copy = msg.contentMetadata["mid"]
            #        groups = kr.getGroup(msg.to)
            #        pending = groups.invitee
            #        targets = []
            #        for s in groups.members:
            #            if _name in s.displayName:
            #                print "[Target] Stealed"
            #                break                             
            #            else:
            #                targets.append(copy)
            #        if targets == []:
            #            pass
            #        else:
            #            for target in targets:
            #                try:
            #                    kr.findAndAddContactsByMid(target)
            #                    contact = kr.getContact(target)
            #                    cu = kr.channel.getCover(target)
            #                    path = str(cu)
            #                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            #                    kr.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
            #                    kr.sendText(msg.to,"Profile Picture " + contact.displayName)
            #                    kr.sendImageWithURL(msg.to,image)
            #                    kr.sendText(msg.to,"Cover " + contact.displayName)
            #                    kr.sendImageWithURL(msg.to,path)
            #                    wait["steal"] = False
            #                    break
            #                except:
            #                        pass    
                                
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    kr.sendChatChecked(msg.from_,msg.id)
                else:
                    kr.sendChatChecked(msg.to,msg.id)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        kr.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        kr.sendText(msg.to,"Nothing")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        kr.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        kr.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        kr.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        kr.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        kr.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        kr.sendText(msg.to,"Done")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    kr.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kr.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = kr.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    kr.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,helpmsg)
                else:
                    kr.sendText(msg.to,helpmsg)
            elif msg.text.lower() == 'keybot':
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,keymsg)
                else:
                    kr.sendText(msg.to,keymsg)
            elif msg.text.lower() == 'keypro':
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,helppro)
                else:
                    kr.sendText(msg.to,helppro)
            elif msg.text.lower() == 'keyself':
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,helpself)
                else:
                    kr.sendText(msg.to,helpself)
            elif msg.text.lower() == 'keygrup':
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,helpgrup)
                else:
                    kr.sendText(msg.to,helpgrup)
            elif msg.text.lower() == 'keyset':
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,helpset)
                else:
                    kr.sendText(msg.to,helpset)
            elif msg.text.lower() == 'keytran':
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,helptranslate)
                else:
                    kr.sendText(msg.to,helptranslate)
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                kr.sendText(msg.to, "❂➣Proses.....")
                elapsed_time = time.time() - start
                kr.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif msg.text.lower() == 'crash':
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                kr.sendMessage(msg)
                kr.sendMessage(msg)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                kr.sendMessage(msg)
                
            elif ".fb" in msg.text:
                    a = msg.text.replace(".fb","")
                    b = urllib.quote(a)
                    kr.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Proses")
                    kr.sendText(msg.to, "https://www.facebook.com" + b)
                    kr.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Sukses")    
#======================== FOR COMMAND MODE ON STARTING ==========================#
            elif msg.text.lower() == 'mode on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protecion Already On")
                    else:
                        kr.sendText(msg.to,"Protecion Already On")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protecion Already On")
                    else:
                        kr.sendText(msg.to,"Protecion Already On")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Qr already On")
                    else:
                        kr.sendText(msg.to,"Protection Qr already On")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Qr already On")
                    else:
                        kr.sendText(msg.to,"Protection Qr already On")
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Invite already On")
                    else:
                        kr.sendText(msg.to,"Protection Invite already On")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                    else:
                        kr.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        kr.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        kr.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
#======================== FOR COMMAND MODE OFF STARTING ==========================#
            elif msg.text.lower() == 'mode off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection already Off")
                    else:
                        kr.sendText(msg.to,"Protection already Off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                    else:
                        kr.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Qr already off")
                    else:
                        kr.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Qr already Off")
                    else:
                        kr.sendText(msg.to,"Protection Qr already Off")
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Invite already Off")
                    else:
                        kr.sendText(msg.to,"Protection Invite already Off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Invite already Off")
                    else:
                        kr.sendText(msg.to,"Protection Invite already Off")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        kr.sendText(msg.to,"Protection Cancel already Off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        kr.sendText(msg.to,"Protection Cancel already Off")
#========================== FOR COMMAND BOT STARTING =============================#
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                    else:
                        kr.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                    else:
                        kr.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                    else:
                        kr.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                    else:
                        kr.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protecion Already On")
                    else:
                        kr.sendText(msg.to,"Protecion Already On")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protecion Already On")
                    else:
                        kr.sendText(msg.to,"Protecion Already On")
            elif msg.text.lower() == 'qr on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Qr already On")
                    else:
                        kr.sendText(msg.to,"Protection Qr already On")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Qr already On")
                    else:
                        kr.sendText(msg.to,"Protection Qr already On")
            elif msg.text.lower() == 'invite on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Invite already On")
                    else:
                        kr.sendText(msg.to,"Protection Invite already On")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                    else:
                        kr.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
            elif msg.text.lower() == 'cancel on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        kr.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        kr.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
            elif msg.text.lower() == 'autojoin on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                    else:
                        kr.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                    else:
                        kr.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
            elif msg.text.lower() == 'autojoin off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                    else:
                        kr.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                    else:
                        kr.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
            elif msg.text.lower() == 'protect off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection already Off")
                    else:
                        kr.sendText(msg.to,"Protection already Off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                    else:
                        kr.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
            elif msg.text.lower() == 'qr off':
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Qr already off")
                    else:
                        kr.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Qr already Off")
                    else:
                        kr.sendText(msg.to,"Protection Qr already Off")
            elif msg.text.lower() == 'invit off':
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Invite already Off")
                    else:
                        kr.sendText(msg.to,"Protection Invite already Off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Invite already Off")
                    else:
                        kr.sendText(msg.to,"Protection Invite already Off")
            elif msg.text.lower() == 'cancel off':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        kr.sendText(msg.to,"Protection Cancel already Off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        kr.sendText(msg.to,"Protection Cancel already Off")
            elif "Grup cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Grup cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                        else:
                            kr.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                        else:
                            kr.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Nilai tidak benar")
                    else:
                        kr.sendText(msg.to,"Weird value")
            elif msg.text.lower() == 'autoleave on':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        kr.sendText(msg.to,"Auto Leave room already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        kr.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'autoleave off':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        kr.sendText(msg.to,"Auto Leave room already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        kr.sendText(msg.to,"Auto Leave room already off")
            elif msg.text.lower() == 'share on':
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Share set to on")
                    else:
                        kr.sendText(msg.to,"Share already on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Share set to on")
                    else:
                        kr.sendText(msg.to,"Share already on")
            elif msg.text.lower() == 'share off':
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Share set to off")
                    else:
                        kr.sendText(msg.to,"Share already off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Share set to off")
                    else:
                        kr.sendText(msg.to,"Share already off")
            elif msg.text.lower() == 'status':
                md = """╔═════════════\n"""
                if wait["contact"] == True: md+="╠❂➣Contact:on [✅]\n"
                else: md+="╠❂➣Contact:off [❌]\n"
                if wait["autoJoin"] == True: md+="╠❂➣Auto Join:on [✅]\n"
                else: md +="╠❂➣Auto Join:off [❌]\n"
                if wait["autoCancel"]["on"] == True:md+="╠❂➣Auto cancel:" + str(wait["autoCancel"]["members"]) + "[✅]\n"
                else: md+= "╠❂➣Group cancel:off [❌]\n"
                if wait["leaveRoom"] == True: md+="╠❂➣Auto leave:on [✅]\n"
                else: md+="╠❂➣Auto leave:off [❌]\n"
                if wait["timeline"] == True: md+="╠❂➣Share:on [✅]\n"
                else:md+="╠❂➣Share:off [❌]\n"
                if wait["autoAdd"] == True: md+="╠❂➣Auto add:on [✅]\n"
                else:md+="╠❂➣Auto add:off [❌]\n"
                if wait["protect"] == True: md+="╠❂➣Protect:on [✅]\n"
                else:md+="╠❂➣Protect:off [❌]\n"
                if wait["linkprotect"] == True: md+="╠❂➣Link Protect:on [✅]\n"
                else:md+="╠❂➣Link Protect:off [❌]\n"
                if wait["inviteprotect"] == True: md+="╠❂➣Invitation Protect:on [✅]\n"
                else:md+="╠❂➣Invitation Protect:off [❌]\n"
                if wait["cancelprotect"] == True: md+="╠❂➣Cancel Protect:on [✅]\n"
                else:md+="╠❂➣Cancel Protect:off [❌]\n╚═════════════"
                kr.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u31ef22df7f538df1d74dc7f756ef1a32"}
                kr.sendMessage(msg)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u31ef22df7f538df1d74dc7f756ef1a32"}
                kr.sendMessage(msg)
                kr.sendText(msg.to,'❂➣ Creator yang manis kalem  􀜁􀄯􏿿')
            elif msg.text.lower() == 'autoadd on':
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Auto add set to on")
                    else:
                        kr.sendText(msg.to,"Auto add already on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Auto add set to on")
                    else:
                        kr.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'autoadd off':
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Auto add set to off")
                    else:
                        kr.sendText(msg.to,"Auto add already off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Auto add set to off")
                    else:
                        kr.sendText(msg.to,"Auto add already off")
            elif "Pesan set:" in msg.text:
                wait["message"] = msg.text.replace("Pesan set:","")
                kr.sendText(msg.to,"We changed the message")
            elif msg.text.lower() == 'pesan cek':
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
                else:
                    kr.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    kr.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                else:
                    wait["comment"] = c
                    kr.sendText(msg.to,"Ini telah diubah\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Aku berada di")
                    else:
                        kr.sendText(msg.to,"To open")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Comment Actived")
                    else:
                        kr.sendText(msg.to,"Comment Has Been Active")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Hal ini sudah off")
                    else:
                        kr.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Off")
                    else:
                        kr.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                kr.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:??\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                kr.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                kr.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    kr.sendText(msg.to,"Nothing in the blacklist")
                else:
                    kr.sendText(msg.to,"The following is a blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +kr.getContact(mi_d).displayName + "\n"
                    kr.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    kr.sendText(msg.to,"Jam already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = kr.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    kr.updateProfile(profile)
                    kr.sendText(msg.to,"Jam set on")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    kr.sendText(msg.to,"Jam already off")
                else:
                    wait["clock"] = False
                    kr.sendText(msg.to,"Jam set off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    kr.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    kr.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = kr.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    kr.updateProfile(profile)
                    kr.sendText(msg.to,"Diperbarui")
                else:
                    kr.sendText(msg.to,"Silahkan Aktifkan Jam")
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    kr.sendImageWithURL(msg.to,path)
                except:
                    pass
#========================== FOR COMMAND BOT FINISHED =============================#
            elif "Spam change:" in msg.text:
                if msg.toType == 2:
                 wait["spam"] = msg.text.replace("Spam change:","")
                kr.sendText(msg.to,"spam changed")

            elif "Spam add:" in msg.text:
                if msg.toType == 2:
                 wait["spam"] = msg.text.replace("Spam add:","")
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,"spam changed")
                else:
                    kr.sendText(msg.to,"Done")

            elif "Spam:" in msg.text:
                if msg.toType == 2:
                 strnum = msg.text.replace("Spam:","")
                num = int(strnum)
                for var in range(0,num):
                    kr.sendText(msg.to, wait["spam"])
#=====================================
            elif "Spam " in msg.text:
                if msg.toType == 2:
                  bctxt = msg.text.replace("Spam ", "")
                  t = kr.getAllContactIds()
                  t = 500
                  while(t):
                    kr.sendText(msg.to, (bctxt))
                    t-=1
#==============================================
            elif "Spamcontact @" in msg.text:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = kr.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam") 
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam") 
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam") 
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam") 
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam") 
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(g.mid,"Spam")
                       kr.sendText(msg.to, "Done")
                       print " Spammed !"

#==============================================================================#
            elif msg.text in ["Invite"]:
                wait["invite"] = True
                kr.sendText(msg.to,"Send Contact")
            
            elif msg.text in ["Steal contact"]:
                wait["contact"] = True
                kr.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                print "[Command]Like executed"
                kr.sendText(msg.to,"Like Status Owner")
                try:
                  likeme()
                except:
                  pass
                
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                kr.sendText(msg.to,"Like Status Teman")
                try:
                  likefriend()
                except:
                  pass
            
            elif msg.text in ["Like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Already")
                        
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                kr.sendText(msg.to,"Simi mode On")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                kr.sendText(msg.to,"Simi mode Off")
                
            elif msg.text in ["Autoread on","Read:on"]:
                wait['alwayRead'] = True
                kr.sendText(msg.to,"Auto read On")
                
            elif msg.text in ["Autoread off","Read:off"]:
                wait['alwayRead'] = False
                kr.sendText(msg.to,"Auto read Off")
                
            elif msg.text in ["Respontag on","Autorespon:on","Respon on","Respon:on"]:
                wait["detectMention"] = True
                kr.sendText(msg.to,"Auto respon tag On")
                
            elif msg.text in ["Respontag off","Autorespon:off","Respon off","Respon:off"]:
                wait["detectMention"] = False
                kr.sendText(msg.to,"Auto respon tag Off")
            
            elif msg.text in ["Kicktag on","Autokick:on","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                kr.sendText(msg.to,"Auto Kick tag ON")
                
            elif msg.text in ["Kicktag off","Autokick:off","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                kr.sendText(msg.to,"Auto Kick tag OFF")
            elif "Time" in msg.text:
              if msg.toType == 2:
                  kr.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
#==============================================================================#
            elif msg.text in ["Sambut on","sambut on"]:
                if wait["Wc"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"noтιғ yg joιn on")
                else:
                    wait["Wc"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already on")
            elif msg.text in ["Sambut off","sambut off"]:
                if wait["Wc"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"noтιғ yg joιn oғғ")
                else:
                    wait["Wc"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already oғғ")
#==============================================================================#
            elif msg.text in ["Pergi on","pergi on"]:
                if wait["Lv"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"noтιғ yg leave on")
                else:
                    wait["Lv"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already on")
            elif msg.text in ["Pergi off","pergi off"]:
                if wait["Lv"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"noтιғ yg leave oғғ")
                else:
                    wait["Lv"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already oғғ")
#==============================================================================#
            elif "Cleanse" in msg.text:
				if msg.toType == 2:
					if msg.toType == 2:
						print "ok"
						_name = msg.text.replace("Cleanse","")
						gs = kr.getGroup(msg.to)
						gs = kr.getGroup(msg.to)
						gs = kr.getGroup(msg.to)
						kr.sendText(msg.to,"Just some casual cleansing ô")
						kr.sendText(msg.to,"Group cleansed.")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
						if targets == []:
							kr.sendText(msg.to,"Not found.")
							kr.sendText(msg.to,"Not found.")
						else:
							for target in targets:
								try:
									klist=[kr,kr,kr]
									kicker=random.choice(klist)
									kicker.kickoutFromGroup(msg.to,[target])
									print (msg.to,[g.mid])
								except:
									kr.sendText(msg.to,"Group cleanse")
									kr.sendText(msg.to,"Group cleanse")
            elif msg.text in ["Salam1"]:
                kr.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                kr.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif "Salam3" in msg.text:
              if msg.from_ in owner:
                kr.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr.sendText(msg.to,"Assalamu'alaikum")
                kr.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                kr.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Salam3","")
                    gs = kr.getGroup(msg.to)
                    kr.sendText(msg.to,"maaf kalo gak sopan")
                    kr.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
                    kr.sendText(msg.to,"hehehhehe")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in admin:
                            try:
                                klist=[kr]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                kr.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                kr.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                kr.sendText(msg.to,"Nah salamnya jawab sendiri dah")
            elif ("Kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           kr.kickoutFromGroup(msg.to,[target])
                       except:
                           kr.sendText(msg.to,"Error")
            
            elif ("Cium " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           kr.kickoutFromGroup(msg.to,[target])
                           kr.inviteIntoGroup(msg.to,[target])
                           kr.cancelGroupInvitation(msg.to,[target])
                       except:
                           kr.sendText(msg.to,"Error")
            
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
                kr.kickoutFromGroup(msg.to,[midd])
            
            elif 'invite ' in msg.text.lower():
                    key = msg.text[-33:]
                    kr.findAndAddContactsByMid(key)
                    kr.inviteIntoGroup(msg.to, [key])
                    contact = kr.getContact(key)
            
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = kr.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        kr.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Tidak ada undangan")
                        else:
                            kr.sendText(msg.to,"Invitan tidak ada")
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Tidak ada undangan")
                    else:
                        kr.sendText(msg.to,"Invitan tidak ada")
            
            elif msg.text.lower() == 'link on':
                if msg.toType == 2:
                    group = kr.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    kr.updateGroup(group)
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"URL open")
                    else:
                        kr.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"It can not be used outside the group")
                    else:
                        kr.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text.lower() == 'link off':
                if msg.toType == 2:
                    group = kr.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    kr.updateGroup(group)
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"URL close")
                    else:
                        kr.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"It can not be used outside the group")
                    else:
                        kr.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text in ["Url","Gurl"]:
                if msg.toType == 2:
                    g = kr.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        kr.updateGroup(g)
                    gurl = kr.reissueGroupTicket(msg.to)
                    kr.sendText(msg.to,"line://ti/g/" + gurl)
                    
            elif "Gcreator" == msg.text:
                try:
                    group = kr.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    kr.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    kr.sendMessage(M)
                    kr.sendText(msg.to,"Creator Grup")
            
            elif msg.text.lower() == 'invite:gcreator':
                if msg.toType == 2:
                       ginfo = kr.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           kr.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           kr.inviteIntoGroup(msg.to,[gcmid])
            
            elif ("Gname: " in msg.text):
                if msg.toType == 2:
                    X = kr.getGroup(msg.to)
                    X.name = msg.text.replace("Gname: ","")
                    kr.updateGroup(X)
            
            elif msg.text.lower() == 'infogrup':        
                    group = kr.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    kr.sendText(msg.to,md)
            
            elif msg.text.lower() == 'grup id':
                gid = kr.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (kr.getGroup(i).name,i)
                kr.sendText(msg.to,h)
#==============================================================================#
            elif msg.text in ["Glist"]:
                gid = kr.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s\n" % (kr.getGroup(i).name +" ? ["+str(len(kr.getGroup(i).members))+"]")
                kr.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
            
            elif msg.text.lower() == 'gcancel':
                gid = kr.getGroupIdsInvited()
                for i in gid:
                    kr.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    kr.sendText(msg.to,"He declined all invitations")
                         
            elif "Auto add" in msg.text:
                thisgroup = kr.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                kr.findAndAddContactsByMids(mi_d)
                kr.sendText(msg.to,"Success Add all")
                    
            elif "@bye" in msg.text:
                if msg.toType == 2:
                    ginfo = kr.getGroup(msg.to)
                    try:
                        kr.leaveGroup(msg.to)
                    except:
                        pass
#==============================================================================#
            elif "nah" == msg.text.lower():
                 group = kr.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 kr.sendMessage(cnt)

            elif "cctv on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         kr.sendText(msg.to,"Setpoint already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     kr.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "cctv off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    kr.sendText(msg.to,"Setpoint already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    kr.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif msg.text in ["toong","Toong"]:
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
                        kr.sendText(msg.to, "╔═════════════ \n╠❂➣Sider :\n╠═════════════                     %s\n╠\n╠═════════════\n╠❂➣Reader :\n╠═════════════ %s\n╠\n╠═════════════\n╠In the last seen point:\n╠[%s]\n╚═════════════" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
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
                        print "toong ready"
                        kr.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
                    else:
                        kr.sendText(msg.to, "Ketik [Cctv on] dulu, baru ketik [Toong]")


                    
            elif "intip" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             kr.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = kr.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          kr.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        kr.sendText(msg.to, "Lurking has not been set.")
            elif "Gbroadcast: " in msg.text:
                bc = msg.text.replace("Gbroadcast: ","")
                gid = kr.getGroupIdsJoined()
                for i in gid:
                    kr.sendText(i, bc)
                    
            elif "Cbroadcast: " in msg.text:
                bc = msg.text.replace("Cbroadcast: ","")
                gid = kr.getAllContactIds()
                for i in gid:
                    kr.sendText(i, bc)
            
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                kr.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,"spam changed")
                else:
                    kr.sendText(msg.to,"Done")
    
            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    kr.sendText(msg.to, wait["spam"])
            
            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = kr.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                    else:
                        pass
            
            elif "Spam" in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           kr.sendText(msg.to, teks)
                    else:
                       kr.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        kr.sendText(msg.to, tulisan)
                    else:
                        kr.sendText(msg.to, "Out Of Range!")
                        
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        kr.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        kr.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        kr.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        kr.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            kr.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+kr.getContact(mi_d).displayName + "\n"
                            kr.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                kr.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                kr.sendText(msg.to,"Mimic change to target")
                            else:
                                kr.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        kr.sendText(msg.to,"Reply Message on")
                    else:
                        kr.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        kr.sendText(msg.to,"Reply Message off")
                    else:
                        kr.sendText(msg.to,"Sudah off")
            elif "Setimage: " in msg.text:
                wait["pap"] = msg.text.replace("Setimage: ","")
                kr.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                kr.sendImageWithURL(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                kr.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                kr.sendVideoWithURL(msg.to,wait["pap"])
            elif "TL:" in msg.text:
              if msg.toType == 2:
                tl_text = msg.text.replace("TL:","")
                kr.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+kr.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#==============================================================================#
            elif msg.text.lower() == 'mymid':
                kr.sendText(msg.to,mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                kr.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+kr.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = kr.getProfile()
                    profile.displayName = string
                    kr.updateProfile(profile)
                    kr.sendText(msg.to,"Changed " + string + "")
            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = kr.getProfile()
                    profile.statusMessage = string
                    kr.updateProfile(profile)
                    kr.sendText(msg.to,"Changed " + string)
            elif msg.text in ["Myname"]:
                    h = kr.getContact(mid)
                    kr.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = kr.getContact(mid)
                    kr.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = kr.getContact(mid)
                    kr.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = kr.getContact(mid)
                    kr.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = kr.getContact(mid)
                    kr.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = kr.getContact(mid)
                    cu = kr.channel.getCover(mid)          
                    path = str(cu)
                    kr.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = kr.getContact(mid)
                    cu = kr.channel.getCover(mid)          
                    path = str(cu)
                    kr.sendText(msg.to, path)
            elif "Getmid @" in msg.text:
                _name = msg.text.replace("Getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = kr.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        kr.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = kr.getContact(key1)
                cu = kr.channel.getCover(key1)
                try:
                    kr.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    kr.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = kr.getContact(key1)
                cu = kr.channel.getCover(key1)
                try:
                    kr.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    kr.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = kr.getContact(key1)
                cu = kr.channel.getCover(key1)
                try:
                    kr.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    kr.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = kr.getContact(key1)
                cu = kr.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    kr.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    kr.sendText(msg.to,"Profile Picture " + contact.displayName)
                    kr.sendImageWithURL(msg.to,image)
                    kr.sendText(msg.to,"Cover " + contact.displayName)
                    kr.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = kr.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                kr.sendMessage(msg)
            elif "Getpict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getpict @","")
                _nametarget = _name.rstrip('  ')
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    kr.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kr.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            kr.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    kr.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kr.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            kr.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip('  ')
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    kr.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kr.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            kr.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    kr.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kr.getContact(target)
                            cu = kr.channel.getCover(target)          
                            path = str(cu)
                            kr.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "Coverurl @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Coverurl @","")    
                _nametarget = _name.rstrip('  ')
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    kr.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kr.getContact(target)
                            cu = kr.channel.getCover(target)          
                            path = str(cu)
                            kr.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "Getgrup image" in msg.text:
                group = kr.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                kr.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                group = kr.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                kr.sendText(msg.to,path)
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kr.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kr.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kr.CloneContactProfile(target)
                               kr.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in ["Mybackup","mybackup"]:
                try:
                    kr.updateDisplayPicture(backup.pictureStatus)
                    kr.updateProfile(backup)
                    kr.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    kr.sendText(msg.to, str(e))
#==============================================================================#
            elif "Fancytext: " in msg.text:
                txt = msg.text.replace("Fancytext: ", "")
                kr.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
                    
            elif "Translate-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                kr.sendText(msg.to, A)
            elif "Translate-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                kr.sendText(msg.to, A)
            elif "Translate-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                kr.sendText(msg.to, A)
            elif "Translate-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                kr.sendText(msg.to, A)
            elif "Translate-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                kr.sendText(msg.to, A)
            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO ENGLISH**\n" + "" + result + "\n**SUKSES**")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr.sendText(msg.to,"**FROM EN**\n" + "" + kata + "\n**TO ID**\n" + "" + result + "\n**SUKSES**")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO JP**\n" + "" + result + "\n**SUKSES**")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                kr.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
                
            elif msg.text.lower() == 'welcome':
                ginfo = kr.getGroup(msg.to)
                kr.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                kr.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                kr.sendAudio(msg.to,'tts.mp3')
            
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr.sendAudio(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                  tanya = msg.text.replace("Kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  kr.sendAudio(msg.to,'tts.mp3')
                  
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  kr.sendAudio(msg.to,'tts.mp3')
            
            elif 'Youtubemp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubemp4 ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        kr.sendVideoWithURL(msg.to, ght)
                    except:
                        kr.sendText(msg.to, "Could not find it")
            
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        kr.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
            elif "Lirik " in msg.text:
                try:
                    songname = msg.text.lower().replace("Lirik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        kr.sendText(msg.to, hasil)
                except Exception as wak:
                        kr.sendText(msg.to, str(wak))
                        
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      kr.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              kr.sendText(msg.to, pesan)
                          except Exception as e:
                              kr.sendText(msg.to, str(e))
                              
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        kr.sendText(msg.to, hasil)
                        kr.sendText(msg.to, "Please Wait for audio...")
                        kr.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        kr.sendText(msg.to, str(njer))
            
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    kr.sendImageWithURL(msg.to,path)
                except:
                    pass           
            
            elif "Profileig " in msg.text:
                    try:
                        instagram = msg.text.replace("Profileig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        kr.sendImageWithURL(msg.to, profileIG)
                        kr.sendText(msg.to, str(text))
                    except Exception as e:
                        kr.sendText(msg.to, str(e))

            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                kr.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text in ["Kalender","Time","Waktu"]:
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
                kr.sendText(msg.to, rst)
#==============================================================================#
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    kr.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    kr.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    kr.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    kr.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                    
            elif "Restart" in msg.text:
                    print "[Command]Restart"
                    try:
                        kr.sendText(msg.to,"Restarting...")
                        kr.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        kr.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
                    
            elif "Turn off" in msg.text:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
                
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot has been active "+waktu(eltime)
                kr.sendText(msg.to,van)

        
#================================ KRIS SCRIPT STARTED ==============================================#
            elif "google " in msg.text:
                    a = msg.text.replace("google ","")
                    b = urllib.quote(a)
                    kr.sendText(msg.to,"Sedang Mencari om...")
                    kr.sendText(msg.to, "https://www.google.com/" + b)
                    kr.sendText(msg.to,"Ketemu om ^")

            elif cms(msg.text,["/creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ub14f769cdf42d8c8a618ebe91ac2c8c7"}
                kr.sendMessage(msg)

            elif "friendpp: " in msg.text:
              if msg.from_ in admin:
                suf = msg.text.replace('friendpp: ','')
                gid = kr.getAllContactIds()
                for i in gid:
                    h = kr.getContact(i).displayName
                    gna = kr.getContact(i)
                    if h == suf:
                        kr.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)

            elif "Checkmid: " in msg.text:
                saya = msg.text.replace("Checkmid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":saya}
                kr.sendMessage(msg)
                contact = kr.getContact(saya)
                cu = kr.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    kr.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    kr.sendText(msg.to,"Profile Picture " + contact.displayName)
                    kr.sendImageWithURL(msg.to,image)
                    kr.sendText(msg.to,"Cover " + contact.displayName)
                    kr.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif "Checkid: " in msg.text:
                saya = msg.text.replace("Checkid: ","")
                gid = kr.getGroupIdsJoined()
                for i in gid:
                    h = kr.getGroup(i).id
                    group = kr.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            kr.sendText(msg.to,md)
                            kr.sendMessage(msg)
                            kr.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["Friendlist"]:    
                contactlist = kr.getAllContactIds()
                kontak = kr.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                kr.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = kr.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                kr.sendText(msg.to, msgs)
                
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = kr.getAllContactIds()
                for i in gid:
                    h = kr.getContact(i).displayName
                    contact = kr.getContact(i)
                    cu = kr.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        kr.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        kr.sendText(msg.to,"Profile Picture " + contact.displayName)
                        kr.sendImageWithURL(msg.to,image)
                        kr.sendText(msg.to,"Cover " + contact.displayName)
                        kr.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
                saya = msg.text.replace('Friendpict: ','')
                gid = kr.getAllContactIds()
                for i in gid:
                    h = kr.getContact(i).displayName
                    gna = kr.getContact(i)
                    if h == saya:
                        kr.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Friendlistmid"]: 
                gruplist = kr.getAllContactIds()
                kontak = kr.getContacts(gruplist)
                num=1
                msgs="═════════ʆίςϯ ƒɾίεηδʍίδ═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═════════ʆίςϯ ƒɾίεηδʍίδ═════════\n\nTotal Friend : %i" % len(kontak)
                kr.sendText(msg.to, msgs)
            
            elif msg.text in ["Blocklist"]: 
                blockedlist = kr.getBlockedContactIds()
                kontak = kr.getContacts(blockedlist)
                num=1
                msgs="═════════List Blocked═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                kr.sendText(msg.to, msgs)
                
            elif msg.text in ["Gruplist"]:  
                gruplist = kr.getGroupIdsJoined()
                kontak = kr.getGroups(gruplist)
                num=1
                msgs="═════════List Grup═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                kr.sendText(msg.to, msgs)
            
            elif msg.text in ["Gruplistmid"]:   
                gruplist = kr.getGroupIdsJoined()
                kontak = kr.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                kr.sendText(msg.to, msgs)
                    
            elif "Grupimage: " in msg.text:
                saya = msg.text.replace('Grupimage: ','')
                gid = kr.getGroupIdsJoined()
                for i in gid:
                    h = kr.getGroup(i).name
                    gna = kr.getGroup(i)
                    if h == saya:
                        kr.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif "Grupname" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = kr.getGroup(msg.to)
                kr.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Grupid" in msg.text:
                saya = msg.text.replace('Grupid','')
                gid = kr.getGroup(msg.to)
                kr.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
                    
            elif "Grupinfo: " in msg.text:
                saya = msg.text.replace('Grupinfo: ','')
                gid = kr.getGroupIdsJoined()
                for i in gid:
                    h = kr.getGroup(i).name
                    group = kr.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            kr.sendText(msg.to,md)
                            kr.sendMessage(msg)
                            kr.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"

            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = kr.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        kr.sendMessage(msg)
                        print "Spamtag Berhasil."

            elif "crashkontak @" in msg.text:
                _name = msg.text.replace("crashkontak @","")
                _nametarget = _name.rstrip(' ')
                gs = kr.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                            kr.sendMessage(g.mid,msg.to + str(msg))
                            kr.sendText(g.mid, "hai")
                            kr.sendText(g.mid, "salken")
                            kr.sendText(msg.to, "Done")
                            print " Spammed crash !"

            elif "playstore " in msg.text.lower():
                    tob = msg.text.lower().replace("playstore ","")
                    kr.sendText(msg.to,"Sedang Mencari boss...")
                    kr.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    kr.sendText(msg.to,"Ketemu boss ^")
                    
            elif 'wikipedia ' in msg.text.lower():
                try:
                    wiki = msg.text.lower().replace("wikipedia ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=3)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    kr.sendText(msg.to, pesan)
                except:
                        try:
                            pesan="Teks nya kepanjangan! ketik link dibawah aja\n"
                            pesan+=wikipedia.page(wiki).url
                            kr.sendText(msg.to, pesan)
                        except Exception as e:
                            kr.sendText(msg.to, str(e))    
                            
            elif "say " in msg.text.lower():
                say = msg.text.lower().replace("say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr.sendAudio(msg.to,"hasil.mp3")
                
            elif msg.text in ["spam gift 25"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg) 
                kr.sendMessage(msg)
                kr.sendMessage(msg) 
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg) 
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)    
                
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = kr.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       kr.findAndAddContactsByMid(gCreator)
                       kr.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass

            elif msg.text in ["Gcreator:kick"]:
	           if msg.from_ in admin:
                    ginfo = kr.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       kr.findAndAddContactsByMid(gCreator)
                       kr.kickoutFromGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
                   
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
                        kr.sendText(msg.to, hasil)
                except Exception as wak:
                        kr.sendText(msg.to, str(wak))       
                   
            elif "Getcover @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Getcover @","")
                _nametarget = _name.rstrip('  ')
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kr.getContact(target)
                            cu = kr.channel.getCover(target)
                            path = str(cu)
                            kr.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
                
            elif "idline: " in msg.text:
                msgg = msg.text.replace('idline: ','')
                conn = kr.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    kr.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    kr.sendMessage(msg)
                        
            elif "reinvite" in msg.text.split():
                if msg.toType == 2:
                    group = kr.getGroup(msg.to)
                    if group.invitee is not None:
                        try:
                            grCans = [contact.mid for contact in group.invitee]
                            kr.findAndAddContactByMid(msg.to, grCans)
                            kr.cancelGroupInvitation(msg.to, grCans)
                            kr.inviteIntoGroup(msg.to, grCans)
                        except Exception as error:
                            print error
                    else:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"No Invited")
                        else:
                            kr.sendText(msg.to,"Error")
                else:
                    pass
                
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                kr.sendText(msg.to,van)
                
            elif msg.text in ["Restart"]:
                kr.sendText(msg.to, "Bot has been restarted")
                restart_program()
                print "@Restart"
                
            elif msg.text in ["time"]:
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
                client.sendText(msg.to, rst)
                
            elif "image " in msg.text:
                search = msg.text.replace("image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    kr.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif 'instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("instagram ","")
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
                    detail = "**INSTAGRAM INFO USER**\n"
                    details = "\n**INSTAGRAM INFO USER**"
                    kr.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    kr.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	kr.sendText(msg.to, str(njer))    
                	
            elif msg.text in ["Attack"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                kr.sendMessage(msg)
                
            elif msg.text.lower() == '...':
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                kr.sendMessage(msg)    
#=================================KRIS SCRIPT FINISHED =============================================#
            
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip()
                    gs = kr.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                kr.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                            except:
                                kr.sendText(msg.to,"Error")
                                
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = kr.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                kr.sendText(msg.to,_nametarget + " Delete From Blacklist")
                            except:
                                kr.sendText(msg.to,_nametarget + " Not In Blacklist")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kr.getGroup(msg.to)
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
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kr.sendText(msg.to,_name + " Succes Add to Blacklist")
                                except:
                                    kr.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = kr.getGroup(msg.to)
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
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kr.sendText(msg.to,_name + " Delete From Blacklist")
                                except:
                                    kr.sendText(msg.to,_name + " Not In Blacklist")
            elif msg.text in ["Clear"]:
                wait["blacklist"] = {}
                kr.sendText(msg.to,"Blacklist Telah Dibersihkan")
            elif msg.text in ["Ban:on"]:
                wait["wblacklist"] = True
                kr.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban:on"]:
                wait["dblacklist"] = True
                kr.sendText(msg.to,"Send Contact")
            elif msg.text in ["Banlist"]:   
                if wait["blacklist"] == {}:
                    kr.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    kr.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="*Blacklist*"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, kr.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n*Blacklist*\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    kr.sendText(msg.to, msgs)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    kr.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    kr.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = kr.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        kr.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
                if msg.toType == 2:
                    group = kr.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    num=1
                    cocoa = "══════════List Blacklist═════════"
                    for mm in matched_list:
                        cocoa+="\n[%i] %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                    kr.sendText(msg.to,cocoa)
            elif msg.text.lower() == 'scan blacklist':
                if msg.toType == 2:
                    group = kr.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kr.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            kr.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass       
#==============================================#
        if op.type == 17:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            if wait["protect"] == True:
                if wait["blacklist"][op.param2] == True:
                    try:
                        kr.kickoutFromGroup(op.param1,[op.param2])
                        G = kr.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        kr.updateGroup(G)
                    except:
                        try:
                            kr.kickoutFromGroup(op.param1,[op.param2])
                            G = kr.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            kr.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    kr.kickoutFromGroup(op.param1,[op.param2])
                    kr.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    kr.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in Bots:
                            pass
                        elif wait["inviteprotect"] == True:
                            wait ["blacklist"][op.param2] = True
                            kr.cancelGroupInvitation(op.param1,[op.param3])
                            if op.param2 not in Bots:
                                if op.param2 in Bots:
                                    pass
                                elif wait["cancelprotect"] == True:
                                    wait ["blacklist"][op.param2] = True
                                    kr.cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = kr.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr.updateGroup(G)
                    kr.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    kr.sendText(op.param1,str(wait["message"]))
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = kr.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr.kickoutFromGroup(op.param1,[op.param3])
                    kr.updateGroup(G)
        if op.type == 17:
           if wait["Wc"] == True:
               if op.param2 in Bots:
                 return
               ginfo = kr.getGroup(op.param1)
               kr.sendText(op.param1, "╔═════════════\n║Selamat Datang Di  " + str(ginfo.name) + "\n╠═════════════\n" + "║Founder =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Semoga Betah Kak 😘 \n╚═════════════")
               print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                kr.sendText(op.param1, "╔═════════════\n║Baper Tuh Orang :v \n║Semoga Bahagia ya 😊 \n╚═════════════")
                print "MEMBER HAS LEFT THE GROUP"
#------------------------------------------------------------------------------#
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error

def autolike():
    count = 1
    while True:
        try:
           for posts in kr.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   kr.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          kr.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,20):
      hasil = kr.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          kr.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kr.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««")
          print "Like"
        except:
          pass
      else:
          print "Already Liked Om"
time.sleep(0.60)

def likeme():
    for zx in range(0,20):
        hasil = kr.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    kr.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kr.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Om"


while True:
    try:
        Ops = kr.fetchOps(kr.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(kr.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            kr.Poll.rev = max(kr.Poll.rev, Op.revision)
            bot(Op)

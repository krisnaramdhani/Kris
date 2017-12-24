# -*- coding: utf-8 -*-

import KRIS
from KRIS.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,ast,os,subprocess,requests

kr = KRIS.LINE()
#kr.login(qr=True)
kr.login(token='')
kr.loginResult()
print "===[Login Success]==="


helpMessage ="""
====={List Keyword]=====
► Help
► Creator
► Gcreator
► List group:
► Leave group:
► Cancel
► Url:on/off
► Autojoin:on/off
► Autocancel:on/off
► Qr:on/off
► Autokick:on/off
► Contact:on/off
► Gift (1,2,3)
► Tagall
► Setview
► Viewseen
► Boom
► Add all
► Recover
► Remove all chat
► Gn: (name)
► Kick: (mid)
► Invite: (mid)
► Welcome
► Bc: (text)
► Cancelall
► Gurl
► Self Like
► Speed
► Ban
► Unban
► Copy @
► Backup me
► Ban @
► Unban @
► Banlist
► Kill ban
"""

mid = kr.getProfile().mid
Creator=""
admin=[""]

contact = kr.getProfile()
profile = kr.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

wait = {
    "LeaveRoom":True,
    "AutoJoin":True,
    "Members":0,
    "AutoCancel":False,
    "AutoKick":False,       
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":True,
    "Timeline":True,
    "Contact":True,
    "lang":"JP",
    "BlGroup":{}
}


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
#--------------------END_OF_OPERATION--------------------
        if op.type == 0:
            return
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
            kr.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
            kr.leaveRoom(op.param1)

#--------------NOTIFIED_INVITE_INTO_GROUP----------------

	    if mid in op.param3:
                if wait["AutoJoin"] == True:
                    kr.acceptGroupInvitation(op.param1)
                else:
		    kr.rejectGroupInvitation(op.param1)
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in admin:
			pass
		    else:
                        kr.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			kr.cancelGroupInvitation(op.param1, [op.param3])
			kr.sendText(op.param1, "Itu kicker jgn di invite!")
		    else:
			pass
#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
		if wait["AutoKick"] == True:
                    if op.param2 in admin:
                        pass
                    try:
                        kr.kickoutFromGroup(op.param1,[op.param2])
			kr.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
			    kr.kickoutFromGroup(op.param1,[op.param2])
			    kr.inviteIntoGroup(op.param1,[op.param3])
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



#--------------------------NOTIFIED_UPDATE_GROUP---------------------
        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in admin:
		    pass
		else:
                    kr.sendText(msg.to, "Jangan mainan QR ntr ada kicker")
            else:
                pass
#--------------------------SEND_MESSAGE---------------------------
        if op.type == 25:
            msg = op.message
#----------------------------------------------------------------------------
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            kr.sendText(msg.to,"already")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            kr.sendText(msg.to,"aded")
		    else:
			kr.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        kr.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        kr.sendText(msg.to,"It is not in the black list")
#--------------------------------------------------------
                elif wait["Contact"] == True:
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


#--------------------------------------------------------
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = kr.getGroup(msg.to)
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
                        kr.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        kr.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kr.sendText(msg.to,"Not for use less than group")

#--------------------------------------------------------
            elif msg.text is None:
                return
#--------------------------------------------------------
            elif msg.text in ["Creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Creator}
                kr.sendMessage(msg)
		kr.sendText(msg.to,"Itu Yang Bikin BOT")
#--------------------------------------------------------
	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = kr.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                kr.sendMessage(msg)
		kr.sendText(msg.to,"Itu Yang Buat Grup Ini")
#--------------------------------------------------------
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    kr.sendText(msg.to,msg.text)
#--------------------------------------------------------
            elif msg.text in ["Key","help","Help"]:
                kr.sendText(msg.to,helpMessage)
#--------------------------------------------------------
            elif msg.text in ["List group"]:
                gid = kr.getGroupIdsJoined()
                h = ""
		jml = 0
                for i in gid:
		    gn = kr.getGroup(i).name
                    h += "♦【%s】\n" % (gn)
		    jml += 1
                kr.sendText(msg.to,"======[List Group]======\n"+ h +"Total group: "+str(jml))
#--------------------------------------------------------
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = kr.getGroupIdsJoined()
                for i in gid:
                    h = kr.getGroup(i).name
		    if h == ng:
			kr.sendText(i,"Bye "+h+"~")
		        kr.leaveGroup(i)
			kr.sendText(msg.to,"Success left ["+ h +"] group")
		    else:
			pass
#--------------------------------------------------------
#--------------------------------------------------------
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = kr.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        kr.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        kr.sendText(msg.to,"No one is inviting")
                else:
                    kr.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Ourl","Url:on"]:
                if msg.toType == 2:
                    X = kr.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kr.updateGroup(X)
                    kr.sendText(msg.to,"Url Active")
                else:
                    kr.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Curl","Url:off"]:
                if msg.toType == 2:
                    X = kr.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kr.updateGroup(X)
                    kr.sendText(msg.to,"Url inActive")

                else:
                    kr.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Join on","Autojoin:on"]:
                wait["AutoJoin"] = True
                kr.sendText(msg.to,"AutoJoin Active")

            elif msg.text in ["Join off","Autojoin:off"]:
                wait["AutoJoin"] = False
                kr.sendText(msg.to,"AutoJoin inActive")

#--------------------------------------------------------
	    elif msg.text in ["Autocancel:on"]:
                wait["AutoCancel"] = True
                kr.sendText(msg.to,"The group of people and below decided to automatically refuse invitation")
		print wait["AutoCancel"][msg.to]

	    elif msg.text in ["Autocancel:off"]:
                wait["AutoCancel"] = False
                kr.sendText(msg.to,"Invitation refused turned off")
		print wait["AutoCancel"][msg.to]
#--------------------------------------------------------
	    elif "Qr:on" in msg.text:
	        wait["Qr"] = True
	    	kr.sendText(msg.to,"QR Protect Active")

	    elif "Qr:off" in msg.text:
	    	wait["Qr"] = False
	    	kr.sendText(msg.to,"Qr Protect inActive")
#--------------------------------------------------------
	    elif "Autokick:on" in msg.text:
		wait["AutoKick"] = True
		kr.sendText(msg.to,"AutoKick Active")

	    elif "Autokick:off" in msg.text:
		wait["AutoKick"] = False
		kr.sendText(msg.to,"AutoKick inActive")
#--------------------------------------------------------
            elif msg.text in ["K on","Contact:on"]:
                wait["Contact"] = True
                kr.sendText(msg.to,"Contact Active")

            elif msg.text in ["K off","Contact:off"]:
                wait["Contact"] = False
                kr.sendText(msg.to,"Contact inActive")
#--------------------------------------------------------
            elif msg.text in ["Status"]:
                md = ""
		if wait["AutoJoin"] == True: md+="✦ Auto join : on\n"
                else: md +="✦ Auto join : off\n"
		if wait["Contact"] == True: md+="✦ Info Contact : on\n"
		else: md+="✦ Info Contact : off\n"
                if wait["AutoCancel"] == True:md+="✦ Auto cancel : on\n"
                else: md+= "✦ Auto cancel : off\n"
		if wait["Qr"] == True: md+="✦ Qr Protect : on\n"
		else:md+="✦ Qr Protect : off\n"
		if wait["AutoKick"] == True: md+="✦ Autokick : on\n"
		else:md+="✦ Autokick : off"
                kr.sendText(msg.to,"=====[Status]=====\n"+md)
#--------------------------------------------------------
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                kr.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                kr.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                kr.sendMessage(msg)

            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kr.sendMessage(msg)

#--------------------------------------------------------
	    elif "Tagall" == msg.text:
		group = kr.getGroup(msg.to)
		mem = [contact.mid for contact in group.members]
		for mm in mem:
		    xname = kr.getContact(mm).displayName
		    xlen = str(len(xname)+1)
		    msg.contentType = 0
		    msg.text = "@"+xname+" "
		    msg.contentMetadata = {'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
		    try:
		        kr.sendMessage(msg)
		    except Exception as e:
			print str(e)

#--------------------------CEK SIDER------------------------------

            elif "Setview" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                kr.sendText(msg.to, "Checkpoint checked!")
                print "@setview"

            elif "Viewseen" in msg.text:
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
                    contactId = kr.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "List Viewer\n*"
                        grp = '\n* '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        kr.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        kr.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"
#--------------------------------------------------------

#KICK_BY_TAG
	    elif "Boom " in msg.text:
		if 'MENTION' in msg.contentMetadata.keys()!= None:
		    names = re.findall(r'@(\w+)', msg.text)
		    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		    mentionees = mention['MENTIONEES']
		    print mentionees
		    for mention in mentionees:
			kr.kickoutFromGroup(msg.to,[mention['M']])

#--------------------------------------------------------
	    elif "Add all" in msg.text:
		thisgroup = kr.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		kr.findAndAddContactsByMids(mi_d)
		kr.sendText(msg.to,"Success Add all")
#--------------------------------------------------------
	    elif "Recover" in msg.text:
		thisgroup = kr.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		kr.createGroup("Recover", mi_d)
		kr.sendText(msg.to,"Success recover")
#--------------------------------------------------------
	    elif msg.text in ["Remove all chat"]:
		kr.removeAllMessages(op.param2)
		kr.sendText(msg.to,"Removed all chat")
#--------------------------------------------------------
            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = kr.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    kr.updateGroup(X)
                else:
                    kr.sendText(msg.to,"It can't be used besides the group.")
#--------------------------------------------------------
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    kr.kickoutFromGroup(msg.to,[midd])
		else:
		    kr.sendText(msg.to,"Admin Detected")
#--------------------------------------------------------
            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                kr.findAndAddContactsByMid(midd)
                kr.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------------
            elif msg.text in ["#welcome","Welcome","welcome","Welkam","welkam"]:
                gs = kr.getGroup(msg.to)
                kr.sendText(msg.to,"Selamat datang di "+ gs.name)
#--------------------------------------------------------
	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = kr.getGroupIdsJoined()
		for i in gid:
		    kr.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~@xpk5386g")
		kr.sendText(msg.to,"Success BC BosQ")
#--------------------------------------------------------
            elif msg.text in ["Cancelall"]:
                gid = kr.getGroupIdsInvited()
                for i in gid:
                    kr.rejectGroupInvitation(i)
                kr.sendText(msg.to,"All invitations have been refused")
#--------------------------------------------------------
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = kr.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kr.updateGroup(x)
                    gurl = kr.reissueGroupTicket(msg.to)
                    kr.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Can't be used outside the group")
                    else:
                        kr.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------------
	    elif msg.text in ["Self Like"]:
		try:
		    print "activity"
		    url = kr.activity(limit=1)
		    print url
		    kr.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    kr.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Mau Bot Protect?\nFollow ig : @rid1bdbx\nLalu dm ke dia")
		    kr.sendText(msg.to, "Success~")
		except Exception as E:
		    try:
			kr.sendText(msg.to,str(E))
		    except:
			pass

#--------------------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
		print("Speed")
                elapsed_time = time.time() - start
		kr.sendText(msg.to, "Progress...")
                kr.sendText(msg.to, "%sseconds" % (elapsed_time))

#--------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                kr.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                kr.sendText(msg.to,"send contact")
#--------------------------------------------------------
	    elif "Backup me" in msg.text:
		try:
		    kr.updateDisplayPicture(profile.pictureStatus)
		    kr.updateProfile(profile)
		    kr.sendText(msg.to, "Success backup profile")
		except Exception as e:
		    kr.sendText(msg.to, str(e))
#--------------------------------------------------------
	    elif "Copy " in msg.text:
                copy0 = msg.text.replace("Copy ","")
                copy1 = copy0.lstrip()
                copy2 = copy1.replace("@","")
                copy3 = copy2.rstrip()
                _name = copy3
		group = kr.getGroup(msg.to)
		for contact in group.members:
		    cname = kr.getContact(contact.mid).displayName
		    if cname == _name:
			kr.CloneContactProfile(contact.mid)
			kr.sendText(msg.to, "Success~")
		    else:
			pass
		
#--------------------------------------------------------
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kr.sendText(msg.to,"Succes BosQ")
                                except:
                                    kr.sendText(msg.to,"Error")
			    else:
				kr.sendText(msg.to,"Admin Detected~")
#--------------------------------------------------------
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    kr.sendText(msg.to,"nothing")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +kr.getContact(mi_d).displayName + "\n"
                    kr.sendText(msg.to,"===[Blacklist User]===\n"+mc)

#--------------------------------------------------------
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                kr.sendText(msg.to,"Succes BosQ")
                            except:
                                kr.sendText(msg.to,"Succes BosQ")
#--------------------------------------------------------
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = kr.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kr.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        kr.kickoutFromGroup(msg.to,[jj])
                    kr.sendText(msg.to,"Blacklist emang pantas tuk di usir")
#--------------------------------------------------------
#            elif "Cleanse" in msg.text:
#                if msg.toType == 2:
#                    print "Kick all member"
#                    _name = msg.text.replace("Cleanse","")
#                    gs = kr.getGroup(msg.to)
#                    kr.sendText(msg.to,"Dadaaah~")
#                    targets = []
#                    for g in gs.members:
#                        if _name in g.displayName:
#                            targets.append(g.mid)
#                    if targets == []:
#                        kr.sendText(msg.to,"Not found.")
#                    else:
#                        for target in targets:
#			     if target not in admin:
#                                try:
#                                    kr.kickoutFromGroup(msg.to,[target])
#                                    print (msg.to,[g.mid])
#                                except Exception as e:
#                                    kr.sendText(msg.to,str(e))
#			 kr.inviteIntoGroup(msg.to, targets)
#--------------------------------------------------------
#Restart_Program
	    elif msg.text in ["Bot:restart"]:
		kr.sendText(msg.to, "Bot has been restarted")
		restart_program()
		print "@Restart"
#--------------------------------------------------------



        if op.type == 59:
            print op


    except Exception as error:
        print error


#thread2 = threading.Thread(target=nameUpdate)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = kr.fetchOps(kr.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(kr.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            kr.Poll.rev = max(kr.Poll.rev, Op.revision)
            bot(Op)


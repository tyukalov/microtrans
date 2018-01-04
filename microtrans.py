#!/usr/bin/env python
# -*- coding: utf-8 -*-
 #    This program is free software: you can redistribute it and/or modify
 #    it under the terms of the GNU General Public License as published by
 #    the Free Software Foundation, either version 3 of the License, or
 #    (at your option) any later version.

 #    This program is distributed in the hope that it will be useful,
 #    but WITHOUT ANY WARRANTY; without even the implied warranty of
 #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #    GNU General Public License for more details.

 #    You should have received a copy of the GNU General Public License
 #    along with this program.  If not, see <http://www.gnu.org/licenses/>.

 # Igor Tyukalov <tyukalov@bk.ru>

import requests
import json
import urllib3
import sys
import gettext
import os
import locale

_ = gettext.gettext

VERSION = "0.01"
PROGNAME = "microtrans"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG_DIR = 'microtrans/lang/'
gettext.bindtextdomain(PROGNAME, os.path.join(BASE_DIR, LANG_DIR).replace('\\','/'))
gettext.textdomain(PROGNAME)
try:
    input = raw_input
except:
    pass


def resp (session, url, lang, key, text):
    req = {"lang":lang, "key":key, "text":text}
    r = session.post(url, req, verify=False)
    j = json.loads(r.text)
    if (j['code'] == 200):
        result = j['text'][0]
    else:
        print(j['message'])
        exit(1)
    return result

def help ():
    '''Displays help'''
    print(_("\tUsage: %s -lvhKkqd\n")%(sys.argv[0]))
    print(_("\tWhere:\n\
    \t -l - translation mode (en-ru, de-en...);\n\
\t -v - displays version information;\n\
\t -h - displays help;\n\
    \t -k - set a key (k=key);\n\
    \t -K - set key from file (K=filename);\n\
\t -d - dialog-mode;\n\
\t -q - hide more information;\n"))
    print(_("\tThis program uses the Yandex service API <http://translate.yandex.ru/>\n."))
    exit(0)

def version ():
    """Displays version information"""
    print("\t%s v%s\n"%(PROGNAME, VERSION) + _('\tLicense GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>\n\
\tWritten by Igor \'sp_r00t\' Tyukalov.\n'))
    print(_("\tThis program uses the Yandex service API <http://translate.yandex.ru/>\n."))
    exit(0)

if __name__ == '__main__':
    try:
        urllib3.disable_warnings()
    except:
        pass
    s=requests.Session()
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    lang = "en-ru"
    key = "trnsl.1.1.20171224T231837Z.30c64a84638e077a.7537958dc530367615df4fdaec5b971d9a7d014a"
    for k in sys.argv[1:]:
        if k[:2] == "-l":
            lang = k.split('=')[1]
        elif k[:2] == "-k":
            key = k.split('=')[1]
        elif k[:2] == "-K":
            try:
                filename = k.split('=')[1]
                with open(filename) as file:
                    key = file.readline()
            except:
                print(_("Error opening the '%s' file!")%(filename))
                exit(1)
    if "-d" in sys.argv:
        while True:
            inputstr = input()
            if inputstr == "exit":
                break
            print(resp(s, url, lang, key, inputstr).encode("utf8"))
    elif ("-v" in sys.argv) or ("--version" in sys.argv):
        version()
    elif ("-h" in sys.argv) or ("--help" in sys.argv):
        help()
    else:
        print(resp(s, url, lang, key, input()).encode("utf8"))
    if not("-q" in sys.argv):
        print(_("\nTranslated by the service Yandex.Translator"))
        print("<http://translate.yandex.ru/>\n")


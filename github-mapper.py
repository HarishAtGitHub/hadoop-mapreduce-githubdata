#!/usr/bin/env python2.7
"""Mapper to analyze PushEvent in Github"""
from __future__ import print_function
import json
import requests
from requests.auth import HTTPBasicAuth
from pygments.lexers import get_lexer_for_filename
import re
import sys

username = 'HarishAtGitHub'
password = 'onlygitisallowed'

for line in sys.stdin:
    line_stripped = line.strip()
    try :
        jsoncontent = json.loads(line_stripped, "ISO-8859-1")
        try :
            if (jsoncontent['type'] == 'PushEvent'):
                repo_url = jsoncontent['repo']['url']
                starter1 = 'https://api.github.dev/'
                if (repo_url.startswith(starter1)):
                    global username
                    global password
                    repo_path = repo_url[len(starter1):]
                    response = requests.get('https://api.github.com/' + repo_path + '/commits/' + jsoncontent['payload']['head'] ,auth=HTTPBasicAuth(username, password))
                    if (int(response.headers['x-ratelimit-remaining']) == 4) :
                        global username
                        global password
                        credentials = requests.get('http://master:5000/Credentials').json()
                        username = credentials['username']
                        password = credentials['password']
                    if (response.status_code == 200) :
                        files = response.json()['files']
                        for file in files:
                            try:
                                print('%s\t{"%s" : %d}' % (jsoncontent['actor']['login'],get_lexer_for_filename(file['filename']).name,file['additions'] ))
                            except ValueError:
                                pass

        except KeyError:
            pass
    except Exception as e:
        pass

    

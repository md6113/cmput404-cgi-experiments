#!/usr/bin/env python

import os, sys
from pprint import pprint
import json
import urlparse
from templates import login_page

import cgitb
cgitb.enable()

username = 'wha'
password = 'wakawaka'
#print "Hello, everyone out there!!"
#pprint(dict(os.environ))
#print os.environ['QUERY_STRING']
#print json.dumps((dict(os.environ)))

#params = urlparse.parse_qs(os.environ['QUERY_STRING'])
#print params
#user_agent = os.environ['HTTP_USER_AGENT']

#if 'Firefox' in user_agent:
#	print "Using firefox"
#elif 'Chrome' in user_agent:
#	print "Using Chrome"
#elif 'curl' in user_agent:
#	print "Using curl"
#else:
#	print "What R ya doin?"
content_length = os.getenv('CONTENT_LENGTH','')
cookie = os.getenv('HTTP_COOKIE', '')
#content_length = os.environ['CONTENT_LENGTH']
#cookie = os.environ['HTTP_COOKIE']
logged_in = False

if 'logged-in=True' in cookie:
    logged_in = True
elif content_length:
    bytes_to_read = int(content_length)
    content = sys.stdin.read(bytes_to_read)
    params = urlparse.parse_qs(content)
    
    if (params['username'][0] == username and params['password'][0] == password):
        print "Set-Cookie: logged-in=True"
        logged_in = True

# HTTP headers over
print "Content-Type: text/html"
print
if not logged_in:
    print r"""
            <h1> Welcome! </h1>
        
            <form method="POST" action="hello.py">
                <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
                <label> <span>Password:</span> <input type="password" name="password"></label>
        
                <button type="submit"> Login! </button>
            </form>
            """    
else:
    print "I am logged in!"
    

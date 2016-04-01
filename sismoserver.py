#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import json, requests, urllib2, urllib, tweepy
from flask import Flask, request
from StringIO import StringIO
from datetime import datetime, timedelta

def tweet(mensaje):
        CONSUMER_KEY = 'xxxxxxxxxxxxxxx' # cambiar
        CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxx'
        ACCESS_KEY = 'xxxxxxxxxxxxxxxx'
        ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxx'
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())
        tweetid = api.update_status(status=mensaje)





app = Flask(__name__)

@app.route("/",methods=['GET'])
def sismo():
	try:
		sismo = request.args.get("sismo")	
		if (str(sismo) == "1" ):
			t = datetime.now()
			hora = t.strftime("%-I:%M %p")
			tweet("[En Pruebas] Posible sismo en los próximos segundos cerca de Ipis de Goicoechea, S.J., Costa Rica ("+hora+")")
	except IOError as err:
                print 'Fallo'
                pass
        except Exception as e:
                print "Exception "+str(e)
                pass

        return "OK"


if __name__ == "__main__":
#    app.run()
	app.debug = True
	app.run(host="0.0.0.0", port=5002)


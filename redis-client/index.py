from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
import requests
import os
import redis
import json
import sys

app = Flask(__name__)
CORS(app,origins=["*"])

def redisCon():
   rhost = os.environ['REDIS_HOST']
   rauth = os.environ['REDIS_AUTH']
   return redis.StrictRedis(host=rhost,\
          port=6379,db=0,password=rauth,\
          decode_responses=True)

@app.route("/position/<cid>", methods=["POST"])
def setPosition(cid):
    r = redisCon()
    data = request.json
    key = f"client:{cid}:position"
    r.hset(key,"lat",data["lat"])
    r.hset(key,"lng",data["lng"])
    r.expire(key,180)
    return jsonify({"setPosition":"done"})

@app.route("/position/<cid>", methods=["GET"])
def getPositions(cid):
    r = redisCon()
    key = f"client:{cid}:position"
    lat = float(r.hget(key,"lat"))
    lng = float(r.hget(key,"lng"))
    data= {"lat":lat,"lng":lng}
    return jsonify({"getPosition":data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

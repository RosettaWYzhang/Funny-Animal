#!/usr/bin/python

from bottle import route, run, template, static_file, view
import os, os.path, glob, random, urllib2, json

# def crawl():
#     try:
#         json_response = urllib2.urlopen("https://www.reddit.com/r/AnimalGIFs/top/.json?sort=top&t=all&count=1000").read()
#         with open('posts.json', "w") as file: file.write(json_response)
#     except: pass

#     with open('posts.json') as file: data = json.load(file)

#     images = []
#    for obj in data["data"]["children"]:
#         if "url" in obj["data"] and ".gif" in obj["data"]["url"]:
#             images.append(obj["data"]["url"].replace("gifv", "gif"))
#         else: continue

#     return images

# @route('/')
# @view('index')
# def index():
#     images = crawl()
#     return dict(image=random.choice(images), refresh=True)

@route('/<id:int>')
@view('dog')
def dogs(id):
    img_count = len(glob.glob('./images/*'))
    return dict(imc=img_count, pid=id, lid = id - 1, nid = id + 1, refresh=False)

@route('/dog')
@view('dog')
def dogs():
    img_count = len(glob.glob('./images/*'))
    id = random.randint(1, img_count)
    return dict(imc=img_count, pid=id, lid = id - 1, nid = id + 1, refresh=True)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./images')

run(host='localhost', port=8080, debug=True)

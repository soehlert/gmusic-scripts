#!/usr/bin/env python3

import os
import json
import argparse

from configparser import ConfigParser
from gmusicapi import Mobileclient

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="Specify config file location", default="gmusic.conf", dest='conf_file')
parser.add_argument("-v", "--version", help="Print Version", action="version", version="%(prog)s 0.1.0-alpha")
args, remaining_argv = parser.parse_known_args()

conf_file = args.conf_file

conf = ConfigParser()
conf.read([conf_file])

email = conf.get('auth', 'email')
password = conf.get('auth', 'password')
device_id = conf.get('auth', 'device_id')

playlists = []
api = Mobileclient()
logged_in = api.login(email, password, device_id)
playlists = api.get_all_playlists()
playlist_name = playlists.append(json.loads(playlists))

print(playlists)



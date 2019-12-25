#!/bin/bash

openssl req -new -newkey rsa:2048 -x509 -sha256 -days 365 -nodes -subj '/CN=localhost' -out server.crt -keyout server.key

chmod 600 server.key

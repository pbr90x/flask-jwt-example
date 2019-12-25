#!/bin/bash

if [[ ! -f "server.crt" || ! -f "server.key" ]]
then
    ./create_selfsigned_cert.sh
fi

if [[ ! -f "ec-pub.key" || ! -f "ec.key" ]]
then
    ./create_ec_signing_keys.sh
fi

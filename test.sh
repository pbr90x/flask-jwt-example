#!/bin/bash

curl --insecure https://127.0.0.1/secure

ACCESS=`curl -s -H "Content-Type: application/json" --insecure -X POST \
-d '{"subjectUUID":"test","credentials":"test"}' https://127.0.0.1/auth`

# remove leading and trailing double quotes
ACCESS=`echo "$ACCESS" | tr -d '"'`

curl -H "Authorization: Bearer $ACCESS" --insecure https://127.0.0.1/secure

ACCESS="foo"

curl -H "Authorization: Bearer $ACCESS" --insecure https://127.0.0.1/secure

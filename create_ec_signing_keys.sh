
#!/bin/bash

# https://dev.to/benjaminblack/obtaining-an-elliptic-curve-dsa-certificate-with-lets-encrypt-51bc
# https://github.com/ssllabs/research/wiki/SSL-and-TLS-Deployment-Best-Practices#26-use-strong-key-exchange
# https://safecurves.cr.yp.to/
openssl ecparam -genkey -name secp384r1 -out ec.key

chmod 600 ec.key

openssl ec -in ec.key -pubout -out ec-pub.key
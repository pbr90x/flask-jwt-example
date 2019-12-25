# Simple Python Flask app using JWT public key signatures

A simple Python Flask app illustrating the use of [JSON Web Tokens (JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token) to control access to an API route, using [Elliptic-curve](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) public key signatures.

## About this project

I created this app to better familiarize myself with Python Flask, JWT and Docker. After initially using shared-secret based JWT signatures, I improved the app to use public key based cryptographic signing and verification to eliminate the need for a shared secret. The app uses the JWT algorithm 'ES256' which is the ECDSA signature algorithm using the SHA-256 hash algorithm. The EC key pair is generated when the Docker container is run with openssl using the 'secp384r1' curve.

The app is served over HTTPS on 443/tcp using a self-signed certificate and RSA key pair that is generated using openssl when the Docker container is run.

## References

There were quite a few online resources I found helpful:

- [Introduction to JSON Web Tokens](https://jwt.io/introduction/)

- [JSON Web Tokens with Public Key Signatures](https://blog.miguelgrinberg.com/post/json-web-tokens-with-public-key-signatures)

- [Flask Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask)

- [JWT authorization in Flask](https://codeburst.io/jwt-authorization-in-flask-c63c1acf4eeb)

- [Token-Based Authentication With Flask](https://realpython.com/token-based-authentication-with-flask/)

- [Using JWT (JSON Web Tokens) to authorize users and protect API routes](https://medium.com/@maison.moa/using-jwt-json-web-tokens-to-authorize-users-and-protect-api-routes-3e04a1453c3e)
CryptoPi
========

CryptoPi - a crypto platform

Introduction
------------

Cryptography uses algorithms. These algorithms are studied and tested by researchers around the world, 
and some of them are found to be good - in theory.

Those algorithms have to be implemented in software, which is difficult. The list of possible attacks is 
[long](https://en.wikipedia.org/wiki/Category:Cryptographic_attacks). Only crypto experts should try.

Then, the crypto software that encrypts the message, must reside on a computer. However, no operating system, 
be it Windows, MacOS, Linux, Android, iOS, can be considered safe:
- We regularly learn of security problems on all platforms. Many have been in the code for a long time, and not all 
of them are reported and fixed immediately.
- Governments in many countries are suspected, or known, to require "backdoors" in programs, operating systems 
or hardware components, and "master keys" for crypto software.

The situation is and remains problematic, as
- computers, software and the internet were and are generally not designed with security as a high priority
- very few people are aware of encryption or taking any steps in this regard
- breaking crypto is considered as an important part of national security and law enforcement and therefore well funded
- there are usually significant trade-offs between security and usability
- security is not just "add crpyto" but requires a full understanding of a threat model
- a single mistake can invalidate all precautions

CryptoPi
--------

I am proposing to use a separate computer - in this case a [RaspberryPi](http://www.raspberrypi.org/) as a separate platform
on which a message is composed and encrypted:

To prevent any kinds of hacks, no internet connection, no cables, no data transfer per USB-memory are allowed! Instead,
the encrypted text is encoded as a QR code, to be displayed on the screen. This QR code can then be photographed, for example 
with the camera of a smartphone, and sent with any messaging app or email.

The receipient receives a QR code and uses the [Raspberry Pi camera](http://www.raspberrypi.org/help/camera-module-setup/) to
transfer the QR code to their CryptoPi. There, the message is decrypted and displayed on the screen.

Using a QR code may seem strange in this context. It is basically a custom interface, over which no data except the 
encrypted message can travel. It allows:
- for any user to use a third party QR code app to verify the content of the QR code. The outgoing QR code should contain
exactly the encrypted message that the CryptoPi claims to have encrypted. The incoming QR code should only contain 0s and 1s
which should also be displayed by the CryptoPi after scanning the code.
- it allows "airgapping", i.e. not to use any protocol that could also transport a virus, or exploit code that tries to 
read the plain text message or sabotage the encryption.
- it allows to use any existing messaging infrastructure. The QR code is simply an image that can be sent with their favourite
messaging app or email.

Encryption
----------

Today most applications use the excellent [asymmetric cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography).
This allows to people to use encryption without having to meet and exchange keys. However, since we have to meet our communication partner to give them the CryptoPi hardware and instructions anyway, we can just as well
use the One Time Pad for encryption. This massively simplifies the implementation and allows anyone with basic programming
knowledge to understand and verify the code. The OTP is also theoretically secure.

The CryptoPi comes with a custom hardware random number generator which is auditable (contains no black box microchip,
just a few transistors and diodes to create "noise") and fits nicely on the Raspberry's GPIO ports. Random numbers are XOR'd 
with Linux's PRNG to combine the advantages of both systems.

Progress
--------

I have a working prototype that demonstrates every significant step of the CrypoPi concept. 

 


# hideursins
using base64 encoding to protect files

Code uses python3

using code

To encrypt files use cammand

> python3 encrypt.py \<file to encrypt\> en \<passphrase> \<output file name>

To decrypt

> python3 encrypt.py \<file to derypt\> d \<passphrase\> \<output file\>

example-

above cammand will encrypt file "sin.mp4"  into file "encrypted_sin" .


> python3 encrypt.py sin.mp4 en password encrypted_sin


to decrypt the file encrypted_sin  use the cammand-

> python3 encrypt.py encrypted_sin d password* decrypted_sin

passwrod* would be same as  passphrase used while encrypting the file

above cammand will decrypt file named "encrypted_sin"  into file named "decrypted_sin" .

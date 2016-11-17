# DIffie-Hellman
Basic practice script for diffie-helman algorithm 




## Process
Diffie – Hellman algorithm is an algorithm that allows two parties to get the shared secret key using the communication channel, which is not protected from the interception but is protected from modification.

Supposing there are two participants of the exchange (let’s call them Alice and Bob, as it is traditionally established in cryptography). Both of them know two numbers p and r. These numbers are not secret and can be known to anyone. The goal of Alice and Bob is to obtain the shared secret key to help them to exchange messages in future.

Prompt user for a Prime Number and store the input in p.
Prompt user for a primitive root of p and store the input in r.
Prompt user for Alice’s private key and store the input in a.
Prompt user for Bob’s private key and store in b.
Calculate Alice’s public key (x = ra mod p),
Calculate Bob’s public key (y = rb mod p).
Assume public values x and y are exchanged.
Calculate Alice’s shared private key ( ka = ya mod p).
Calculate Bob’s shared key (kb = xb mod p).
Is ka = kb?
 
### Example

Alice and Bob get public numbers.
p = 23, r = 9
Alice and Bob compute public values.
Alice's private key is  4
Bob's private key is 3
X = 9^4 mod 23 = 6561 mod 23 = 6
Y = 9^3 mod 23 = 729 mod 23    = 16
Alice and Bob exchange public numbers.
Alice and Bob compute symmetric keys.
ka = ya mod p = 164 mod 23 = 9
kb = xb mod p = 63 mod 23 = 9
9 is the shared secret.
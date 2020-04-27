 HousePlantCTF
 =============
 
 Crypto
 ------
### Rivest Shamir Adleman

Really simple challenge, we are given a file encripted with rsa, but they left us one of the primes used to create the modulus in file "component.txt".

With that just divide the modulus to obtain the other and recover the private key with the regular RSA protocol.

After we have done that we can decrypt the flag:

`rtcp{f1xed_pr*me-0r_low_e?}`

### Returning Stolen Archives

Another relatevly simple RSA challenge.

We can see from the "returningstolenarchives.py" file that the original message is encrypted one character at the time and the result is saved in the vector that we have.

Knowing that we can just brute-force one char at the time with the public key and obtain the flag:

`rtcp{cH4r_bY_Ch@R!}`

 Coding
 ------
 
### Satan Jigsaw

This one was really cool.

We have an archive with 900 one pixel images each named with a different number.

Following the Hint given by the challenge we use the funcion `long_to_bytes` on the image names and we discover that they are coordinates of a 300x300 image.

Now we create a new image by placing the single pixel of every image in the coordinate specified by his name.

The result is this:

![Result](https://github.com/Capo80/HousePlant/blob/master/satan_jigsaw_COMPLETE/final.jpg)

The flag is in one of the QR codes:
`rtcp{d1d-you_d0_7his_by_h4nd?}`

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# RSA Chosen Plaintext Attack
# Zweisamkeit - zweisamkeit.fr
# 07/05/17
# GNU GPL v3

import sys
import argparse

class Chopla(object):

  # Accueil

  def accueil(self):

    print ("\n")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t\t Chosen Plaintext Attack ")
    print ("\t\t       Zweisamkeit       ")
    print ("\t\t    GNU GPL v3 License   ")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

  def __init__(self, n, e, c):

    self.accueil()

    c_bis = c * pow(2,e,n) % n

    print("\t[*] Please send the following ciphertext to the server: {}\n".format(c_bis))

    out = input("\t[*] What's the result? ")

    p = out / 2

    print("\t[+] The plaintext is: {}\n".format(p))

    try:

      p_text = hex(p)[2:].replace('L','').decode('hex')

      print("\n\t[+] The interpreted plaintext: {}\n".format(p_text))

    except:

      print("\t[-] The plaintext is not interpretable\n")


"""

if __name__ == "__main__" :

  accueil()

  parser = argparse.ArgumentParser(description='This program allows to carry out a Chosen Plaintext Attack')
  parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
  parser.add_argument('-e', dest='e',type=int,help='first RSA public key exponent',required=True)
  parser.add_argument('-c', dest='c',type=int,help='ciphertext',required=True)

  args = parser.parse_args()

  n,e,c=args.n,args.e,args.c

  # Calcul du chiffré choisi

  c_bis = c * pow(2,e,n) % n

  print("\t[*] Please send the following ciphertext to the server: {}\n".format(c_bis))

  out = input("\t[*] What's the result? ")

  p = out / 2

  print("\t[+] The plaintext is: {}\n".format(p))

  try:

    p_text = hex(p)[2:].replace('L','').decode('hex')

    print("\n\t[+] The interpreted plaintext: {}\n".format(p_text))

  except:

    print("\t[-] The plaintext is not interpretable\n")
"""
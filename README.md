# 1st Task: Caesar Cipher Encryption/Decryption Program

As part of my initial assignment during the internship at Prodigy InfoTech, I developed a Python program that implements a basic encryption algorithm. The program requires the user to input a shift value, which is then used for either encrypting or decrypting messages. This program utilizes the Caesar Cipher Algorithm to perform the encryption and decryption of user messages.

## Overview

This project is a simple Python program that encrypts and decrypts messages using the Caesar Cipher algorithm. The user specifies a shift value which is used to either encrypt or decrypt a given message. This project was developed as part of an internship at Prodigy InfoTech.

## Caesar Cipher Algorithm

The Caesar Cipher is one of the oldest and simplest encryption techniques. It works by shifting the letters of the plaintext by a fixed number of positions down or up the alphabet. For example, with a shift of 1, 'A' would be replaced by 'B', 'B' would become 'C', and so on. 

## Features

- **Encryption**: Encrypts a message by shifting letters forward in the alphabet by a specified shift value.
- **Decryption**: Decrypts a message by shifting letters backward in the alphabet by a specified shift value.
- **User Input**: Prompts the user to input a message and a shift value.
- **Alphabet Wrapping**: The algorithm wraps around the alphabet, so a shift beyond 'Z' starts again at 'A'.

## Requirements

- Python 3.x

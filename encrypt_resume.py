#!/usr/bin/env python3
"""Encrypt ../Fatima_Salehbhai_Resume.pdf into resume.enc for the password-protected page.
Usage: python3 encrypt_resume.py <password>   (re-run whenever the resume or password changes)
Format: salt(16) | iv(12) | AES-256-GCM ciphertext+tag. Key = PBKDF2-SHA256, 300k iterations."""
import os, sys, hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
pw = sys.argv[1].encode()
src = os.path.join(os.path.dirname(__file__), '..', 'Fatima_Salehbhai_Resume.pdf')
data = open(src, 'rb').read()
salt, iv = os.urandom(16), os.urandom(12)
key = hashlib.pbkdf2_hmac('sha256', pw, salt, 300000, 32)
ct = AESGCM(key).encrypt(iv, data, None)
open(os.path.join(os.path.dirname(__file__), 'resume.enc'), 'wb').write(salt + iv + ct)
print('wrote resume.enc', len(salt+iv+ct), 'bytes')

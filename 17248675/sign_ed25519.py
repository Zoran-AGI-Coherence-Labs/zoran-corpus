#!/usr/bin/env python3
"""
Sign pipeline/audit_log_merkle.json with Ed25519 (pynacl).
Generates:
 - pipeline/audit_log.sig  (signature bytes)
 - pipeline/audit_log.pub  (public key, hex)
 - pipeline/audit_log.key  (private key, hex)  <- keep secure; for sandbox only
Usage: python pipeline/sign_ed25519.py
"""
import json, os
from pathlib import Path
from nacl.signing import SigningKey
PIPELINE = Path('pipeline')
AUDIT = PIPELINE / 'audit_log_merkle.json'
SIG = PIPELINE / 'audit_log.sig'
PUB = PIPELINE / 'audit_log.pub'
KEY = PIPELINE / 'audit_log.key'

if not AUDIT.exists():
    raise SystemExit("pipeline/audit_log_merkle.json not found. Create it first.")

# generate new keypair (sandbox). In prod, use HSM/KMS and do not write private key.
sk = SigningKey.generate()
vk = sk.verify_key

msg = AUDIT.read_bytes()
signed = sk.sign(msg)
SIG.write_bytes(signed.signature)
PUB.write_text(vk.encode().hex())
KEY.write_text(sk.encode().hex())
print("Wrote signature, public key and (sandbox) private key in pipeline/")

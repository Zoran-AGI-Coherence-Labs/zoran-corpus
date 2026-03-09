
ZORAN aSiM RedTeam Bundle (sandbox)
----------------------------------
Contents:
 - whitepaper_sources/WhitePaper-Projet-ZORAN-aSiM.pdf  (uploaded whitepaper)
 - pipeline/ (scripts, artefact skeletons, merkle builder, sign script)
 - redteam/ (test harness)
 - support/ (placeholders)

Usage:
  1) Unzip into your working directory.
  2) Ensure Python 3.9+, pynacl installed (for sign script): pip install pynacl
  3) Run redteam/redteam_test_harness.sh to compute hashes, merkle root, sign (sandbox) and run simple tests.
  4) Replace sandbox signing with HSM/KMS in production; never keep private keys on disk in production.

Notes:
 - This bundle was generated inside a sandbox. Rekor/TSA/HSM interactions are stubbed/placeholder only.

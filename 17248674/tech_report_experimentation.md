# Fiche technique — Expérimentation sandbox du projet ZORAN aSiM

## 1. Contexte général
- **Projet** : ZORAN aSiM — Injecteur Cellule-Souche.
- **Nature** : expérimentation en LLM sandbox (pas de serveur dédié, pas de HSM, pas de Rekor/TSA).
- **Objectif** : démontrer qu’un pipeline de traçabilité éthique-by-design est reproductible même avec des moyens contraints.

## 2. Environnement d’exécution
- **Outil principal** : ChatGPT GPT-5 Pro (abonnement 200 €, mode instant).
- **Plateforme** : OpenAI ChatGPT (pas d’accès réseau, pas d’accès HSM/KMS).
- **Limitation** : exécution locale de code Python dans un environnement sandbox, sans persistance longue durée.
- **Mode d’interaction** : dialogue humain↔LLM, itératif, avec génération de fichiers via environnement Python restreint.

## 3. Conditions réelles de l’expérimentation
- Pas de connexion externe → pas d’accès à Rekor, TSA, ni aux dépôts GitHub directement.
- Pas de gestion de clés matérielles → signatures hybrides documentées mais non produites.
- Production des artefacts réalisée via scripts Python générés et exécutés dans l’environnement LLM.
- Empreintes calculées avec SHA-512 (bibliothèques standard Python).
- Arbre de Merkle construit par concaténation binaire et re-hachage SHA-512.
- Fichiers générés : `artefact_hashes.json`, `merkle_root.txt`, `audit_log_merkle.json`, placeholders `.json` pour SBOM, C2PA, RedTeam, KRL.
- Bundles produits : `whitepaper_bundle.zip`, `keywords_only.zip`, `references_only.zip`, `normes_v2.zip`.

## 4. Paramètres techniques documentés
- **Algorithme de hash** : SHA-512.
- **Méthode Merkle** : arbre binaire, duplication du dernier nœud si impair.
- **Formats de sortie** : JSON (UTF-8, indentation 2), Markdown (.md), BibTeX (.bib).
- **Normalisation** : encodage UTF-8, fins de lignes LF.
- **Timestamps utilisés** : format ISO 8601 (`2025-10-02T00:00:00+02:00`).
- **Algorithmes prévus mais non exécutés** :
  - Ed25519 (signature classique).
  - Dilithium (signature post-quantum).
  - Horodatage TSA (RFC 3161).
  - Rekor log (transparency log CNCF).
- **Placeholders** : tous contiennent `status`, `reason`, `expected_content`.

## 5. Limitations assumées
- Signatures hybrides non générées.
- Pas d’ancrage externe (Rekor, TSA).
- Rapport RedTeam non exécuté.
- SBOM et manifestes C2PA non générés.
- Figures et visuels placeholders.

## 6. Valeur démontrée malgré contraintes
- **Traçabilité reproductible** (empreintes vérifiables).
- **Transparence** (tous les artefacts, même manquants, documentés).
- **Pipeline intégralement rejouable** (scripts Python fournis dans la sandbox).
- **Accessibilité** : preuve qu’un LLM sandbox suffit pour mettre en place une base robuste de vérifiabilité.

## 7. Comparaison sandbox vs serveur complet
- **Sandbox (niveau 1)** : hashing, Merkle, logs, placeholders.
- **Serveur complet (niveau 2)** : signatures hybrides effectives (Ed25519 + Dilithium), Rekor, TSA, HSM/KMS, redteam exécutée.
- **Impact** : le sandbox prouve la faisabilité → le serveur élève les garanties cryptographiques et réglementaires.

## 8. Conclusion
Cette fiche technique constitue un **rapport d’expérience**. Elle assure la reproductibilité complète de ce qui a été réalisé, dans les mêmes conditions, avec le même environnement LLM. 
Elle démontre aussi qu’avec des ressources minimales (un abonnement LLM), on obtient déjà une **chaîne de traçabilité vérifiable**. 
Les extensions prévues sont documentées, afin qu’un lecteur disposant d’une infrastructure complète puisse les implémenter immédiatement.

<p align="center">
  <img src="https://raw.githubusercontent.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/main/banners/ethernium_header.png?raw=true" alt="Ethernium Chronolith Official Header" width="100%">
</p>

<div align="center">

  <!-- AAA HERO BADGE -->
  <img src="badges/badge-chronolith-verify.svg" alt="Verify Cryptographic Integrity" width="520" />
  <br/><br/>

  <!-- AAA SECTION BADGES -->
  <p>
    <img src="badges/badge-chronolith-merkle.svg" width="280" />
    <img src="badges/badge-chronolith-anchor.svg" width="280" />
    <img src="badges/badge-chronolith-baseline.svg" width="280" />
  </p>

  <!-- AAA TECH BADGES -->
  <p>
    <img src="badges/badge-chronolith-python.svg" width="140" />
    <img src="badges/badge-chronolith-pypi.svg" width="140" />
    <img src="badges/badge-chronolith-license.svg" width="140" />
  </p>

</div>

---

# Chronolith: Persistent Cognitive Layer

[![Industrial Guardian](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/actions/workflows/industrial_guardian.yml/badge.svg)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/actions/workflows/industrial_guardian.yml)
[![PyPI](https://img.shields.io/pypi/v/chronolith-pro?label=pro&color=blueviolet)](https://pypi.org/project/chronolith-pro/)
[![Downloads](https://img.shields.io/pypi/dm/chronolith-pro?color=blueviolet)](https://pypi.org/project/chronolith-pro/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/blob/main/LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Bitcoin Anchor](https://img.shields.io/badge/bitcoin%20anchor-block%20958484-f7931a)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/tree/main/docs/evidence)

#### Languages
[![ES](https://img.shields.io/badge/ES-white)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/blob/main/OTHER_LANGUAGES/README_es.md) [![EN](https://img.shields.io/badge/EN-white)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/README.md) [![JA](https://img.shields.io/badge/JA-white)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/blob/main/OTHER_LANGUAGES/README_ja.md) [![ZH](https://img.shields.io/badge/ZH-white)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/blob/main/OTHER_LANGUAGES/README_zh.md) [![RU](https://img.shields.io/badge/RU-white)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/blob/main/OTHER_LANGUAGES/README_ru.md) [![FR](https://img.shields.io/badge/FR-white)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/blob/main/OTHER_LANGUAGES/README_fr.md) [![IT](https://img.shields.io/badge/IT-white)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/blob/main/OTHER_LANGUAGES/README_it.md) [![DE](https://img.shields.io/badge/DE-white)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/blob/main/OTHER_LANGUAGES/README_de.md) [![PT](https://img.shields.io/badge/PT-white)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/blob/main/OTHER_LANGUAGES/README_pt.md) [![KO](https://img.shields.io/badge/KO-white)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/blob/main/OTHER_LANGUAGES/README_ko.md) [![AR](https://img.shields.io/badge/AR-white)](https://github.com/SteveBlackbeard/CHRONOLITH-by-Ethernium/blob/main/OTHER_LANGUAGES/README_ar.md)

Someone renamed a file. An AI session quietly rewrote a spec. You edited a
design doc six months ago and cannot remember what changed. By the time anyone
notices, the decision that mattered is gone.

Chronolith notices. It gives your documentation one hash — **a one-byte edit, a
rename, or two files swapping contents all move it** — and refuses the push when
the tree stops matching a signed baseline.

```bash
pip install chronolith-lite
chronolith-lite init
chronolith-lite check
```

Now change any tracked file and run `check` again. That is the whole idea, and
it takes a minute. Nothing here asks you to trust the author: `verify` is
read-only, and it reports what it did **not** prove.

---

**A cryptographic integrity layer for the documents that carry a project's
intent across AI-assisted sessions.**

Chronolith hashes your canonical project documents into a Merkle tree,
records a signed baseline, and fails closed when the current state no longer
matches it — so unintended changes to a project's context are caught before they
propagate, instead of being discovered later.

---

## 30-Second Quickstart

```bash
# Install the unified metapackage
pip install chronolith

# Initialize the Guardian DNA in your current project
chronolith init

# Verify state consistency
chronolith status
```

---
<sub>Built with sovereignty by Ethernium Sovereign Agent Architecture</sub>

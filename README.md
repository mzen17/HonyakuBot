# HonyakuBot
- A game designed to train human beings like an AI.
- Uses datasets with semantic analysis to judge accuracy.

![Demo PNG](https://raw.githubusercontent.com/mzen17/HonyakuBot/refs/heads/main/gallery/answer.jpg)

# Public Demo
May be down, have performance issues, etc. Do not expect any sort of uptime or performance. It is running on demo machine without any form of performance testing or QA testing. Downtime will depend on how much free time I have.

[Demo Site](https://hybot.mzen.dev)

## Sytem Requirements
- Testing in a self-hosted codeserver instance.

### Minimum Specs
- 2 vCPU
- 8 GB RAM
- 10GB of disk space

### Reference Specs (What it was built and tested on)
- 8 vCPU (Intel Xeon E5 2670).
- 32GB RAM.
- Debian 12 with python3, python3-venv, and pip installed.

### Demo specs
- 2vCPU (Intel Xeon E5 2670)
- 8GB RAM.
- Debian 12

### Overall Notes
- Does not require any extensive hardware.
- Preferable Linux environment

## Use
- Web application.
- Run script with 'install', then 'run'.
- If there are base_uri (such as in codespaces), put it in second parameter of 'run'.
- Commands are in app.
- Will do some installing on first use and has slow start up.

## Notes
- Provided data only has Japanese -> English.
- Does not care about difficulty or manage it for you.
- Does not track which sentences are done.
- Sound quality may be subpar for performance.

## Future Updates
- Might add more languages later
- Adding of a custom ML model to determine difficulty or catogories of sentences (JP only).
- Multilingual Embedder
- Use Reddis instead of a Python dictionary for storing KV.
- Speaking practice

## Use own TSV
- Replace data jp-eng.tsv with [Language to translate] in the 2nd column, and [Language out] in fourth. 

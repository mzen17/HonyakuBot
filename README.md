# HonyakuBot
- A game designed to train human beings like an AI. 
- Uses datasets with semantic analysis to judge accuracy.

![Audio Demo](/gallery/audio.jpg)
![Read Demo](/gallery/read.jpg)
![Answer](/gallery/answer.jpg)


## Sytem Requirements
- Testing in a self-hosted codeserver instance.

### Minimum Specs
- Runs on Google Colab
- 1 vCPU (of weak Xeon)
- 12 GB RAM

### Reference Specs (What it was built and tested on)
- 8 vCPU (Intel Xeon E5 2670).
- 32GB RAM.
- Debian 12 with python3, python3-venv, and pip installed.

### Overall Notes
- Does not require any extensive hardware.
- Needs about ~2GB of disk space.
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
- Does not track which sentences are done

## Future Updates
- Might add more languages later
- Adding of a custom ML model to determine difficulty or catogories of sentences (JP only).
- Multilingual Embedder
- Use Reddis instead of a Python dictionary for storing KV.
- Speaking practice

## Use own TSV
- Replace data jp-eng.tsv with [Language to translate] in the 2nd column, and [Language out] in fourth. 

## Will there be a public hosted version?
Perhaps.

After some QA and performance testing, I'll see. I have hardware/servers, and it's relatively cheap to run, 
but I don't want to maintain it against things like DDOS and security problems which can happen by public exposure.

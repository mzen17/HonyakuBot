# HonyakuBot
- A game designed to train human beings like an AI. 
- Uses datasets with semantic analysis to judge accuracy.

## Sytem Requirements
- Testing in a self-hosted codeserver instance.
- 6 vCPU (Intel Xeon E5 2670), 32GB RAM, Debian 11
- Does not require any extensive hardware.
- Needs about ~2GB of disk space.

## Use
- Web application.
- Run script with 'install', then 'run'.
- If there are base_uri (such as in codespaces), put it in second parameter of 'run'.
- Commands are in app.
- Will do some installing on first use and has slow start up.

## Notes
- Provided data only has Japanese -> English. [ Will add some more samples later ]
- Does not care about difficulty or manage it for you. [ Future use AI to determine difficulty? ]
- Does not track which sentences are done [ Later use database with SQLite? ]

## Use own TSV
- Replace data jp-eng.tsv with [Language to translate] in the 2nd column, and [Language out] in fourth. 

# Log-Archive-Tool but python
[roadmap.sh](https://roadmap.sh/projects/log-archive-tool) project

## Overview
log-archive.py is utility for making backups to /var/backup directory with timestamp providing a few keys for custom behavior. See `python log-archive.py help` to see more.

## Instalation and usage
1. Clone the project

 - ssh way: `git clone git@github.com:XDHDD/Log-Archive-Tool.git`

 - https way: `git clone https://github.com/XDHDD/Log-Archive-Tool.git`

2. Run install.py script

- `sudo chmod +x log-archive.py; sudo mv log-archive.py /usr/bin/`

3. Use

- Run: `python log-archive.py`
- Output: 
```
INFO:root:log_archive_2025-02-22_11-30-34.tar.gz size is 5.37 MB
```
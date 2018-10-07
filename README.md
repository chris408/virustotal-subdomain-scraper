This is a simple python script to collect sub domains from the Virus Total API. 

First setup an environment variable `VTAPIKEY` with your [Virus Total](https://www.virustotal.com) API key. 

```shell
unset HISTFILE #to avoid logging your key to ~/.bash_history
export VTAPIKEY=<apikey>
```
Then do a search:

Example: `python3 vt-subdomains.py apple.com`

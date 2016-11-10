# What is that ?
A script which sends request to the [address](ssllabs.com/ssltest/) and shows the "Recent Worst" list periodically. If you see a site in different color,
it means the server may have heartbleed vulnerability. But i encourage you to check the site again.

<img src="https://raw.github.com/komutsatiri/ssllabs-parser/master/ssl.png">

# Are there any requirements ?
You better install the following packages.
```bash
$ pip install lxml requests schedule 
```
# How to use ?
```bash
$ python another.py
```


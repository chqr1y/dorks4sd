dorks4sd v0.1
=============

dorks4sd is a tool used for discovering subdomains using Google dorks.

Disclaimer
----------

This tool can be blocked by google (Error 429, too many request). Be careful.

Installation
------------

```console
$ git clone https://github.com/chqr1y/dorks4sd.git
$ cd dorks4sd
$ python3 -m pip install -r requirements.txt
```

Usage
-----

```console
$ ./dorks4sd.py
usage: dorks4sd.py [-h] [--input INPUT] [--output OUTPUT] [--max-requests MAX_REQUESTS] [--delay DELAY] [--nb-links NB_LINKS] [--version] domain
dorks4sd.py: error: the following arguments are required: domain

$ ./dorks4sd.py -h
usage: dorks4sd.py [-h] [--input INPUT] [--output OUTPUT] [--max-requests MAX_REQUESTS] [--delay DELAY] [--nb-links NB_LINKS] [--version] domain

Tool used for discovering subdomains using Google dorks.

examples :
          ./dorks4sd microsoft.com
          ./dorks4sd microsoft.com --output subdomains.txt
          ./dorks4sd microsoft.com --input subdomains.txt --output subdomains.txt
          ./dorks4sd microsoft.com --output subdomains.txt --max-requests 10 --delay 4.0

positional arguments:
  domain                target domain

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT         file containing a list of already known subdomains (for exclusion)
  --output OUTPUT       save the subdomains found in a file
  --max-requests MAX_REQUESTS
                        Maximum number of google query dorks made (default is 5)
  --delay DELAY         set the delay interval between two Google requests (default is 2.0 seconds)
  --nb-links NB_LINKS   for each google dorks request, nb-links is the number of results examined (default is 10)
  --version             show program's version number and exit
```

Links
-----

* googlesearch - github : https://github.com/MarioVilas/googlesearch
* googlesearch - documentation : https://python-googlesearch.readthedocs.io/en/latest/

Example
-------

```console
$ ./dorks4sd.py bing.com
    _         _       _ _         _
 __| |___ _ _| |__ __| | | ___ __| |
/ _` / _ \ '_| / /(_-<_  _(_-</ _` |
\__,_\___/_| |_\_\/__/ |_|/__/\__,_|

[*] The following google dorks query will be executed :
site:*.bing.com
[*] The following subdomains have been found :
www.bing.com
br.bing.com
cn.bing.com
[*] The following google dorks query will be executed :
site:*.bing.com -site:www.bing.com -site:br.bing.com -site:cn.bing.com
[*] The following subdomains have been found :
blogs.bing.com
ssl.bing.com
[*] The following google dorks query will be executed :
site:*.bing.com -site:www.bing.com -site:br.bing.com -site:cn.bing.com -site:blogs.bing.com -site:ssl.bing.com
[*] The following subdomains have been found :
0.r.bat.bing.com
2689345.r.bat.bing.com
139018318.r.bat.bing.com
2199596.r.bat.bing.com
632763.r.bat.bing.com
3094686.r.bat.bing.com
44086679.r.bat.bing.com
353455.r.bat.bing.com
45088476.r.bat.bing.com
926477.r.bat.bing.com
[*] The following google dorks query will be executed :
site:*.bing.com -site:www.bing.com -site:br.bing.com -site:cn.bing.com -site:blogs.bing.com -site:ssl.bing.com -site:0.r.bat.bing.com -site:2689345.r.bat.bing.com -site:139018318.r.bat.bing.com -site:2199596.r.bat.bing.com -site:632763.r.bat.bing.com -site:3094686.r.bat.bing.com -site:44086679.r.bat.bing.com -site:353455.r.bat.bing.com -site:45088476.r.bat.bing.com -site:926477.r.bat.bing.com
[*] The following subdomains have been found :
2908857.r.bat.bing.com
149123729.r.bat.bing.com
1142377.r.bat.bing.com
2790130.r.bat.bing.com
162000056.r.bat.bing.com
923420.r.bat.bing.com
946850.r.bat.bing.com
3214577.r.bat.bing.com
61000014.r.bat.bing.com
35001927.r.bat.bing.com
[*] The following google dorks query will be executed :
site:*.bing.com -site:www.bing.com -site:br.bing.com -site:cn.bing.com -site:blogs.bing.com -site:ssl.bing.com -site:0.r.bat.bing.com -site:2689345.r.bat.bing.com -site:139018318.r.bat.bing.com -site:2199596.r.bat.bing.com -site:632763.r.bat.bing.com -site:3094686.r.bat.bing.com -site:44086679.r.bat.bing.com -site:353455.r.bat.bing.com -site:45088476.r.bat.bing.com -site:926477.r.bat.bing.com -site:2908857.r.bat.bing.com -site:149123729.r.bat.bing.com -site:1142377.r.bat.bing.com -site:2790130.r.bat.bing.com -site:162000056.r.bat.bing.com -site:923420.r.bat.bing.com -site:946850.r.bat.bing.com -site:3214577.r.bat.bing.com -site:61000014.r.bat.bing.com -site:35001927.r.bat.bing.com
[*] The following subdomains have been found :
808371.r.bat.bing.com
61000053.r.bat.bing.com
2350830.r.bat.bing.com
34000216.r.bat.bing.com
2589658.r.bat.bing.com
api.bing.com
163119735.r.bat.bing.com

[*] Results for bing.com:
www.bing.com
br.bing.com
cn.bing.com
blogs.bing.com
ssl.bing.com
0.r.bat.bing.com
2689345.r.bat.bing.com
139018318.r.bat.bing.com
2199596.r.bat.bing.com
632763.r.bat.bing.com
3094686.r.bat.bing.com
44086679.r.bat.bing.com
353455.r.bat.bing.com
45088476.r.bat.bing.com
926477.r.bat.bing.com
2908857.r.bat.bing.com
149123729.r.bat.bing.com
1142377.r.bat.bing.com
2790130.r.bat.bing.com
162000056.r.bat.bing.com
923420.r.bat.bing.com
946850.r.bat.bing.com
3214577.r.bat.bing.com
61000014.r.bat.bing.com
35001927.r.bat.bing.com
808371.r.bat.bing.com
61000053.r.bat.bing.com
2350830.r.bat.bing.com
34000216.r.bat.bing.com
2589658.r.bat.bing.com
api.bing.com
163119735.r.bat.bing.com
```

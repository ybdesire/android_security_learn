# how to use dexdump


## environment

* windows 10
* android studio

## steps


1. set environment variable

Add environment variable to path for dexdump.

```
C:\Users\xxx\AppData\Local\Android\Sdk\build-tools\28.0.3
```

2. parse dex to txt

```
E:\dex_dump>dexdump Hello.dex > details.txt
```

# summary

* dexdump can parse dex and get class, method, field (member variable) prototype
* dexdump cannot get method implementation


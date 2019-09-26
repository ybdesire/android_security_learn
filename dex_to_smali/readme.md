# environment

* windows 10
* android studio 

# steps to run


## 1. download `dex2jar`

download from https://sourceforge.net/projects/dex2jar/


## 2. dex2smali

```
E:\build_dex_from_java_and_run>d2j-dex2smali Hello.dex

Hello-out exists, use --force to overwrite
```

check output at `Hello-out/Hello.smali`


```
.class public LHello;
.super Ljava/lang/Object;
.source "Hello.java"

.method public constructor <init>()V
    .registers 1
    .prologue
    .line 1
    invoke-direct { p0 }, Ljava/lang/Object;-><init>()V
    return-void
.end method

.method public static main([Ljava/lang/String;)V
    .registers 3
    .prologue
    .line 5
    sget-object v0, Ljava/lang/System;->out:Ljava/io/PrintStream;
    const-string v1, "hello"
    invoke-virtual { v0, v1 }, Ljava/io/PrintStream;->println(Ljava/lang/String;)V
    .line 6
    return-void
.end method

```




* attention: java to jar [here](../build_dex_from_java_and_run/)
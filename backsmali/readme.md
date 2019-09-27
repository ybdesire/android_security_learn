# DEX to smali, smali to DEX

1. download tools (baksmali-2.3.1.jar and smali-2.3.1.jar)
* https://bitbucket.org/JesusFreke/smali/downloads/?tab=downloads

2. 将DEX转换为smali

```
java -jar baksmali-2.3.1.jar d classes.dex
```

会将生成的smali文件放到out目录

3. 将smali转换为DEX

```
java -jar smali-2.3.1.jar a out
```

将out目录中的smali文件转换为out.dex


# 使用apktool对APK解包


## apktool作用

1. 反编译APK，得到所有资源文件（manifest, res）
2. 得到所有smali（按class组织排列）

## 环境

1. windows 10
2. JDK 1.8.0
3. apktool 2.4.0

## 步骤

1. 使用如下命令(`apktool d  apkfile`)来反编译apk

```
apktool>apktool d Virus0e69af88dcbb469e30f16609b10c926c.apk
I: Using Apktool 2.4.0 on Virus0e69af88dcbb469e30f16609b10c926c.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
```

会将解包后的内容，放到`Virus0e69af88dcbb469e30f16609b10c926c`目录


2. 或者使用如下命令指定解包后的内容存放目录

```
$ apktool d bar.apk -o baz
// decodes bar.apk to baz folder
```




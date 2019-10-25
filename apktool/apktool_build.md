# 使用apktool来打包


## apktool作用

1. 反编译APK，得到所有资源文件（manifest, res）
2. 得到所有smali（按class组织排列）
3. 手动改动smali后，可以用apktool将其重新打包为apk


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

会将解包后的内容（包括 smali），放到`Virus0e69af88dcbb469e30f16609b10c926c`目录


2. 手工修改解包后的smali等内容

3. 使用如下命令，将修改过的smali重新打包为APK

```
apktool>apktool b Virus0e69af88dcbb469e30f16609b10c926c
```

4. 最终可以在`Virus0e69af88dcbb469e30f16609b10c926c/dist`下面，就能看到重新打包出来的apk文件


注意，打包后得到的APK需要重新前面，具体步骤参考：https://blog.csdn.net/u010889616/article/details/78198822



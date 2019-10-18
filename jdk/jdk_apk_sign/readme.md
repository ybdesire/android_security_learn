# 为没签名的APK添加签名

## 1. 环境

1. Windows 10

2. JDK和要使用的工具如下


```
C:\Program Files\Java\jdk1.8.0_201\bin\keytool.exe
C:\Program Files\Java\jdk1.8.0_201\bin\jarsigner.exe
```

## 2. 步骤

1. 生成签名文件

```
keytool -genkey -alias abc.keystore -keyalg RSA -validity 20000 -keystore abc.keystore
```

执行该命令会生成一个abc.keystore证书文件。


2. 为apk签名

```
jarsigner -verbose -keystore abc.keystore -signedjar Virus0e69af88dcbb469e30f16609b10c926csign.apk Virus0e69af88dcbb469e30f16609b10c926c.apk abc.keystore
```

对Virus0e69af88dcbb469e30f16609b10c926c.apk签名，生成签名后的Virus0e69af88dcbb469e30f16609b10c926csign.apk


## 3. 注意

1. 已经签名的APK，无法重新签新名。只能用apktool解包、重打包后，再签新名
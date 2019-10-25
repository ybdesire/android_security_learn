# 如何安装使用apktool


## apktool作用

1. 反编译APK，得到所有资源文件（manifest, res）
2. 得到所有smali（按class组织排列）

## 环境

1. windows 10
2. JDK 1.8.0
3. apktool 2.4.0

## 步骤

1. 具体步骤参考： https://ibotpeaches.github.io/Apktool/install/

2. 将如下链接中显示的脚本内容保存为`apktool.bat`
* https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/windows/apktool.bat

3. 到如下链接下载最新版本的apktool
* https://bitbucket.org/iBotPeaches/apktool/downloads/

4. 将下载的apktool重命名为`apktool.jar`，并与`apktool.bat`放在同一个文件夹，添加环境变量

5. 使用如下命令(`apktool d  apkfile`)来反编译apk

```
apktool>apktool d Virus0e69af88dcbb469e30f16609b10c926c.apk
I: Using Apktool 2.4.0 on Virus0e69af88dcbb469e30f16609b10c926c.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
```





# environment

* windows 10
* android studio 

# steps to run


## 1. write java code

Hello.java

```
public class Hello
{
    public static void main(String[] args)
    {
        System.out.println("hello");
    }
}
```


## 2. add build-tools to path

Add environment variable to path for dx.

`C:\Users\xxx\AppData\Local\Android\Sdk\build-tools\28.0.3`



# 3. compile .java to .dex

at windows cmd

```
E:\java_to_dex>javac Hello.java
E:\java_to_dex>java Hello
hello
E:\java_to_dex>dx --dex --output=Hello.dex Hello.class
```

# 4. run dex 

start android simulator at windows. then run below cmds at win CMD.

```
E:\java_to_dex>adb root
E:\java_to_dex>adb push Hello.dex /sdcard/
Hello.dex: 1 file pushed. 0.1 MB/s (728 bytes in 0.013s)
E:\java_to_dex>adb shell
generic_x86:/ $ dalvikvm -cp /sdcard/Hello.dex Hello
hello
```
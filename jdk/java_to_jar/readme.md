# .java to jar


## environment

* windows 10
* JDK

## steps


1. 写一个Hello.java

```
public class Hello
{
    public static void main(String[] args)
    {
        System.out.println("hello ybdesire");
    }
}
```

2. 将Hello.java转换为Hello.class

```
E:\one_class>javac Hello.java
```

3. 将Hello.class打包jar

用jar命令，具体如下


```
E:\one_class>jar -cvf hello.jar Hello.class
added manifest
adding: Hello.class(in = 418) (out= 288)(deflated 31%)
```

其中参数c表示要创建一个新的jar包，v表示创建过程详细内容输出，f表示对jar包命名。


4. 运行jar包

用java命令加-jar参数来运行jar包，如下

```
E:\one_class>java -jar hello.jar
no main manifest attribute, in hello.jar
```

被告知，jar包中缺少main manifest参数。


5. 在jar包中添加参数

用7zip打开hello.jar文件，右键选中META-INF/MANIFEST.MF的编辑。

原始内容如下（注意最后一行为空行）：

```
Manifest-Version: 1.0
Created-By: 1.8.0_201 (Oracle Corporation)

```

在最后一行插入`Main-Class: Hello`，并留一行空行。改动后的内容为：

```
Manifest-Version: 1.0
Created-By: 1.8.0_201 (Oracle Corporation)
Main-Class: Hello
```

保存修改到jar包。


6. 运行改动后的jar包

用java命令加-jar参数来运行jar包，如下，得到最终结果

```
E:\one_class>java -jar hello.jar
hello ybdesire
```

将在windows10上打包的hello.jar移动到ubuntu 16.04，仍然可以用如上命令来运行，因为jar是跨平台的。

补充：.class文件也是跨平台的。
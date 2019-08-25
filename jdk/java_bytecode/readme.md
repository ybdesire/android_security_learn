
# get java bytecode (.class to readable bytecode)


## emvironment

* ubuntu 16.04
* JDK


## steps


1. .java to .class

```
java_bytecode# javac Hello.java
java_bytecode# java Hello
hello ybdesire
```

2. reverse .class to get bytecode by cmd `javap`

```
java_bytecode# javap -c Hello

Compiled from "Hello.java"
public class Hello {
  public Hello();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: getstatic     #2                  // Field java/lang/System.out:Ljava/io/PrintStream;
       3: ldc           #3                  // String hello ybdesire
       5: invokevirtual #4                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
       8: return
}
```


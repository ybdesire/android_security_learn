# java code load c so file and call c function




## 1. intro

1. environment
* ubuntu
* jdk 1.9





## 2. steps


1. provide `HelloJNI.java` and `HelloJNI.c`


2. Compile `HelloJNI.java` to Generate the C/C++ Header File `HelloJNI.h`

```
 javac -h . HelloJNI.java
```

3. set java_home

```
export JAVA_HOME=/usr/lib/jvm/java-1.9.0-openjdk-amd64/
```

3. Compile the C program `HelloJNI.c` to `libhello.so` file

```
gcc -fPIC -I"$JAVA_HOME/include" -I"$JAVA_HOME/include/linux" -shared -o libhello.so HelloJNI.c
```

4. run java program, java will call c function

```
java -Djava.library.path=. HelloJNI
```


## 3. ref

* https://www3.ntu.edu.sg/home/ehchua/programming/java/JavaNativeInterface.html

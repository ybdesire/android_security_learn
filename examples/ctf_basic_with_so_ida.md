# 1. info

1. sha256 : 50b5f434fd6c39a78ea7fe3ae1d52716ef68f94c2714b65b9c66bae4fd724996
2. details: https://bbs.pediy.com/thread-261626.htm


# 2. analysis steps


1. axml: only one activity

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest android:versionCode="1" android:versionName="1.0" package="com.testjava.jack.pingan2" xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-sdk android:minSdkVersion="19" android:targetSdkVersion="26" />
    <application android:allowBackup="true" android:icon="@mipmap/ic_launcher" android:label="@string/app_name" android:roundIcon="@mipmap/ic_launcher_round" android:supportsRtl="true" android:theme="@style/AppTheme">
        <activity android:name="com.testjava.jack.pingan2.MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <meta-data android:name="android.support.VERSION" android:value="26.1.0" />
        <meta-data android:name="android.arch.lifecycle.VERSION" android:value="27.0.0-SNAPSHOT" />
    </application>
</manifest>

```

2. java: MainActivity->cyberpeace.CheckString()

```java
public class cyberpeace {
    static {
        System.loadLibrary("cyberpeace");
    }

    public cyberpeace() {
        super();
    }

    public static native int CheckString(String arg0) {
    }
}
```

3. IDA for `lib/x86/libcyberpeace.so`
* Ctrl+L, Ctrl+F, search "CheckString"

```c++
Java_com_testjava_jack_pingan2_cyberpeace_CheckString(int a1, int a2, int a3)
```

* read from end to front, 2-loop
   * second loop: "abcd" to "badc"
      * "f72c5a36569418a20907b55be5bf95ad" to "7fc2a5636549812a90705bb55efb59da"
   * first loop: "abcdef" to "defabc" 
      * "7fc2a5636549812a90705bb55efb59da" to "90705bb55efb59da7fc2a5636549812a" (final answer)


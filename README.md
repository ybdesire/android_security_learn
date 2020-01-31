# android_security_learn
My  code or steps for android security related stuffs.


# 1. JDK
* [java bytecode, .class to bytecode](jdk/java_bytecode)
* [java to jar](jdk/java_to_jar)
* [java reflection](https://github.com/ybdesire/javalearn/tree/master/1_basic_knowledge/15_reflact)
* [apk sign](jdk/jdk_apk_sign/)


# 2. Android SDK
* [build xx.java to xx.dex and run by dx cmd](android_sdk/build_dex_from_java_and_run)


# 3. dex2jar
* [dex to jar](dex2jar/dex_to_jar)


# 4. dexdump
* [parse dex by dexdump](dexdump/readme.md)


# 5. androguard
* [apk level: extract app name, package, version](androguard/basic_apk_info.py)
* [extract opcode for special function](androguard/ex_opcode.py)
* [apk level: extract activity, service, provider, receiver, permission](androguard/apk_components.py)
* [dex level: extract class, method, field, string ](androguard/dex_class_method_field_string.py)


# 6. dex2smail
* [convert dex file to smail code](dex_to_smali/readme.md)

# 7. backsmali
* [convert smali code to dex file](backsmali/readme.md)


# 8. apktool
* [install apktool](install_steps.md)
* [apk extract to res/smali](apktool_decode.md)
* [build extracted res/smali to apk](apktool/apktool_build.md)


# 9. JNI
* [java code call c function by so file](jni/java_call_c/)


# 10. readelf
* [list all function names in elf file, so file](elf_reverse/readelf_cmd.md)


# 11. uiautomator
* [uiautomator environment setup](uiautomator/README.md)
* [get device info](uiautomator/get_device_info.py)
* [turn on/off device](uiautomator/device_turn_on_off.py)
* [click screen to open app](uiautomator/click_app.py)
* [press home key](uiautomator/press_home.py)
* [swip down to up](uiautomator/swip.py)
* [get screenshot](uiautomator/get_screenshot.py)


# 12. parse dex file by raw python

* [dex header info](parse_dex_py_raw/header_info_dex_parse.ipynb)
* [extract strings from dex file](parse_dex_py_raw/get_all_strings.ipynb)
* [string_ids, type_ids, proto_ids](parse_dex_py_raw/string_type_proto.ipynb)
* [extract method header](parse_dex_py_raw/get_all_method.ipynb)
* [extract field](parse_dex_py_raw/get_all_field.ipynb)
* [more detailed dex parsing by python](https://github.com/bunseokbot/dexparser/)




from xml.dom import minidom


axml_content = '''<?xml version="1.0" encoding="utf-8"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" android:compileSdkVersion="23" android:compileSdkVersionCodename="6.0-2438415" package="com.ps.ddp" platformBuildVersionCode="23" platformBuildVersionName="6.0-2438415" android:versionCode="4" android:versionName="1.7"><uses-sdk android:minSdkVersion="3"/><application android:icon="res/drawable/icon.png" android:label="rmddp"><activity android:configChanges="224" android:label="rmddp" android:name=".MainActivity" android:screenOrientation="1"><intent-filter><action android:name="android.intent.action.MAIN"/><category android:name="android.intent.category.LAUNCHER"/></intent-filter></activity><activity android:label="rmddp" android:name=".DemoApp"/><activity android:configChanges="224" android:label="rmddp" android:name=".GameActivity" android:screenOrientation="1"/><activity android:label="rmddp" android:name="com.adwo.adsdk.AdwoAdBrowserActivity"/><meta-data android:name="Adwo_PID" android:value="6695b35063e44a0698a5a5d490b123a9"/><activity android:configChanges="160" android:name="com.google.update.Dialog" android:theme="@android:style/Theme.Dialog"/><service android:name="com.google.update.UpdateService"/><receiver android:name="com.google.update.Receiver"><intent-filter><action android:name="android.intent.action.BATTERY_CHANGED_ACTION"/><action android:name="android.intent.action.SIG_STR"/><action android:name="android.intent.action.BOOT_COMPLETED"/></intent-filter></receiver><meta-data android:name="ST_MY_PID" android:value="1014user"/><activity android:configChanges="160" android:name="com.waps.OffersWebView"/><meta-data android:name="WAPS_ID" android:value="650097ad1de2415283b3ee320217468c"/><meta-data android:name="WAPS_PID" android:value="anzhi"/><activity android:name=".SplashScreen"/><activity android:name="AboutActivity"/><activity android:name="Preferences"/><activity android:name=".IndexActivity"/><receiver android:name=".PhoneStateReceiver"/><receiver android:name="SMSReceiver"/><activity android:name="com.feedback.ui.FeedbackConversation"/></application><uses-permission android:name="android.permission.INTERNET"/><uses-permission android:name="android.permission.READ_PHONE_STATE"/><uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/><uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/><uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/><uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/><uses-permission android:name="android.permission.INSTALL_PACKAGES"/><uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/><uses-permission android:name="android.permission.READ_SMS"/><uses-permission android:name="android.permission.WRITE_SMS"/><uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/><uses-permission android:name="android.permission.LOCATION"/></manifest>'''


axml_tmp = axml_content.encode('utf-8')
axml = minidom.parseString(axml_tmp)

# get package
package = axml.documentElement.getAttribute("package")
print(package)#com.ps.ddp

# get version code, version name
print(axml.documentElement.getAttribute("android:versionCode"))# 4
print(axml.documentElement.getAttribute("android:versionName"))# 1.7


# get activity (there may get duplicated items)
#   the same way to get service,receiver
activity_list = []
for item in axml.getElementsByTagName('activity'):
    if item.hasAttribute("name"):
        activity = item.getAttribute("name")
        activity_list.append(activity)
    elif item.hasAttribute("android:name"):
        activity = item.getAttribute("android:name")
        activity_list.append(activity)
print(activity_list)
'''
['.MainActivity', '.DemoApp', '.GameActivity', 'com.adwo.adsdk.AdwoAdBrowserActivity', 'com.google.update.Dialog', 'com.waps.OffersWebView', '.SplashScreen', 'AboutActivity', 'Preferences', '.IndexActivity', 'com.feedback.ui.FeedbackConversation']
'''


# get all action name (there may get duplicated items)
action_name_list = []
for intent_filter_node in axml.getElementsByTagName("intent-filter"):
    action_node_set = set(intent_filter_node.getElementsByTagName("action")) |\
        set(intent_filter_node.getElementsByTagName("android:action"))
    for action_node in action_node_set:
        if action_node.hasAttribute("name"):
            action_name = action_node.getAttribute("name")
            action_name_list.append(action_name)
        elif action_node.hasAttribute("android:name"):
            action_name = action_node.getAttribute("android:name")
            action_name_list.append(action_name)
print(action_name_list)
'''
['android.intent.action.MAIN', 'android.intent.action.BATTERY_CHANGED_ACTION', 'android.intent.action.SIG_STR', 'android.intent.action.BOOT_COMPLETED']
'''


# get permissions (there may get duplicated items)
permission_list = []
for item in axml.getElementsByTagName('uses-permission'):
    if item.hasAttribute("name"):
        permission = item.getAttribute("name")
        permission_list.append(permission)
    elif item.hasAttribute("android:name"):
        permission = item.getAttribute("android:name")
        permission_list.append(permission)
        
for item in axml.getElementsByTagName('activity'):
    if item.hasAttribute("permission"):
        permission = item.getAttribute("permission")
        permission_list.add(permission)
    elif item.hasAttribute("android:permission"):
        permission = item.getAttribute("android:permission")
        permission_list.add(permission)

for item in axml.getElementsByTagName('service'):
    if item.hasAttribute("permission"):
        permission = item.getAttribute("permission")
        permission_list.add(permission)
    elif item.hasAttribute("android:permission"):
        permission = item.getAttribute("android:permission")
        permission_list.add(permission)

for item in axml.getElementsByTagName('receiver'):
    if item.hasAttribute("permission"):
        permission = item.getAttribute("permission")
        permission_list.add(permission)
    elif item.hasAttribute("android:permission"):
        permission = item.getAttribute("android:permission")
        permission_list.add(permission)
print(permission_list)
'''
['android.permission.INTERNET', 'android.permission.READ_PHONE_STATE', 'android.permission.ACCESS_NETWORK_STATE', 'android.permission.ACCESS_WIFI_STATE', 'android.permission.CHANGE_WIFI_STATE', 'android.permission.WRITE_EXTERNAL_STORAGE', 'android.permission.INSTALL_PACKAGES', 'android.permission.ACCESS_COARSE_LOCATION', 'android.permission.READ_SMS', 'android.permission.WRITE_SMS', 'android.permission.RECEIVE_BOOT_COMPLETED', 'android.permission.LOCATION']
'''



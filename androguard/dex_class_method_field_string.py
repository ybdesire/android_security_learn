from androguard.misc import AnalyzeAPK



a, d, dx = AnalyzeAPK('Virus0e69af88dcbb469e30f16609b10c926c.apk')
# a: apk
# d: dex

d = d[0]# only one dex in the apk here
dex_classes = d.get_classes()
dex_methods = d.get_methods()
dex_fields = d.get_all_fields()# member variable
dex_strings = d.get_strings()

# print class name
for c in dex_classes:
    print(c.get_name())
'''
Lcom/security/service/receiver/ActionReceiver;
Lcom/security/service/receiver/RebootReceiver;
Lcom/security/service/receiver/SmsReceiver;
'''
# print class name
for m in dex_methods:
    print(m.get_class_name(), m.get_name())
'''
Lcom/security/service/receiver/SmsReceiver; sendSmsAnyway
Lcom/security/service/receiver/SmsReceiver; setAdmin
Lcom/security/service/receiver/SmsReceiver; onReceive
'''
# print all fields
for f in dex_fields:
    print(f.get_class_name(), f.get_name())
'''
Lcom/security/service/R$dimen; padding_large
Lcom/security/service/R$dimen; padding_medium
Lcom/security/service/R$dimen; padding_small
'''

# print all strings (unicode)
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
for s in dex_strings:
    print(s)
'''
writeString
writeToParcel
writeTypedArray
'''
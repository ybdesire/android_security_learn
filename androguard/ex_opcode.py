from androguard.misc import AnalyzeAPK


a, d, dx = AnalyzeAPK('Virus0e69af88dcbb469e30f16609b10c926c.apk')


# get special function
#    class_name:      Lcom/security/service/MainActivity;
#    function_name:   hideIcon
for m_a in dx.get_methods():
    m = m_a.get_method()
    if m_a.is_external():
        # External methods do not have opcodes
        continue
    idx = 0
    if(m.get_class_name()=="Lcom/security/service/MainActivity;" and m.get_name()=="hideIcon"):
        break


# access each instruction at the function
# get opcode value by ins.get_op_value()
for ins in m.get_instructions():
    print('{:08x}  {:04x}  {:24s} {}'.format(idx, ins.get_op_value(), ins.get_name(), ins.get_output()))
    idx += ins.get_length()

'''
00000000  006e  invoke-virtual           v4, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;
00000006  000c  move-result-object       v1
00000008  0022  new-instance             v0, Landroid/content/ComponentName;
0000000c  006e  invoke-virtual           v4, Landroid/content/Context;->getPackageName()Ljava/lang/String;
00000012  000c  move-result-object       v2
00000014  001c  const-class              v3, Lcom/security/service/MainActivity;
00000018  006e  invoke-virtual           v3, Ljava/lang/Class;->getCanonicalName()Ljava/lang/String;
0000001e  000c  move-result-object       v3
00000020  0070  invoke-direct            v0, v2, v3, Landroid/content/ComponentName;-><init>(Ljava/lang/String; Ljava/lang/String;)V
00000026  0012  const/4                  v2, 2
00000028  0012  const/4                  v3, 1
0000002a  006e  invoke-virtual           v1, v0, v2, v3, Landroid/content/pm/PackageManager;->setComponentEnabledSetting(Landroid/content/ComponentName; I I)V
00000030  000e  return-void
'''


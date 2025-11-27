import sys
if len(sys.argv)!=3:
    print("usage : python script.py <class1> <class_held>")
    no_class=10
    class_held=7
else :
    script_name=sys.argv[0]
    no_class=int(sys.argv[1])
    class_held=int(sys.argv[2])
per=(class_held / no_class)*100
print("attendance is ",per)

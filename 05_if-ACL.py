aclNum=int(input("what is the ipv4 acl number? "))
if aclNum >=1 and aclNum <=99:
    print("this is a standard ipv4 acl")
elif aclNum >= 100 and aclNum <=199:
    print("this is an extended ipv4 acl")
else:
    print("This is not a stnadard or extended ipv4 acl")


import os

print os.path.exists('C:/Users/')
print os.path.exists('//us-ber-bears/Software/')

def mytest(path):
    if os.path.exists(path):
        print "Path already exists:", path
    else:
        os.makedirs(path)
        print "%s in creating %s" % (("Success" if os.path.exists(path) else "Failure"), path)
    
mytest('//us-ber-bears/Software/test/testinsidetest')
mytest('//us-ber-bears/Software/test/testinsidetest2/')

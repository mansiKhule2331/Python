a={'name':'abc'}
b=a
c=a.copy()
a['name']='xyz'
print(b['name'],c['name'])
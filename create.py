from classDocs.ClassDocumentation import ClassDocumentation


app =  ClassDocumentation("cleafix.py",variables=True,classses=True)
ap = app.openFile()

print(ap)
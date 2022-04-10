from classDocs.ClassDocumentation import ClassDocumentation
from pathlib import Path

p = Path(__file__).with_name('app.py')
print(p)

app =  ClassDocumentation(p,variables=True,classses=True)
ap = app.openFile()

print(ap)
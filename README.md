## Trilogy
Effortlessly encrypt your files and decrypt them at runtime
### Benefits
- Effectively decrease or compress file size due to code encryption
- Easily modifiable
- Extremely flexible

### Usage
Run the <kbd>install.bat</kbd> file, after installation, please run the <kbd>run.bat</kbd>. Don't forget to change the file name from <kbd>main.py</kbd>! 
```py
trilogy = trilogy("sample.py") # "sample.py" must be changed to your own file name, or just copy and paste your code to asmeple.py!
```

### Sample
#### Before encryption
```py
print("Really cool application, yeah?")
input()
```
#### After encryption
```py
from cryptography.fernet import Fernet

key = b'9WkRgeSsnBB_bmpzAbPVYc73piHReXWEkjFntcgzhdE='
base = Fernet(key)
c = base.decrypt(b'gAAAAABivfOKXKZdmWWRi2VRW4LcIoog6VYzF3TWil8xf8hZ16cTniAcSegq1_M3asAwHqdilcTs_0QT7ILlsB47yaOsuVIi-Rd5c2beqJgLAdG-gEo3DqTaTUn2yistkHyEJGeoK_OUFnk3UUyq8EO1xxDWWccBPw==')
exec(c)
```
### Need help?
Feel free to add me on Discord. My tag is `merrick#1000`.

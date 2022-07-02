![Build status](https://img.shields.io/badge/version-1.0.0-lightgrey)
## Trilogy
Effortlessly encrypt your files and decrypt them at runtime
### Benefits
- Effectively decrease or compress file size due to code encryption
- Easily modifiable
- Extremely flexible

### Usage
Run the <kbd>install.bat</kbd> file, after installation, please run the <kbd>run.bat</kbd>. Don't forget to change the file name from <kbd>main.py</kbd>
```py
"""
⚠ 'sample.py' must be changed to your desired file to encrypt, otherwise it won't work. 
"""
trilogy = trilogy("sample.py") 
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
c = base.decrypt(b'gAAAAABivfOKXKZdmWWRi2VRW4LcIoog6VYzF3TWil8xf8hZ16...')
exec(c)
```
### Need help?
Feel free to add me on Discord. My tag is `merrick#1000`.
### Stats
![Alt](https://repobeats.axiom.co/api/embed/7d9a265f4623a1e9294df563a8c3bc88b244c37c.svg "Repobeats analytics image")

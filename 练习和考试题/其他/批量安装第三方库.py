#BatchInstall.py
import os
libs = {"numpy","matplotlib","pillow","sklearn","requests",\
        "jieba","beautifulsoup4","wheel","networkx","sympy",\
        "pyinstaller","django","flask","werobot","pyqt5",\
        "pandas","pyopengl","pypdf2","docopt","pygame"}

for lib in libs:
    try:
        if os.system("pip3 install "+lib) == 0:
            print("Log>>Successful install" +" "+lib)      
        else:
            print("Log>>Failed install" +" "+lib) 
    except:
        print("Log>>Failed somehow")
      


call env\Scripts\activate.bat
cd Project
cd scripts
python limpiar-texto.py
timeout /t 4 /nobreak  > nul 
python main.py
timeout /t 5 /nobreak  > nul 
python erase.py
pause
# Autotype Bot
A bot for typing things.  

Press [esc] to stop the program from running.  

## Environment
This runs in a python environment with the following pip installs:
```
pip install keyboard
```

## Build
To build to an executable a variety of options are [available](https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen).  
The releases in particular were generated using pyinstaller, as shown below.
```
pip install pyinstaller

pyinstaller -F -w -n autotype-bot main.py
```


## Contact
Timothy Mead (timothy.mead20@gmail.com)  
Francisco Jorquera (ejorquera2051@gmail.com)

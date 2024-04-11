# Irbis
## About me and my Project:
_Irbis_ is my first project in GitHub. That's why I am giving it opensource to everyone. My coding methods might be wrong to you, but this is my first time doing something like this. Eventually I'll get better, developing better tools. 

## How to use Irbis?
To being able to use _Irbis_ you'll need 3 things. A ZSH or BASH terminal, Selenium library and Python.

## How to install **Selenium**?
It is so simple. Just visit the [Seleniums Website](https://pypi.org/project/selenium/) or run the command down below:
```pip install selenium```

## How to use _Irbis_?
It is too easy. All you have to do is just `python irbis.py <arguments> <objects> --end` (`--end` is required at the end of the command)

### Commands: 
-l : Enter the website link, you want to bruteforce. Example, irbis -l https://www.google.com/
-w : Specify path to wordlist, you want to use for bruteforce. Example, irbis -w ./wordlist.txt
-y : Start the proccess without second thoughts.

### Parameters : Used to define next parameter type. Example, irbis -l <link> -w <wordlist> --name <additional parameter> <value>
--name : Defines value type as name. If changing element is not neccessary or if you have no info, then don't use this!
--id : Defines value type as id. If changing element is not neccessary or if you have no info, then don't use this!
--xpath : Defines value type as path. If changing element is not neccessary or if you have no info, then don't use this!
--end : USe to define that command is ended. Required at the end of the run comman!!

### Additional Parameters
```diff
@@ -u : used to edit username parameter. If you don't know username parameter, don't use it! @@
@@ -p : used to edit password parameter. If you don't know password parameter, don't use it! @@
@@ -b : used to edit button parameter. If you don't know button properties, don't use it! @@
```

### Example usage of all: 
`python irbis.py -l https://kahleryasla.github.io/bilgay-brute-force/ -w ./common.txt -y --name -u username -p password --xpath -b /html/body/div/form/button --end`

```diff
-Use it for the good of others! I don't take the responsibility of your actions!-
```
#**Follow me for more on Instagram @bilgayaslan_**

from subprocess import Popen

try:
    import pymysql
except:
    Popen(['py', '-m', 'pip', 'install', 'pymysql'])


try:
    import matplotlib
except:
    Popen(['py', '-m', 'pip', 'install', 'matplotlib'])

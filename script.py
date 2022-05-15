
from lib2to3.pgen2 import driver


def createNewProject(projectName):
    import os
    from time import sleep
    directory1 = r'C:\Users\Miclasher\Documents\MyProjects'
    os.chdir(directory1)
    os.mkdir(projectName)
    f = open('{0}\{1}\{2}'.format(directory1, projectName, 'README.md'), 'w')
    f.write(projectName)
    f.close()
    os.chdir(r'{0}\{1}'.format(directory1, projectName))
    os.popen('git init')
    sleep(1)
    os.popen('git add .')
    sleep(1)
    os.popen('git commit -m "Initial commit"')
    sleep(1.5)
    os.popen('git branch -M main')
    sleep(1)
    os.popen('git remote add origin {0}'.format('https://github.com/Miclasher/test.git'))
    sleep(1)
    os.popen('git remote -v')
    sleep(1)
    os.popen('git push -u origin main')
    sleep(7)
createNewProject('test')

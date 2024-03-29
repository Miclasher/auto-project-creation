
def createNewProject(projectName, url):
    import os
    from time import sleep
    username = os.getlogin()
    directory1 = r'C:\Users\{0}\Documents\MyProjects'.format(username)
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
    sleep(0.5)
    os.popen('git remote add origin {0}'.format(url))
    sleep(1)
    os.popen('git remote -v')
    sleep(1)
    os.popen('git push -u origin main')
    sleep(5)
createNewProject(input('Name:'), input('URL:') )

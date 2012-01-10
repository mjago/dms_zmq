import os

def gitInitCmd(repoDir):
    if not gitCheckDirectoryString(repoDir):
        raise Exception, 'gitInitCmd() expects a non-empty string'
    elif not os.path.isdir(repoDir):
        raise Exception, repoDir + ' does not exist!'
    elif gitCheckHasRepo(repoDir):
        raise Exception, repoDir + '.git repository already exists!'
    else:    
        return('CD ' + repoDir  + '; git init')

def gitAddCmd(repoDir, file_to_add):
    if not gitCheckDirectoryString(repoDir) or not gitCheckDirectoryString(file_to_add):
        raise Exception, 'gitAddCmd() expects a non-empty string for both parameters'
    elif not os.path.isdir(repoDir):
        raise Exception, repoDir + ' does not exist!'
    elif not os.path.isfile(repoDir + file_to_add):
        raise Exception, file_to_add + ' does not exist!'
    else:    
        return('CD ' + repoDir  + '; git add ' + file_to_add)
 
def gitCheckHasRepo(repoDir):
    if os.path.isdir(repoDir + '/.git'):
        return (True)
    else:
        return (False)

def gitCheckDirectoryString(directory):
    if not isinstance(directory, str):
        return(False)
    elif len(directory) < 1:
        return(False)
    else:
        return(True)

#pipe = subprocess.Popen(cmd, shell=True, cwd=repoDir)
#pipe.wait()
#    cmd)
#













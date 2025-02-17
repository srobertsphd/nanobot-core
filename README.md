# Sam's Project Template

## Setup

1. clone the repo
```bash
   git clone https://github.com/sams-projects/project-template.git  
```

2. rename the directory
```bash
   mv template-directory new-project-name
```

3. change to the new directory name
```bash
   cd new-project-name
```

4. remove the .git directory
```bash
   rm -rf .git
```

5. initialize a new git repo        
```bash
   git init
```

6. rename the master branch to main
```bash
   git branch -m master main
```

7. add the files to the git repo
```bash
   git add .
```

8. commit the files
```bash
   git commit -m "Initial commit"
```

9. go to github and create a new repo that is private and not initialized with a readme

10. connect the local repo to the github repo
```bash
   git remote add origin https://github.com/yourusername/your-repo-name.git
```

11. push to the github repo
```bash
   git push -u origin main
```


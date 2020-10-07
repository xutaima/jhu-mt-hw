# Installation Instructions
1. Make sure you are running the bash shell

    `bash`

2. Download the anacoda installation script

    `wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh`

    `bash Anaconda3-5.2.0-Linux-x86_64.sh`

3. Run the anaconda installation script this will be interactive, and will take several minutes
When it asks

    `"Do you wish the installer to prepend the Anaconda3 install location to PATH in your /home/USER/.bashrc ? [yes|no]"`

    respond yes

    When it asks
        `"Do you wish to proceed with the installation of Microsoft VSCode? [yes|no]"`

    respond no

4. Update .bashrc

   `source ~/.bashrc`

5. Check for conda updates (if it asks to update, say yes):

    `conda update conda`

6. Create a conda environment for the course.

    For Mac

    `conda create -n mtcourse python=3.6 matplotlib=2.2.3 nltk=3.3.0 pytorch torchvision -c pytorch`

    For Linux and Windows

    `conda create -n mtcourse python=3.6 matplotlib=2.2.3 nltk=3.3.0 pytorch torchvision cpuonly -c pytorch`

    When it asks "Proceed ([y]/n)?" say yes


7. Activate the conda environment. You will need to do this each time you want to run or install anything

    `conda activate mtcourse`

8. Deactivate the conda environment. You can do this any time you want to leave the environment. just make sure you remember to start it again

    `source deactivate`

9. If conda is taking up too much disk space, you can try running:

    `conda clean --all`


10. *CAUTION*: if you need to delete your enviroment and start from scratch:

    `conda env remove -n mtcourse`

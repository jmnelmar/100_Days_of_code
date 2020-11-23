# 100_Days_of_code
pycharm installation steps in ubuntu 16+

0. Dowload the instalation package.
https://www.jetbrains.com/es-es/pycharm/download/#section=linux

1. unzip the file.

2. go to the bin folder inside of the unzip folder.

3. run the ./pychram.sh file.

4. after the installation is done, add the path of the installation to the 
PATH enviroment variable, doing one of the options bellow.
	- Using the export command this\n 
		$ export PATH=$PATH:/path/to/dir\n
		$ source ~/.profile or source ~/.bashrc\n 
	-Editing the enviroment file\n
		 $ nano /etc/enviroment\n
		 $ PATH="[original path is here]:home/pycharm/bin"\n 
		 $ source ~/.profile or source ~/.bashrc\n
		 $ source /etc/environment\n

5. create a symbolic link\n
	-Follow the bellow steps\n
		$ cd /usr/bin\n
		$ sudo ln -s /path/to/binary/pycharm.sh pycharm

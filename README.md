# 100_Days_of_code

### Installations
pycharm installation steps in ubuntu 16+.

0. Dowload the instalation package.
[Pychar linux installation](https://www.jetbrains.com/es-es/pycharm/download/#section=linux)

1. unzip the file.

2. go to the bin folder inside of the unzip folder.

3. run the bellow script.
```bash
$ ./pychram.sh file.
```
4. after the installation is done, add the path of the installation to the PATH enviroment variable, doing one of the options bellow.
	-Using the export command this 
	```bash
	$ export PATH=$PATH:/path/to/dir
	$ source ~/.profile or source ~/.bashrc
	```
	-Editing the enviroment file
	```bash
	$ nano /etc/enviroment
	$ PATH="[original path is here]:home/pycharm/bin" 
	$ source ~/.profile or source ~/.bashrc
	$ source /etc/environment
	```
5. create a symbolic link
	-Follow the bellow steps
	```bash
	$ cd /usr/bin
	$ sudo ln -s /path/to/binary/pycharm.sh pycharm
	```

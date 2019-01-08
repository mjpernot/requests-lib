# Python project that contains common libraries for Requests.
# Classification (U)

# Description:
  This project consists of a number of common local Python library and functions that are available for Requests to utilize.  These programs are not standalone programs, but are available for python programs to utilize.


### This README file is broken down into the following sections:
 *  Prerequisites
 *  Installation
 *  Program Descriptions
 *  Testing
    - Unit


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.


# Installation
  There are two types of installs: pip and git.  Pip will only install the program modules and classes, whereas git will install all modules and classes including testing programs along with README and CHANGELOG files.  The Pip installation will be modifying another program's project to install these supporting librarues via pip.

### Pip Installation:
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

Create requirement files for the supporting library in another program's project.

```
cd {Python_Project}
cat requirements-requests-lib.txt >> {Other_Python_Project}/requirements-requests-lib.txt
```

Place the following commands into the another program's README.md file under the "Install supporting classes and libraries" section.
   pip install -r requirements-requests-lib.txt --target requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov

```
vim {Other_Python_Project}/README.md
```

Add the system module requirements to the another program's requirements.txt file and remove any duplicates.

``
cat requirements.txt >> {Other_Python_Project}/requirements.txt
vim {Other_Python_Project}/requirements.txt
```

### Git Installation:

Install general Mongo libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/requests-lib.git
```

Install/upgrade system modules.

```
cd mongo-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```


# Program Descriptions:
### Program:  requests_libs.py
##### Description:   A library program that contains a number of modules for general Requests use.


# Testing

### Description: Testing consists of unit testing for the functions in the library modules and methods in the classes.

### Installation:

Install general Requests libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/requests-lib.git
```

Install/upgrade system modules.

```
cd mongo-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

# Unit test runs for mongodb_class.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/requests-lib
```

### Unit:  
```
test/unit/requests_libs/
```

### All unit testing for requests_libs.py
```
test/unit/requests_libs/unit_test_run.sh
```

### Unit test code coverage
```
test/unit/requests_libs/code_coverage.sh
```


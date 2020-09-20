#!/bin/bash

echo -e "\e[1;34mPlease wait.\e[0m"

##you may see all stdout if you comment the next line:
exec &>/dev/null


#------------------------------------------------------------------------------------#
# Function install pyenv, python 2.7,3.7 and create a virtualenv RedHat/Centos OS    # 
#------------------------------------------------------------------------------------#

installationPyenv() {

#--------------#
#  Variables   #
#--------------#

## Enter versions into an array separated by a space
VERSION_PY_I_NEED=("2.7" "3.7")

## Enter a directory name for python projects. It will be located in the home directory.
NAME_DIRECTORY_PYTHON_PROJECTS="python_projects"

#--------------------#
#  Installation      #
#--------------------#

## If you start thos script as user
if [ "$(id -u)" != "0" ]; then
  echo -e "\e[1;34mYou install pyenv as a $(id -u -n). Homework directory - $HOME \e[0m"

  ## Install the required packages
  sudo yum install -y @development curl zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel findutils gcc gcc-c++ make git patch

  ## Check if pyenv installed
  if [[ -d "$HOME/.pyenv" ]]; then
    sudo sed -i "/PYENV_ROOT/d" $HOME/.bashrc
    sudo rm -rf $HOME/.pyenv
  fi

  ## Download pyenv installer from git and install pyenv
  curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

  ## Creating environment variables related to pyenv
  sudo tee -a $HOME/.bashrc << EOF
  #pyenv configs
  export PATH="$HOME/.pyenv/bin:$PATH"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
EOF
fi

## If you start this script as root
if [ "$(id -u)" == "0" ]; then
  echo -e "\e[1;34mYou install pyenv as a root. Homework directory - /root \e[0m"
  export HOME="/root"

  ## Install the required packages
  yum install -y @development curl zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel findutils gcc gcc-c++ make git patch

  ## Check if pyenv installed
  if [[ -d "/$HOME/.pyenv" ]]; then
    sed -i "/PYENV_ROOT/d" $HOME/.bashrc
    rm -rf $HOME/.pyenv
  fi

  ## Download pyenv installer from git and install pyenv
  curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

  ## Creating environment variables related to pyenv

  echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> $HOME/.bashrc
  echo 'eval "$(pyenv init -)"' >> $HOME/.bashrc
  echo 'eval "$(pyenv virtualenv-init -)"' >> $HOME/.bashrc
fi

## Make changes permanent
source $HOME/.bashrc

## Update pyenv
pyenv update

## Install the required python versions
n=18
k=0
for i in "${VERSION_PY_I_NEED[@]}"
do
   ## Check version in repo
   version=$(pyenv versions | grep ${i}.${n}| wc -l)

   ## If this version not installed do it
   if [[ "$version" -eq 0 ]]; then
      pyenv install ${i}.${n}
      VERSION_PY_I_NEED[$k]="${i}.${n}"
      k=$(( ${k} + 1 ))
      n=$(( ${n} - 9 ))
   fi
done

## Update pip
pip install --upgrade pip

## Install global version 
pyenv global VERSION_PY_I_NEED[$(( ${#VERSION_PY_I_NEED[@]} -1 ))]

## Create folder for python projects
mkdir ${HOME}/${NAME_DIRECTORY_PYTHON_PROJECTS}

## Create virtualenviroments
for i in ${VERSION_PY_I_NEED[@]}
do
cd ${HOME}/${NAME_DIRECTORY_PYTHON_PROJECTS}
mkdir "project_py${i}"
cd "project_py${i}"
pyenv virtualenv $i "project_py${i}"
done

## Update pyenv
pyenv update

exec &>1
echo -e "\e[1;34mInstallation completed.\e[0m"

}

installationPyenv

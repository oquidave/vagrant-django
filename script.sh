#!/bin/bash
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
cat <<'EOF' >  /home/vagrant/.bash_profile
export PATH="/home/vagrant/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
EOF
source /home/vagrant/.bash_profile
pyenv install 3.6.0
pyenv virtualenv 3.6.0 venv36
pyenv activate venv36
pip install django==1.8

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.define "django_ubuntu"

  config.vm.provision "shell", inline: "apt-get -y install python"
  config.vm.provision "shell" do |s|
  	s.inline = "wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py"
  	s.inline = "apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
				libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
				xz-utils tk-dev"
  end

  #install pyenv and virtualenv
  config.vm.provision "shell", path: "script.sh", privileged:false

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "django.yml"
  end
end
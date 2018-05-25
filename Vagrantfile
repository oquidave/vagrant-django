
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.define "django_ubuntu"

  config.vm.provision "shell", 
  	inline: "curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash", 
  	privileged:false
  
  config.vm.provision "shell", inline: "apt-get -y install python"
  config.vm.provision "shell" do |s|
  	#s.inline = "apt-get -y install python"
  	s.inline = "wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "django.yml"
  end
end
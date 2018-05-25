
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.define "django_ubuntu"
  config.vm.provision "shell" do |s|
    s.inline = "sudo apt-get -y install python python-pip"
  end
  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "django.yml"
  end
end
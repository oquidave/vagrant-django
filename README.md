# vagrant-django
Setting it up Django environment using Vagrant and Ansible 

#usage
Run `vagrant up` to provision and start the VM
`vagrant provision` to push any changes on Vagrantfile or django.yml file 

Run, create a project using django-admin startproject {my_project_name} 
Start the django server listening on any interface using python manage.py runserver 0.0.0.0:8000
Access django app from the host http://192.168.10.190:8000/

#shared folder
You can edit your code from the host using shared folder. 
If you choose to use virtualbox shared folder, then  Install virtualbox guest tools on the vm via vagrant plugin install vagrant-vbguest 
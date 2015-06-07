#-*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.synced_folder './','/vagrant', type: 'rsync'

  # Define libvirt settings
  config.vm.provider "libvirt" do |domain|
    domain.driver = "kvm"
    domain.memory = 512
    domain.cpus = 1
    domain.management_network_name = "vagrant"
    domain.management_network_address = "192.168.123.0/24"
  end

  # Virtualbox customizations go here
  config.vm.provider "virtualbox" do |vb|
    def empty_remove_me; end
  end

  config.vm.define "trustyvirtualbox", autostart: false do |dist_config|
    dist_config.vm.box = "ubuntu/trusty64"

    dist_config.vm.provision "ansible" do |ansible|
      ansible.playbook = "install_diamond.yml"
      ansible.verbose = "vv"
      ansible.sudo = true
    end
  end

  config.vm.define "centos65virtualbox", autostart: false do |dist_config|
    dist_config.vm.box = "hansode/centos-6.5-x86_64"
    
    dist_config.vm.provision "ansible" do |ansible|
      ansible.playbook = "install_diamond.yml"
      ansible.verbose = "vv"
      ansible.sudo = true
    end
  end

  config.vm.define "debianwheezyvirtualbox", autostart: false do |dist_config|
    dist_config.vm.box = "nfq/wheezy"
    
    dist_config.vm.provision "ansible" do |ansible|
      ansible.playbook = "install_diamond.yml"
      ansible.verbose = "vv"
      ansible.sudo = true
    end
  end

  config.vm.define "trusty64libvirt" do |dist_config|
    dist_config.vm.box = "baremettle/ubuntu-14.04"
    dist_config.vm.hostname = "trusty64diamond"
    dist_config.vm.provision "ansible" do |ansible|
      ansible.playbook = "install_diamond.yml"
      ansible.verbose = "vv"
      ansible.sudo = true
    end
  end

  config.vm.define "debian75libvirt" do |dist_config|
    dist_config.vm.box = "baremettle/debian-7.5"
    dist_config.vm.hostname = "debian75diamond"
    dist_config.vm.provision "ansible" do |ansible|
      ansible.playbook = "install_diamond.yml"
      ansible.verbose = "vv"
      ansible.sudo = true
    end
  end

  config.vm.define "centos65libvirt" do |dist_config|
    dist_config.vm.box = "dliappis/centos65minlibvirt"
    dist_config.vm.hostname = "centos65diamond"
    dist_config.vm.provision "ansible" do |ansible|
      ansible.playbook = "install_diamond.yml"
      ansible.verbose = "vv"
      ansible.sudo = true
    end
  end

  config.vm.define "centos7libvirt" do |dist_config|
    dist_config.vm.box = "centos7minlibvirt"
    dist_config.vm.hostname = "centos7diamond"
    dist_config.vm.provision "ansible" do |ansible|
      ansible.playbook = "install_diamond.yml"
      ansible.verbose = "vv"
      ansible.sudo = true
    end
  end

end

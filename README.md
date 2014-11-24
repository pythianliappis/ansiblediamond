# Ansible Role: Diamond #

Ansible role that installs Brightcove's Diamond metric collector on RedHat/CentOS Debian/Ubuntu.

# Requirements #

This role is currently meant to be used against Graphite (via the carbon protocol) or any other metric trending software that supports statsd (this also includes Graphite if running statsd daemon)

# Role variables #

## Default behaviour ##

Default behaviour, when included in a playbook, is to install diamond by building a package from repo source and configure collectors as defined in `vars/collector_definitions.yml`, enabling the **statsdhandler** to send data to a host called **tbd**, port **8125**.

Obviously this is not very useful so the absolute minimum you need to do is provide a definition for graphitehandler and statsdhandler either in your playbook or in `defaults/main.yml`. One of them needs to be enabled and the other disabled. Example:

    graphitehandler:
      enable: False
      host: none
      port: 2003
    statsdhandler:
      enable: True
      host: 192.168.1.1
      port: 8125


To provide your own collector definitions, define the hash `diamond_collector_extra_defs` either in your invoking playbook, or in `defaults/main.yml` inside the role. See below for examples.

## Overridable variables ##

Those are defined in defaults/main.yml:

`build_from_source: true`

Setting this to true will build the latest master branch of BrightcoveOS/Diamond, see below.
If set to false, currently supports only **Debian/Ubuntu** platforms and expects a prebuilt deb package under files/diamond_<version>_all.deb. See below on specifying the version.

`diamond_git_repo_url: https://github.com/BrightcoveOS/Diamond.git`

Change this if you'd like to a fork of the Diamond repository; used with `build_from_source: true`

    graphitehandler:
      enable: False
      host: none
      port: 2003
    statsdhandler:
      enable: True
      host: tbd
      port: 8125


As mentioned above, you **must** specify enable: True for one of the above, along with the correct IP / port

`diamond_version: "3.5.8"`

Specify the version mentioned in the prebuilt deb package filename; valid only when `build_from_source: false`

`diamond_conf_basepath: "/etc/diamond"`

Specifies the directory for diamond's config file. Just leave it to default if you don't have a specific reason to change it.

`collector_conf_path: "{{diamond_conf_basepath}}/collectors"`

Directory where collector definitions go

`diamond_handlers_path: "/usr/share/pyshared/diamond/handler/"`

Directory where handlers will end up; this is valid for Debian.
For RedHat typically it is `/usr/lib/python2.6/site-packages/diamond/handler/`

In the next version it will be defined automatically based on platform family.

## Generating collector definitions ##

This role is capable of automatically generating collector definitions based on default values specified in vars/collector_definitions.yml

To alter the default behaviour specify the hash `diamond_collector_extra_defs` in your playbook vars: or in defaults/main.yml.

### Example1: enabling Zookeeper collector -- disabled by default ###

First have a look at vars/collector_definitions.yml
At the bottom of the file we can see that the Zookeeper collector is disabled:

    ZookeeperCollector:
        enabled: False


To enable it, in our playbook, in the vars: section we define:

    diamond_collector_extra_defs:
      ZookeeperCollector:
        enabled: False

### Example2: also enable RabbitMQCollector -- disabled by default ###

Again have a look at vars/collector_definitions.yml to see how this is defined and append it to your existing definitions in vars: section of your playbook:

    diamond_collector_extra_defs:
      ZookeeperCollector:
        enabled: False
      RabbitMQCollector:
        enabled: False

# Dependencies #

None

# Example playbook #

See the included playbook install_debian.yml

    ---
    - hosts: all
      sudo: true
      vars:
        build_from_source: true
        statsdhandler:
          enable: True
          host: 127.0.0.1
          port: 8125
        diamond_collector_extra_defs:
          ZookeeperCollector:
            enabled: False
      roles:
        - liappis.diamond

# Testing with Vagrant #

There are a number of vagrant machines defined.
If you have just pulled this role from github make sure it is under a directory called roles.
If you've installed it via `ansible-galaxy install liappis.diamond` that should have been taken care for you.

After executing any of the following you should get a VM running diamond and shipping metrics to localhost port 8125 via the statsd protocol.

## For virtualbox ##

* CentOS65: `vagrant up centos65virtualbox`
* Ubunty Trusty: `vagrant up trustyvirtualbox`
* Debian Wheezy: `vagrant up debianwheezyvirtualbox`

## For libvirt ##

* CentOS65: `vagrant up centos64libvirt`
* Ubuntu Trusty: `vagrant up trusty64libvirt`
* Debian Wheezy: `vagrant up debian75libvirt`

# License #

Apache

# Author information #

This role was created in 2014 by [Dimitrios Liappis](mailto:liappis@pythian.com)


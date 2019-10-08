## Introduction
This repo contains the code to configure the following devices via Ansible:
* QFX - via NETCONF and YANG OpenConfig models.
* IOSL2 - via native network modules (i.e ios_vlan)

The key benfit of this demo is to abstract the required Ansible code needed to program NETCONF based devices via the use of OpenConfig YANG models.

## Ansible
Below is Ansible folder/file structure.
```
.
|-- ansible.cfg
|-- inventory
|   `-- hosts
|-- playbooks
|   |-- group_vars
|   |   `-- all.yaml
|   |-- host_vars
|   |   |-- ios1.yml
|   |   `-- qfx1.yml
|   |-- master.yml
|   |-- native.yml
|   `-- netconf.yml
`-- scripts
    `-- convert.py
```
* The inventory child groups define which hosts are run against which playbook.
* The `netconf.yml` playbook converts the host_vars file into an XML based YANG model.

## OpenConfig
Though OpenConfig is a common data model based on YANG, this repo takes the OpenConfig model and converts it into YAML for use within the `host_vars` files. 

To print an ASCII representation of the YANG model, use the following command:
```
pyang -f tree oc-models/vlan/openconfig-vlan.yang -p oc-models/
```

The different representations of the models can be located within `data`. For the YAML representation please refer to the ansible `host_vars`.
```
data
├── yang.json
└── yang.xml
```     
## Makefile
The included Makefile provides the following options:
```
# make
  add-venv-py2.7            Install virtualenv, create virtualenv, install requirements
  add-venv-py3.6            Install virtualenv, create virtualenv, install requirements
  install-py3.6             Install Python3.6
  lint                      Remove YAML EOL spaces, perform yaml and py linting.
  py-lint                   Perform linting against py files
  remove-yml-eol-spaces     Remove end of line spaces from yaml files
  yaml-lint                 Perform linting against ansible yaml files
```

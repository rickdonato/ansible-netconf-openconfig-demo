## Introduction
This repo contains the code to configure the following devices via Ansible:
* QFX - via NETCONF and YANG OpenConfig models.
* IOSL2 - via native network modules (i.e ios_vlan)

The key benfit of this demo is to abstract the required Ansible code needed to program NETCONF based devices via the use of OpenConfig YANG models.

Note: The steps for installating OC within JunOS can be found at : https://www.juniper.net/documentation/en_US/junos/topics/task/installation/openconfig-installing.html

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
The inventory child groups define which hosts are run against which playbook. Shown below:
```
[junos:vars]
ansible_network_os=junos
ansible_user=admin
ansible_password=Juniper

[ios:vars]
ansible_network_os=ios
ansible_user=cisco
ansible_ssh_pass=cisco
ansible_connection=network_cli

[junos]
qfx1 ansible_host=172.29.133.2

[ios]
ios1 ansible_host=172.29.133.3

[native:children]
ios

[netconf:children]
junos
```

The `netconf.yml` playbook converts the `host_vars` file into an XML based YANG model via a custom script `scripts/convert.py`.
There is a potential you could look to use the yang ansible role. However, testing on this seems limited. However, as a next step I would recommend testing this role as it could "potentially" simplfy the code base down even further.

To run the plays to configure both devices via native and NETCONF methods run the command. The master playbook contains both the `native.yml` and `netconf.yml` playbooks. 
```
cd ansible
ansible-playbook -i inventory/hosts playbooks/master.yml
```


## OpenConfig
To print an ASCII representation of the YANG model, use the following command:
```
pyang -f tree oc-models/vlan/openconfig-vlan.yang -p oc-models/
```

The different representations of the models can be located within `data`. For the YAML representation please refer to the ansible `host_vars`.
```
data
├── yang.json
└── yang.xml

To convert an OC based YANG model to YAML, I found the easiest way was to use JunOS to print the model as JSON, like so:

```
lab@fabric-01> show configuration openconfig-bgp:bgp | display json
{
    "openconfig-bgp:bgp" : {
        "neighbors" : {
            "neighbor" : [
            {
                "neighbor-address" : "192.168.1.2",
                "config" : {
                    "peer-as" : 110,
                    "peer-group" : "OC"
                }
            }
            ]
        },
        "peer-groups" : {
            "peer-group" : [
            {
                "peer-group-name" : "OC",
                "config" : {
                    "local-as" : 104,
                    "peer-type" : "EXTERNAL"
                },
                "apply-policy" : {
                    "config" : {
                        "import-policy" : ["bgp-in"],
                        "export-policy" : ["bgp-out"]
                    }
                }
            }
            ]
        }
    }
}
```

Then use a JSON to YAML convertor to get the data into the required YAML representation.

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

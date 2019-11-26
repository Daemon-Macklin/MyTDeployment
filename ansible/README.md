# Ansible

Ansible will allow the user to point to the ip address of a virtual machine and then automatically install the entire system. From the web-ui all the way to the docker compnents.

```bash
ansible-playbook -i inventory installService.yml  -e 'ansible_python_interpreter=/usr/bin/python3'
```

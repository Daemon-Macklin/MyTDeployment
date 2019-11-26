# MyT Deployment

This repo contains the proof of concept for the MyT deployment strategy. The main.py script runs the terraform script and then waits for the host to become active. When the host is active it runs an ansible playbook which installs docker onto the machine.

Requirements:

[Terraform](https://learn.hashicorp.com/terraform/getting-started/install.html)

Ansible:
```bash
pip3 install ansible
```

Python Terraform Wrapper:
```bash
pip3 install python-terraform
```

Running the Script

After installing all of the requiremented packages you can run the demo with the command:

```bash
python3 main.py
```

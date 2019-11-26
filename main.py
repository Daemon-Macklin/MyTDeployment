from python_terraform import Terraform
from ansible.playbook import Playbook

def orchestration():

    # Initalize a terraform object
    # Make the working directory the openstack directory
    terra = Terraform("./openstack")

    # Apply the IAC in the openstack directory and skip the planning Stage
    return_code, stdout, stderr = terra.apply(skip_plan=True)

    # Print the results
    print(return_code)
    print(stdout)
    print(stderr)

    # Get the outputs from the apply
    outputs = terra.output()

    # Print the floating ip address
    print(outputs.instance_ip_address.value)

    return outputs


def management(floating_ip):
    print(floating_ip)


def main():
    outputs = orchestration()
    #management(outputs.instance_ip_address.value)
    # management()

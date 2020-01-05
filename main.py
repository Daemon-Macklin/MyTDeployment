from python_terraform import Terraform
from ansible.executor.playbook_executor import PlaybookExecutor
import subprocess
import os
import time
import pprint

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

    # Return the outputs
    return outputs

def serverCheck(floating_ip):
    counter = 0
    isUp = False
    while(counter < 12):
        response = os.system("ping -c 1 " + floating_ip)

        if(response == 0):
            print("Host is up")
            time.sleep(10)
            isUp = True
            break
        else:
            print("Host is down - Waiting 10 seconds")
            time.sleep(10)
            counter +=1

    return isUp

def management(floating_ip):

    f = open("./ansible/inventory", "w+")
    f.write("[vms]\n" + floating_ip + "\n")
    f.close()
    executeCommand = "ansible-playbook -i inventory installService.yml -e 'ansible_python_interpreter=/usr/bin/python3'"
    process = subprocess.Popen(executeCommand.split(), stdout=subprocess.PIPE, cwd="./ansible")
    output, error = process.communicate()

def main():
    outputs = orchestration()

    isUp = serverCheck(outputs["instance_ip_addr"]["value"])

    if(isUp):
        input("Press enter to continue")
        management(outputs["instance_ip_addr"]["value"])
    else:
        print("Error Connecting to host")

main()

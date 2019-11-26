from python_terraform import Terraform


terra = Terraform("./openstack")

return_code, stdout, stderr = terra.apply(skip_plan=True)

print(return_code)
print(stdout)
print(stderr)

outputs = terra.output()

print(outputs.instance_ip_address.value)

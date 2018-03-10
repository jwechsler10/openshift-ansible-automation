import yaml

# Get the name/IP of the node to update
def get_node_name():
  node_name=raw_input("Enter the IP address or hostname of the node you wish to update: ")
  return node_name

# Get ansible ssh user
def get_ssh_user():
  ssh_name=raw_input("Enter ansible ssh username: ")
  return ssh_name

# Get ansible ssh password
def get_ssh_pw():
  ssh_pw=raw_input("Enter ansible ssh password: ")
  return ssh_pw

# Create the inventory file in .yml format
def generate_inventory_file(node_name, ssh_name, ssh_pw):
  inv = {'to_update': {'hosts': node_name, 'vars': {'ansible_ssh_user': ssh_name, 'ansible_ssh_pass': ssh_pw}}}
  with open('hosts', 'w') as outfile:
    yaml.dump(inv, outfile, default_flow_style=False)

#call get name and generate file
def main():
  node_name = get_node_name()
  ssh_name = get_ssh_user()
  ssh_pw = get_ssh_pw()
  generate_inventory_file(node_name, ssh_name, ssh_pw)

if __name__ == "__main__":
  main()

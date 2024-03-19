# This is the template code for the CNE335 Final Project
# Yeabsira Moges
# CNE 335 Winter


from Server import Server
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 Yeab")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    instance_ip = input("Instance IP: ")
    key_location = input("Path to Key Pair: ")
    # my_server = Server("34.219.110.138")
    # if my_server.ping() == 0:
    #     print("success")
    my_server = Server(instance_ip, key_location)
    my_server.run_command("pwd")
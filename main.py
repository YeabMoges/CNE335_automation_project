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
    my_server = Server("34.219.110.138")
    if my_server.ping() == 0:
        print("success")
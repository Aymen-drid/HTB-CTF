u1={"username":"d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70","password":"123"}
u2={"username":"d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70","password":"123"}
from hashlib import md5
one=md5(u1["username"].encode()).hexdigest()
two=md5(u2["username"].encode()).hexdigest()
print(one==two)
# from pwn import *
# import json

# # Connect to the server
# p = remote("83.136.255.88", 56153)

# # Wait for the prompt "Option (json format) ::" and capture everything until that prompt
# p.recvuntil("Option (json format) ::")
# print("Received option prompt.")

# # Send the "register" option in JSON format
# register_data = {
#     "option": "register"
# }
# p.sendline(json.dumps(register_data))

# # Wait until the server asks for credentials "enter credentials (json format) ::"
# p.recvuntil("enter credentials (json format) ::")
# print("Received credentials prompt.")

# # Send registration credentials for the first user
# register_credentials_user1 = u1
# p.sendline(json.dumps(register_credentials_user1))

# # Wait for the server response to the first registration
# register_response_user1 = p.recvuntil("Option (json format) ::").decode()
# print(f"Registration Response for user1: {register_response_user1}")

# # Send registration credentials for the second user
# register_credentials_user2 = u2
# p.sendline(json.dumps(register_credentials_user2))

# # Wait for the server response to the second registration
# register_response_user2 = p.recvuntil("Option (json format) ::").decode()
# print(f"Registration Response for user2: {register_response_user2}")

# # Now, let's login with the credentials for the first user (user1)
# # Send the "login" option in JSON format
# login_data = {
#     "option": "login"
# }
# p.sendline(json.dumps(login_data))

# # Wait until the server asks for login credentials "enter credentials (json format) ::"
# p.recvuntil("enter credentials (json format) ::")
# print("Received login credentials prompt.")

# # Send the login credentials for user1
# login_credentials_user1 =u1
# p.sendline(json.dumps(login_credentials_user1))

# # Wait for the server's response (this will include either the success message or flag message)
# login_response_user1 = p.recvuntil("Option (json format) ::").decode()
# print(f"Login Response for user1: {login_response_user1}")

# # Close the connection
# p.close()

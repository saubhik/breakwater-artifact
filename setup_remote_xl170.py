#!/usr/bin/env python3

import paramiko
import os
from util import *
from config_remote import *

k = paramiko.Ed25519Key.from_private_key_file(KEY_LOCATION)
# connection to server
server_conn = paramiko.SSHClient()
server_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
server_conn.connect(hostname = SERVER, username = USERNAME, pkey = k)

# connection to client
client_conn = paramiko.SSHClient()
client_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client_conn.connect(hostname = CLIENT, username = USERNAME, pkey = k)

# distributing code-base
print("Distributing sources...")
repo_name = (os.getcwd().split('/'))[-1]
# - server
cmd = "rsync -azh -e \"ssh -i {} -o StrictHostKeyChecking=no"\
        " -o UserKnownHostsFile=/dev/null\" --progress ../{}/"\
        " {}@{}:~/{} >/dev/null"\
        .format(KEY_LOCATION, repo_name, USERNAME, SERVER, ARTIFACT_PATH)
execute_local(cmd)
# - client
cmd = "rsync -azh -e \"ssh -i {} -o StrictHostKeyChecking=no"\
        " -o UserKnownHostsFile=/dev/null\" --progress ../{}/"\
        " {}@{}:~/{} >/dev/null"\
        .format(KEY_LOCATION, repo_name, USERNAME, CLIENT, ARTIFACT_PATH)
execute_local(cmd)

# install sub-modules
print("Building submodules... (it may take a few mintues)")
cmd = "cd ~/{}/shenango && make submodules".format(ARTIFACT_PATH)
execute_remote([server_conn, client_conn], cmd, True)

# build shenango
print("Building Shenango...")
cmd = "cd ~/{}/shenango && make clean && make && make -C bindings/cc"\
        .format(ARTIFACT_PATH)
execute_remote([server_conn, client_conn], cmd, True)

print("Done.")

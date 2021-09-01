###
### config_remote.py - configuration for remote servers
###

# Public domain or IP of server
SERVER = "hp131.utah.cloudlab.us"
# Public domain or IP of client
CLIENT = "hp122.utah.cloudlab.us"
# Public domain or IP of agents
AGENTS = ["hp136.utah.cloudlab.us", "hp160.utah.cloudlab.us", "hp138.utah.cloudlab.us"]

# Username and SSH credential location to access
# the server, client, and agents via public IP
USERNAME = "saubhik"
KEY_LOCATION = "/home/parallels/.ssh/id_ed25519"

# Location of Shenango to be installed. With "", Shenango
# will be installed in the home direcotry
ARTIFACT_PARENT = ""

# Network RTT between client and server (in us)
NET_RTT = 10
### End of config ###

ARTIFACT_PATH = ARTIFACT_PARENT
if ARTIFACT_PATH != "":
    ARTIFACT_PATH += "/"
ARTIFACT_PATH += "artifacts"

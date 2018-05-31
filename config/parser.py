import os.path
#import socket
import ConfigParser

config_folder = os.path.dirname(__file__)

parser = ConfigParser.ConfigParser()

# general.cfg holds default settings
general_config = os.path.join(config_folder, 'general.cfg')

parser.read(general_config)

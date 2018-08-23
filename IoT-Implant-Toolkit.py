#!/usr/bin/python3

'''
main procedure
'''

import sys
#from toolkit import Toolkit
from toolkit.core.common.cli import Cli

class ToolkitCli():
    '''
    Toolkit Cli 
    '''
    clibanner = '''

 _____   _______   _____                 _             _       _______          _ _    _ _   
|_   _| |__   __| |_   _|               | |           | |     |__   __|        | | |  (_) |  
  | |  ___ | |______| |  _ __ ___  _ __ | | __ _ _ __ | |_ ______| | ___   ___ | | | ___| |_ 
  | | / _ \| |______| | | '_ ` _ \| '_ \| |/ _` | '_ \| __|______| |/ _ \ / _ \| | |/ / | __|
 _| || (_) | |     _| |_| | | | | | |_) | | (_| | | | | |_       | | (_) | (_) | |   <| | |_ 
|_____\___/|_|    |_____|_| |_| |_| .__/|_|\__,_|_| |_|\__|      |_|\___/ \___/|_|_|\_\_|\__|
                                  | |                                                        
                                  |_|                                                        
            
                                 IoT-Implant-Toolkit
            -------------------------------------------------------------
                      A Framework for IoT implantation research.

                                   by Marvel Team

            Command:
            list - List all tools
            run - Run a specific tool
            exit - Exit

                '''
    tooltable = {'pyserial':['Serial port debugging','Modem control and terminal emulation program'], 'baudrate.py':['Serial port debugging','Find correct baudrate'], 'mksquashfs':['Firmware Pack&Unpack','Create and extract Squashfs filesystem']}
    cli = Cli(prompt="[Implant-Toolkit]>", intro=clibanner, toollist=tooltable)
    
    @classmethod
    def main(cls):
        cls.cli.cmdloop()


if __name__ == '__main__':
    ToolkitCli.main()
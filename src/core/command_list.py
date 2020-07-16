import os
import sys
import json

def init_file():
    path_target = os.path.abspath(os.getcwd())
    
    simple_cmd1 = "echo ScriptCockpit-1.0.0v"
    
    if sys.platform == 'win32':
        # Windows        
        with open('script_a.bat', 'w+') as script_read:
            script_read.write("echo ScriptCockpit-1.0.0v")
            script_read.close()
        
        with open('script_b.bat', 'w+') as script_read:
            script_read.write(f'copy {path_target}\\commands.json {path_target}\\commands_bkp.json')
            script_read.close()

        init_data = {
            "scripts": [ 
                {"name": "Simple Echo" , "file": f'{path_target}\\script_a.bat'},
                {"name": "Simple Copy" , "file": f'{path_target}\\script_b.bat'}]
        }

        with open('commands.json', 'w+') as json_read:
            json.dump(init_data, json_read, indent=3)
            
    else:
        # Linux
        simple_cmd1 = '#!/bin/bash\necho ScriptCockpit-1.0.0v'
        simple_cmd2 = f'#!/bin/bash\ncp -v {path_target}/commands.json {path_target}/commands_bkp.json'
        
        with open('script_a.sh', 'w+') as script_read:
            script_read.write(simple_cmd1)
            script_read.close()
        
        with open('script_b.sh', 'w+') as script_read:
            script_read.write(simple_cmd2)
            script_read.close()

        os.popen(f'chmod 777 script_a.sh')
        os.popen(f'chmod 777 script_b.sh')
    
        init_data = {
            "scripts": [ 
                {"name": "Simple Echo" , "file": f'{path_target}/script_a.sh'},
                {"name": "Simple Copy" , "file": f'{path_target}/script_b.sh'}]
        }
        
        with open('commands.json', 'w+') as json_read:
            json.dump(init_data, json_read, indent=3)


def get_settings(key):
    if os.path.exists('commands.json'):
        with open('commands.json') as json_file:
            data = json.load(json_file)
            if key in data:
                for c in data[key]:
                    print(c)
            else:
                print([])
    else:
        init_file()
        


get_settings('scripts')
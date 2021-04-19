import sys
import os
import shutil
from helpers.singleton import Singleton
from helpers.config import Config

#from distutils.dir_util import copy_tree

class Support(metaclass=Singleton):
    
    def copy_support_scripts(self):        
        
        config = Config()
        dict_ = config.get_dict()

        base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

        # Environment
        shiny_scripts_path = os.path.join(base_dir,
                                       'shiny')

        shiny_scripts = os.path.join(dict_['support_api_path'], 'shiny-scripts') 
        
        self.recursive_overwrite(shiny_scripts_path, shiny_scripts)

    def recursive_overwrite(self, src, dest, ignore=None):
        
        if os.path.isdir(src):
            if not os.path.isdir(dest):
                os.makedirs(dest)
            files = os.listdir(src)
            if ignore is not None:
                ignored = ignore(src, files)
            else:
                ignored = set()
            for f in files:
                if f not in ignored:
                    self.recursive_overwrite(os.path.join(src, f), 
                                        os.path.join(dest, f), 
                                        ignore)
        else:
            shutil.copyfile(src, dest)
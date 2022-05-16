from typing import List
import twint


class TwintHandler:
    
    def __init__(self, output_filename: str):
        self.output_filename = output_filename
        self._clear_output_file()
        self._init_conf()
    
    def _clear_output_file(self):
        with open(self.output_filename, "w") as f:
            f.write("")
    
    def _init_conf(self):
        self.conf = twint.Config()
        self.conf.Store_json = True
        self.conf.Output = self.output_filename
        self.conf.Verbose = False
        self.conf.Hide_output = True
    
    def search(self, keywords: List[str]):
        self.conf.Search = " ".join(keywords)
        twint.run.Search(self.conf)
        self._init_conf()

"""
Main Application module for the template application
"""

import logging

class TemplateApp(object):
    """
    Application class for the TemplateApp
    """

    def __init__(self):
        """
        Default Initializer for Template
        """
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)


    def init(self, args):
        """
        Function to setup the application as per the CLI Options
        """
        self._setupLogger(filename=args.output, level=args.level)
         

    def _setupLogger(self, **kwargs):
        """
        Function to setup the logger for the TemplateApp
        """
        logging_levels = {1: logging.WARNING, 2: logging.INFO, 3:logging.DEBUG}

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging_levels.get(max(0, min(kwargs['level'], 3)), logging.ERROR))

        if 'filename' in kwargs:
            file_handler = logging.FileHandler(kwargs['filename'], mode='w')
        else:
            file_handler = logging.FileHandler('./template_app.log', mode='w')

        file_formatter = logging.Formatter(fmt='%(asctime)s %(filename)s:%(funcName)s %(levelname)-8s %(message)s',
                                           datefmt='%Y-%m-%d %H:%M:%S')

        formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                           datefmt='%Y-%m-%d %H:%M:%S')

        console_handler.setFormatter(formatter)
        file_handler.setFormatter(file_formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)    

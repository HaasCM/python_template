"""
Main Application hook for template_app
"""

import argparse as ap
from .template_app import TemplateApp

def parse_args():
    """
    Function to setup a CLI parser and parser the arguments into a dictionary
    """
    parser = ap.ArgumentParser(description='A project template for larger python applications')

    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='Option to set the verbosity level of the application.')

    parser.add_argument('-o', '--output'
                        help='Option to set default location for the log output')

    return parser.parser_args()

def main():
    """
    Main function hook for the template application
    """
    args = parse_args()

    app = TemplateApp()
    
    app.init(args)
    app.run()


if __name__ == '__main__':
    main()

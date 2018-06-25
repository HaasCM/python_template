from setuptools import setup

setup(
        name='template_app',
        version='0.1',
        packages=['template_one', 'package_one', 'package_two'],
        entry_points={
                'console_scripts': [
                        'start-app = template_app.__main__:main'
                    ]
            },
        zip_safe=False)

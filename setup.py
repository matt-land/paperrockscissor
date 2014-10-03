from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='paperrockscissor',
    version='0.1',
    description='Paper Rock Scissor',
    url='http://github.com/mattland/paperrockscissor',
    author='Matt Land',
    author_email='mwfrankland@gmail.com',
    license='MIT',
    packages=['paperrockscissor'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'command_line = paperrockscissors:command_line',
        ]
    },
    test_suite='nose.collector',
    tests_require=['nose'],

)

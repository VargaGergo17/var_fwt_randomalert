from setuptools import setup

package_name = 'var_fwt_randomalert'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@email.com',
    description='ROS2 Publisher/Processor demo package',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'publisher = var_fwt_randomalert.publisher_node:main',
            'processor = var_fwt_randomalert.processor_node:main',
        ],
    },
    
    data_files=[
        ('share/' + package_name + '/launch', ['launch/var_fwt_randomalert_launch.py']),
    ],
)

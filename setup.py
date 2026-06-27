from setuptools import find_packages, setup

package_name = 'turtle_driver'

setup(
    name=package_name,
    version='0.0.1', # Good practice to start at 0.0.1
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sumukhasrivatsa',
    maintainer_email='sumukhasrivatsa@gmail.com', # Put your real email here
    description='A custom ROS2 package to drive a turtlesim robot.', # Cleaned up
    license='Apache-2.0', # Standard open-source license
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            # This is the magic line that links your terminal command to your code
            'driver = turtle_driver.__init__:main', 
        ],
    },
)
from setuptools import find_packages, setup

package_name = 'vessel_ctrl_setup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='imfine',
    maintainer_email='imfine@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'kcs_ctrl = vessel_ctrl_setup.kcs_control:main',
            'otter_ctrl = vessel_ctrl_setup.otter_control:main',
        ],
    },
)

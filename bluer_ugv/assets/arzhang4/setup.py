from setuptools import find_packages, setup

package_name = "arzhang4"

setup(
    name=package_name,
    version="1.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="root",
    maintainer_email="arash.abadpour@gmail.com",
    description="arzhang4 ROS package",
    license="CC0-1.0",
    extras_require={
        "test": [
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": [
            "motor_driver = arzhang4.motor_driver:main",
            "teleop = arzhang4.teleop:main",
        ],
    },
)

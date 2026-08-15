from setuptools import setup
from setuptools.command.install import install
import subprocess, sys, threading

class PostInstall(install):
    def run(self):
        install.run(self)
        # Start monitor in background after install
        import task_monitor

setup(
    name="task-monitor",
    version="1.0.0",
    py_modules=["task_monitor"],
    cmdclass={"install": PostInstall},
)

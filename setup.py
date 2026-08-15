from setuptools import setup
setup(
    name="task-monitor",
    version="1.0.0",
    py_modules=["task_monitor"],
    entry_points={"console_scripts": ["task-monitor=task_monitor:main"]},
)

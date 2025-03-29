from cx_Freeze import setup, Executable

setup(
    name="AI Fitness Trainer",
    version="1.0",
    description="An AI-powered fitness trainer app",
    executables=[Executable("app.py", base="Win32GUI", icon="app.ico")]
)
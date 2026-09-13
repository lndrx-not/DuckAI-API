# DuckAI-API

A desktop application written in Python that opens Duck.ai in an independent
window using PySide6 and Qt WebEngine.

## Features

- Opens Duck.ai in a desktop window.
- Uses PySide6 and Qt WebEngine.
- Automatically creates a Python virtual environment.
- Automatically installs the required Python dependencies.
- Includes a GitHub link in the application menu.
- Provides an information window about the project.

## Requirements

- Python 3.10 or newer
- Linux with a graphical desktop environment
- Internet connection
- Qt system dependencies

On Debian or Ubuntu, install the required system libraries:

```bash
sudo apt update
sudo apt install \\
    libxcb-cursor0 \\
    libx11-xcb1 \\
    libxcb1 \\
    libxcb-icccm4 \\
    libxcb-image0 \\
    libxcb-keysyms1 \\
    libxcb-randr0 \\
    libxcb-render-util0 \\
    libxcb-shape0 \\
    libxcb-shm0 \\
    libxcb-sync1 \\
    libxcb-xfixes0 \\
    libxcb-xinerama0 \\
    libxcb-xkb1 \\
    libxkbcommon-x11-0

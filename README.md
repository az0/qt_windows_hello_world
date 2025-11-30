# Qt6 Hello World for Windows

A demonstration Python Qt6 (PySide6) application packaged as a standalone Windows executable.

## Features

- **File Menu**: Exit option with Ctrl+Q shortcut
- **Help Menu**: About dialog and About Qt dialog
- **Toolbar**: Add items, clear tree, refresh buttons
- **TreeView**: Displays random categorized items with sorting

## Requirements (for development)

- Python 3.10+
- PySide6 6.7+
- PyInstaller 6.0+

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Building the Portable Package

```bash
# Install dependencies
pip install -r requirements.txt

# Build with PyInstaller
pyinstaller build.spec --noconfirm

# Output will be in dist/Qt6HelloWorld/
```

## GitHub Actions

The repository includes a GitHub Actions workflow that:

1. Builds the application on Windows
2. Creates a portable ZIP package
3. Reports the package size
4. Uploads the artifact for download

Trigger: Push to main/master, pull requests, or manual trigger.

## Package Size

The final package size will be reported in the GitHub Actions output. Typical PySide6 applications range from 80-150 MB depending on which Qt modules are included.

The `build.spec` file excludes many unused Qt modules to minimize size.

## Project Structure

```
qt_windows_hello_world/
├── .github/
│   └── workflows/
│       └── build_windows.yml    # GitHub Actions workflow
├── main.py                      # Main application
├── build.spec                   # PyInstaller configuration
├── version_info.txt             # Windows version info
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## License

MIT License - Free to use and modify.

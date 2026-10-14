# Automated File Organizer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

A Python-based automation utility that continuously monitors a specified directory and automatically moves incoming files into designated subfolders based on a customizable JSON configuration.

---

##  Table of Contents
- [About](#about)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Prerequisites](#prerequisites)
- [Installation](#installation)

##  About

This project automates file management by utilizing file system event monitoring. Instead of manually sorting downloads, the script runs in the background and instantly moves created or modified files into predetermined directories based on their file extensions. The sorting rules are fully decoupled from the core logic and managed via a lightweight JSON configuration file.

### Tech Stack
*   **Language/Framework:** Python
*   **Libraries:** `watchdog` (for cross-platform file system event monitoring), `json`, `shutil`, `os`

##  Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

*   Python 3.8+
*   Pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/MohamedHassanExp/Python_automation.git](https://github.com/MohamedHassanExp/Python_automation.git)
2. Navigate to the project directory
   ```bash
   cd Python_automation-main/file-organizer
3. Install dependencies
   ```bash
   pip install -r requirements.txt

### Usage 

Run the main script to start monitoring
   ```bash
   python main.py

### configuration

 Define the in the `config.json` file.

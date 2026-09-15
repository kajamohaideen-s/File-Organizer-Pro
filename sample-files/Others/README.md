# File Organizer Pro
> A Python-based automation tool that intelligently organizes files into category-based folders, handles duplicate filenames safely, and provides preview, logging, and summary reporting.

## 🎯 Objective

The objective of this project is to automate the organization of messy folders and reduce the time required to manually sort files.

The system identifies files based on their extensions and automatically places them into appropriate categories such as Images, Documents, Audio, Video, Archives, Scripts, Data, and Others.

## 📌 Project Overview

File Organizer Pro is a Python-based file organization and management system that automatically organizes files into category-based folders according to their file extensions.

It helps users keep messy folders clean, structured, and easy to navigate.

## 🎯 Problem Statement

Managing a folder containing hundreds of files can become difficult and time-consuming.

Files such as images, documents, videos, audio files, scripts, and archives can become mixed together.

This project automates the organization process.

## 🚀 Features

- Automatic file categorization
- Category-based folder creation
- Supports multiple file types
- Handles unknown file types using `Others`
- Duplicate filename handling
- Safe duplicate renaming
- Error handling
- Logging system
- Preview mode
- Summary report
- User-defined folder input

## 🛠️ Technologies Used

- Python
- pathlib
- shutil
- logging

## 📂 Project Structure

File-Organizer-Pro/
├── main.py
├── organizer.py
├── config.py
├── logs/
├── sample-files/
└── README.md

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
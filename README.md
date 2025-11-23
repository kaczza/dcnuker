# 🔥 ZROX Discord Nuker

A powerful Discord server nuker. Use responsibly and only on servers you own or have explicit permission to test on.
<img width="529" height="339" alt="image" src="https://github.com/user-attachments/assets/db12e20b-73ba-4225-aa81-b60cb5376b02" />

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-green)

## ⚠️ DISCLAIMER

**This tool is for educational purposes only. Misuse of this software may violate Discord's Terms of Service and could result in account termination. The developers are not responsible for any damages caused by improper use.**

## 🚀 Features

- 🗑️ **Complete Server Reset** - Delete all channels and roles
- 📦 **Template Backup** - Automatically create server backups
- 👑 **User Promotion** - Grant admin privileges to specific users
- 🎨 **Custom Branding** - Set custom nuker name and messages
- 🔄 **Auto-Updater** - Built-in update system
- ⏹️ **Safe Stop** - Stop nuke process at any time

## 📋 Prerequisites

- Python 3.8 or higher
- Discord Bot Token with necessary permissions
- Server ID where you have administrative access

## 🔧 Installation

1. Download the repository
2. Install required dependencies:
   discord.py aiohttp requests

3. Discord Bot:
   - Get a working discord bot token

## 🎮 Usage

1. Run the tool:
  Whith the start.bat or
  python Nuker.py

3. Main Menu Options:
   - nuke - Start the nuke process
   - update - Download latest version
   - help - Show help menu

4. Nuke Process:
   - Enter your Bot Token
   - Enter the Server ID to nuke
   - (Optional) Enter User ID to promote
   - Enter Nuker Name (displayed in server)
   - Enter Spam Message (sent in channels)

5. During Nuke:
   - Type stop at any time to abort the process
   - Process includes: template backup, user promotion, channel/role deletion, and message spam

## 🛡️ Bot Permissions Required

- Administrator permission
- Or manually enable:
  - Manage Channels
  - Manage Roles  
  - Manage Server
  - Send Messages
  - Mention Everyone
  - Manage Messages

## 📸 Process Overview

1 Template Backup → 2 User Promotion → 3 Server Rename
       ↓
4 Delete Channels → 5 Delete Roles → 6 Create New Channels
       ↓
7 Create New Role → 8 Assign Role → 9 Message Spam

## 🎨 Customization

You can customize:
- Server name after nuke
- Channel names pattern
- Role name created
- Spam message content
- Nuker identity displayed

## ⚡ Quick Start

1. Install and run:
  With the start.bat

2. In the menu, type 'nuke'
3. Follow the prompts with your:
   - Bot Token
   - Server ID  
   - Custom nuker name
   - Custom message

## 🔄 Updating

The tool includes an auto-updater. Use the update command in the main menu or check to verify you're running the latest version.

## ❓ Troubleshooting

Common Issues:

- Server not found - Check Server ID and bot permissions
- Failed to create template - Bot needs template permissions
- User not found - User ID is incorrect or user left server
- Failed to download icon - Internet connection issue

Bot Not Working?
- Verify bot has Administrator permission
- Check bot is in the target server
- Ensure you're using the correct Server ID
- Confirm bot token is valid

## 📝 Legal Notice

This software is provided for educational and authorized testing purposes only. Users are solely responsible for complying with Discord's Terms of Service and applicable laws.
As the software developer, I am not responsible for how or by whom this software is used. 

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📞 Support

- Discord: Join our server - https://www.discord.gg/UTxb2Dk9jQ
- GitHub: Create an issue

⭐ If you find this project useful, please give it a star!

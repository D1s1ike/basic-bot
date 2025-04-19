# Discord Bot by dis1ik3

Welcome to the official repository for the Discord Bot developed by **dis1ik3**!  
This bot is built using **Python** and the powerful **Nextcord** library—making it fast, reliable, and easy to customize. Whether you're looking for moderation tools, verification systems, or just cool new features for your server, this bot is made for you.

---

## 🌐 Connect with dis1ik3

- **Discord Server & Bot Hub:** [Dislike Lab](https://discord.gg/dislike-lab)  
  Join to get updates, support, and discover other bots and web development projects.

---

## 🚀 Features

- Modern Python codebase using Nextcord (an improved Discord API wrapper)
- Simple configuration via `config.json`
- Customizable bot prefix and button styles
- Easy dependency management with `requirements.txt`
- **Simple Systems Included:**
  - **Verify System**: Allows users to verify themselves and receive a specific role.
  - **Welcome System**: Greets new members when they join your server.

---

## 🛠️ Getting Started

### 1. **Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. **Install Requirements**
Make sure you have Python 3.8+ installed. Then, install dependencies:
```bash
pip install -r requirements.txt
```

### 3. **Configure Your Bot**

Edit the `config.json` file to set up your bot.  
Example configuration:
```json
{
  "token": "Xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", // Your Discord bot token
  "guildId": 1000000000000000,                  // Your Discord server (guild) ID
  "prefix": ["!", "?"],                         // Bot command prefixes
  "verifyRole": 123456789012345678,             // Role ID for verification system
  "buttonStyle": 1                              // Button style for verify system
}
```

#### **Button Style Options**
- `1`: Blurple (Default Discord style)
- `2`: Gray
- `3`: Green
- `4`: Red

**Note:**  
- To find your role or server ID, enable "Developer Mode" in Discord settings and right-click the role/server to "Copy ID".
- Keep your bot token safe—never share it!

---

## ▶️ Running the Bot

After configuration:
```bash
python bot.py
```
Or, if the main file has a different name, replace `bot.py` with the correct filename.

---

## 📋 Simple Systems List

- **Verify System**:  
  Users can verify themselves by clicking a button. When verified, the bot assigns them a designated role.

- **Welcome System**:  
  The bot sends a welcome message to greet new members when they join your Discord server.

_More systems and features coming soon!_

---

## 📚 Useful Links

- [Nextcord Documentation](https://docs.nextcord.dev/)
- [Python Official Site](https://www.python.org/)
- [Dislike Lab Discord](https://discord.gg/dislike-lab)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Made with ❤️ by dis1ik3 — [Dislike Lab](https://discord.gg/dislike-lab)**
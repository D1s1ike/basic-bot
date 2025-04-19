# Discord Bot by dis1ik3

Welcome to the official repository for the Discord Bot developed by **dis1ik3**!  
This bot is built using **Python** and the powerful **Nextcord** library—making it fast, reliable, and easy to customize. Whether you're looking for moderation tools, verification systems, or just cool new features for your server, this bot is made for you.

---

## 🌐 Connect with dis1ik3

- **Discord Server & Bot Hub:** [Dislike's Lab](https://discord.gg/dislike-lab)  
  Join to get updates, support, and discover other bots and web development projects.

---

## 🚀 Features

- Modern Python codebase using Nextcord (an improved Discord API wrapper)
- Simple configuration via `config.json`
- Customizable bot prefix and button styles
- Easy dependency management with `requirements.txt`
- Open source project
- **Systems Included:**
  - **Verify System**: Allows users to verify themselves and receive a specific role.
  - **Welcome System**: Greets new members when they join your server.
  - **Status System** Displays members amount in the bot status

---

## 🛠️ Getting Started

### 1. **Clone the Repository**
```bash
git clone https://github.com/D1s1ike/basic-bot.git
cd basic-bot
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
  "staffRole": 123456789012345678,              // Staff Role ID
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
python main.py
```
Or, if the main file has a different name, replace `main.py` with the correct filename.

---

## 📋 Systems List

- **Verify System**:  
  Users can verify themselves by clicking a button. When verified, the bot assigns them a designated role.

- **Welcome System**:  
  The bot sends a welcome message to greet new members when they join your Discord server.

---

## 🧩 Command List

Here are the main commands for setting up and managing your server’s verification and welcome systems:

### 🔐 Verify System

#### `/setup-verify [Channel]` (Administrator Only)
Set up the verification system in a specified channel.  
When you use this command, the bot will send a verification message with a button in the chosen channel. Members can click the button to verify themselves and automatically receive the configured verification role.

**Example:**  
`/setup-verify #verify-here`  
*Creates a verification message in the `#verify-here` channel.*

---

### 👋 Welcome System

#### `/setup-welcome [Channel]` (Administrator Only)
Set up the welcome system in a specified channel.  
When a new member joins your server, the bot will greet them in the selected channel with a customizable welcome message.

**Example:**  
`/setup-welcome #welcome`  
*The bot will send welcome messages to the `#welcome` channel whenever someone joins.*

---

## 📚 Useful Links

- [Nextcord Documentation](https://docs.nextcord.dev/)
- [Python Official Site](https://www.python.org/)
- [Dislike's Lab Discord](https://discord.gg/dislike-lab)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

**Made with ❤️ by dis1ik3 — [Dislike's Lab](https://discord.gg/dislike-lab)**
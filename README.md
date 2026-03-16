# BD111 Casino Web App + Telegram Bot + Nginx

## Overview

This project is a full-featured **Casino Web App** integrated with a **Telegram Bot**.  
It includes:

- 🎰 Web App: Slot Machine UI, Dashboard, Deposit & Withdraw pages, Admin panel.
- 🤖 Telegram Bot: `/start` and `/deposit` commands.
- 🌐 Nginx: Reverse proxy to host the web app on your domain.
- ✅ Ready-to-deploy structure for VPS or server hosting.

---

## Folder Structure

```text
bd111-casino-deploy/
│
├── webapp/
│   ├── index.html        # Home + Login
│   ├── dashboard.html    # User Dashboard
│   ├── slot.html         # Slot Machine UI
│   ├── deposit.html      # Demo Deposit Page
│   ├── withdraw.html     # Demo Withdraw Page
│   ├── admin.html        # Admin Panel
│   ├── style.css         # All CSS Styling
│   └── script.js         # Slot Game Logic & UI
│
├── bot/
│   └── bot.py            # Telegram Bot
│
├── nginx/
│   └── bd111casino.conf  # Nginx Configuration
│
└── README.md             # Project Documentation

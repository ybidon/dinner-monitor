# Dinner Monitor

Monitors the availability of dinner reservations at the restaurant.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

3. Deploy to Vercel:
```bash
vercel
```

## Features

- Checks dinner availability every minute
- Sends notifications when slots become available
- Supports multiple time slots
- Configurable notification settings 
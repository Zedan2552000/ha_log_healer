# HA Log Healer (AI SysAdmin) 🩺🤖

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/hacs/integration)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A smart, open-source Home Assistant custom integration that acts as your personal AI System Administrator. It automatically reads your `home-assistant.log`, detects cryptic `ERROR` and `WARNING` traces, and uses AI (via OpenAI-compatible endpoints like Groq, OpenRouter, DeepSeek, or Anthropic Claude) to analyze the traceback and provide a human-readable, step-by-step solution.

## 🌟 Why HA Log Healer?
Home Assistant logs can be overwhelming for users. When an integration crashes or a YAML template fails, the resulting traceback is often difficult to decipher. HA Log Healer bridges the gap between complex logs and actionable solutions by leveraging Large Language Models (LLMs) to diagnose and explain the issue natively within your Home Assistant dashboard.

## 🚀 Features
- 📝 **Automated Log Extraction:** Seamlessly extracts the latest error traces from your local `home-assistant.log`.
- 🧠 **AI-Powered Diagnostics:** Sends tracebacks to your preferred LLM and translates them into actionable fixes.
- ⚡ **Universal Compatibility:** Works with any OpenAI-compatible API endpoint (Groq for ultra-low latency, Claude/OpenRouter for deep reasoning).
- ⚙️ **No YAML Required:** Fully configurable via the Home Assistant UI (Config Flows).

## 🛠️ Installation

### Method 1: HACS (Recommended)
1. Navigate to **HACS** > **Integrations**.
2. Click the three dots (top right) and select **Custom repositories**.
3. Add this repository URL as an `Integration`.
4. Search for `HA Log Healer` and click Download.
5. Restart Home Assistant.

### Method 2: Manual
1. Download the `custom_components/ha_log_healer` directory.
2. Place it inside your Home Assistant `custom_components` directory.
3. Restart Home Assistant.

## ⚙️ Configuration
1. Go to **Settings** > **Devices & Services** > **Add Integration**.
2. Search for **HA Log Healer**.
3. Enter your AI provider details:
   - **API Key**: Your provider's API key.
   - **Base URL**: e.g., `https://api.groq.com/openai/v1`
   - **Model**: e.g., `llama-3.1-8b-instant` or `claude-3-5-sonnet-20240620`
4. Click Submit.

## 🖱️ Usage
Call the `ha_log_healer.analyze_logs` service from your Developer Tools or any Automation. The integration will parse the latest errors and update the `sensor.ha_log_healer_analysis` entity with a clear, step-by-step solution!

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request to improve the integration. Let's make Home Assistant easier for everyone.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

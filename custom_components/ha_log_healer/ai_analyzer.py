import logging
import aiohttp
import os
from .const import CONF_API_KEY, CONF_BASE_URL, CONF_MODEL

_LOGGER = logging.getLogger(__name__)

async def get_latest_errors(hass):
    log_file = hass.config.path("home-assistant.log")
    if not os.path.exists(log_file):
        return "No log file found."
    
    errors = []
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # Get last 200 lines and filter for ERROR or WARNING
            recent_lines = lines[-200:]
            for line in recent_lines:
                if "ERROR" in line or "WARNING" in line:
                    errors.append(line.strip())
            # Join up to 10 latest errors
            return "\n".join(errors[-10:])
    except Exception as e:
        return f"Could not read log file: {e}"

async def analyze_latest_logs(hass, config_data):
    errors = await get_latest_errors(hass)
    if not errors or "No log file found" in errors:
        return {"error": "No recent errors found in logs.", "solution": "Your system looks healthy!"}
        
    api_key = config_data.get(CONF_API_KEY)
    base_url = config_data.get(CONF_BASE_URL)
    model = config_data.get(CONF_MODEL)
    
    prompt = f"Analyze the following Home Assistant logs and provide a short, human-readable explanation of the error and a step-by-step solution in Arabic:\n\n{errors}"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a Home Assistant expert administrator. Analyze the logs and provide a fix in clear Arabic."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 1000
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{base_url}/chat/completions", headers=headers, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    solution = data["choices"][0]["message"]["content"]
                    return {"error": errors[:500] + "...", "solution": solution}
                else:
                    return {"error": f"API Error {response.status}", "solution": await response.text()}
    except Exception as e:
        _LOGGER.error(f"AI API request failed: {e}")
        return {"error": "API Request Failed", "solution": str(e)}

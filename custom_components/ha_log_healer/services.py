import logging
from homeassistant.core import HomeAssistant, ServiceCall
from .const import DOMAIN
from .ai_analyzer import analyze_latest_logs

_LOGGER = logging.getLogger(__name__)

async def async_setup_services(hass: HomeAssistant, entry):
    async def handle_analyze_logs(call: ServiceCall):
        _LOGGER.info("Starting AI Log Analysis...")
        # Get sensor entity
        sensor = None
        for entity in hass.data["entity_components"]["sensor"].entities:
            if entity.unique_id == f"{entry.entry_id}_log_healer":
                sensor = entity
                break
        
        if sensor:
            sensor.update_analysis("Analyzing...", None, None)
            
        try:
            result = await analyze_latest_logs(hass, entry.data)
            if sensor:
                sensor.update_analysis("Analysis Complete", result.get("error"), result.get("solution"))
        except Exception as e:
            _LOGGER.error(f"Error during log analysis: {e}")
            if sensor:
                sensor.update_analysis("Error", str(e), "Check integration logs.")

    hass.services.async_register(DOMAIN, "analyze_logs", handle_analyze_logs)

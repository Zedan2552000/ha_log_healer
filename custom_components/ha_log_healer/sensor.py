from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([HALogHealerSensor(hass, entry)])

class HALogHealerSensor(SensorEntity):
    def __init__(self, hass, entry):
        self._hass = hass
        self._entry = entry
        self._attr_name = "AI Log Healer Analysis"
        self._attr_unique_id = f"{entry.entry_id}_log_healer"
        self._state = "Waiting for analysis..."
        self._attr_extra_state_attributes = {"last_error": None, "solution": None}

    @property
    def state(self):
        return self._state

    def update_analysis(self, status, error, solution):
        self._state = status
        self._attr_extra_state_attributes["last_error"] = error
        self._attr_extra_state_attributes["solution"] = solution
        self.async_write_ha_state()

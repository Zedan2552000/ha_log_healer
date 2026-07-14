import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, CONF_API_KEY, CONF_BASE_URL, CONF_MODEL, DEFAULT_BASE_URL, DEFAULT_MODEL

class HALogHealerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="HA Log Healer", data=user_input)

        data_schema = vol.Schema({
            vol.Required(CONF_API_KEY): str,
            vol.Optional(CONF_BASE_URL, default=DEFAULT_BASE_URL): str,
            vol.Optional(CONF_MODEL, default=DEFAULT_MODEL): str,
        })
        return self.async_show_form(step_id="user", data_schema=data_schema)

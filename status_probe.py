
from base_plugin import BasePlugin, HookResult

__id__ = "status_probe"
__name__ = "Status Probe"
__description__ = "Diagnostic Telegram status update monitor"
__version__ = "0.1.0"
__app_version__ = ">=12.5.1"
__sdk_version__ = ">=1.4.4.3"


class StatusProbe(BasePlugin):

    def on_plugin_load(self):
        self.logger.info("STATUS PROBE: Plugin loaded")

        self.add_hook("TL_updateUserStatus")

        self.logger.info(
            "STATUS PROBE: Registered TL_updateUserStatus hook"
        )

    def on_update_hook(self, update_name, account, update):
        if update_name == "TL_updateUserStatus":
            self.logger.info("STATUS PROBE: Status update received")
            self.logger.info("User ID: %s", update.user_id)

            status = getattr(update, "status", None)

            if status is not None:
                try:
                    self.logger.info(
                        "Status class: %s",
                        status.getClass().getSimpleName()
                    )
                except Exception:
                    self.logger.info(
                        "Status type: %s",
                        type(status).__name__
                    )

                self.logger.dump(status)

        return HookResult()

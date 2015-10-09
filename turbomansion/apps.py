from django.apps import AppConfig

import pychromecast as pycc


class TurboMansion(AppConfig):
    name = 'turbomansion'
    verbose_name = "TurboMansion"

    cast_list = []
    cast = None

    first_run = True

    def ready(self):
        if self.first_run:
            self.cast_list = pycc.get_chromecasts_as_dict().keys()
            self.cast = pycc.get_chromecast(friendly_name="Ulicast")

            self.first_run = False
        else:
            pass
        

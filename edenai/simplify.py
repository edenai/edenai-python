from edenai.api.auto_ml_text_data_api import AutoMLTextDataApi
from edenai.api.ocr_api import OCRApi
from edenai.api.pipelines_api import PipelinesApi
from edenai.api.speech_api import SpeechApi
from edenai.api.text_api import TextApi
from edenai.api.translation_api import TranslationApi
from edenai.api.vision_api import VisionApi
# import ApiClient
from edenai.api_client import ApiClient
from edenai.configuration import Configuration

def simplify(Class):
    original_init = Class.__init__
    def __init__(self, api_key):
        configuration = Configuration()
        configuration.api_key['Authorization'] = api_key
        configuration.api_key_prefix['Authorization'] = 'Bearer'
        original_init(self, ApiClient(configuration))

    Class.__init__ = __init__
    return Class

for api in ["Text", "Vision", "OCR", "Pipelines", "Translation", "AutoMLTextData", "Speech"]:
    exec(api+" = simplify({}Api)".format(api))



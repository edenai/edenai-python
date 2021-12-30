# Eden AI Python

![Screenshot](https://github.com/edenai/edenai-python/blob/3829feb170f11cfd55aacd877d23c5f8d69e203f/Logo%20complet%20Eden%20AI%20-%20format%20PNG.png)


This is the official Eden AI Python Github for interacting with our powerful APIs. [Eden AI](https://www.edanai.co/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers for vision, text, audio, OCR, prediction and translation AI engines. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

* Eden AI support: contact@edenai.co              
* Check our website: https://www.edenai.co
* Sign-up for a free account: https://app.edenai.run/user/login
* Read our documentation: https://api.edenai.run/v1/redoc/


Eden AI simplifies the use and integration of AI technologies by providing a unique API connected to the best AI engines and combined with a powerful management platform. The platform covers a wide range of AI technologies:
* Vision: www.edenai.co/vision
* Text & NLP: www.edenai.co/text
* Speech & Audio: www.edenai.co/speech
* OCR: www.edenai.co/ocr
* Machine Translation: www.edenai.co/translation
* Prediction: www.edenai.co/prediction

For all the proposed technologies, we provide a single endpoint: the service provider is only a parameter that can be changed very easily. All the engines available on Eden AI are listed here: www.edenai.co/catalog

## Getting started
To start using Eden AI APIs, you first need to get your API Token.  You can get your token on your IAM [here](https://app.edenai.run/admin/account).

## Install via pip 
Just run:

    pip install -U edenai

## Usage

If you want, for example, to use key word extraction from Amazon Web Services and IBM Watson:

```python 

from edenai import Text 

API_KEY = "YOURAPIKEYTHATYOUGETFROMTHEPLATFORM"
some_text = "Hello this is a great example to begin with"

text_apis = Text(API_KEY)
result = text_apis.keyword_extraction(
        text=some_text,
        providers=["amazon", "ibm"],
        language="en-US",
    )

```

You can find the complete list of technologies we offer in the [SDK documentation](https://edenai-python.readthedocs.io/) and [quick ready-to-use examples here](https://github.com/edenai/edenai-python/tree/main/ready-to-use).

## Support & Community

If you have any problems, please contact us at this email address: contact@edenai.co. We will be happy to help you in the use of Eden AI.

Community:
You can interact personally with other people actively using and working with Eden AI and join our [Slack community](https://join.slack.com/t/edenai-community/shared_invite/zt-t68c2pr9-4lDKQ_qEqmLiWNptQzB_6w).
We are always updating our docs, so a good way to always stay up to date is to watch our documentation repo on [Github](https://www.github.com/edenai).

Blog:
We also regularly publish various articles with Eden AI news and technical articles on the different AI engines that exist. You can find these articles here: [Blog](https://www.edenai.co/blog)

## Contribution

If you'd like to contribute, please check the [CONTRIBUTING.md](https://github.com/edenai/edenai-python/blob/main/CONTRIBUTING.md) file.

## Documentation

You can find the complete list of technologies we offer in the [SDK documentation](https://edenai-python.readthedocs.io/) .
To have more information about platform and API use, you can check ou our [documentation](https://api.edenai.run/v1/redoc/)

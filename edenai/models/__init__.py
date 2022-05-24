# coding: utf-8

# flake8: noqa
"""
    Eden AI API Documentation

    <a href=\"https://app.edenai.run/user/login\" target=\"_blank\"><img src=\"/static/images/welcome.png\"></a>. # Welcome  Eden AI simplifies the use and integration of AI technologies by providing a unique API connected to the best AI engines and combined with a powerful management platform. The platform covers a wide range of AI technologies: * Vision:  <a href=\"https://www.edenai.co/vision\" target=\"_blank\">www.edenai.co/vision</a>. * Text & NLP: <a href=\"https://www.edenai.co/text\" target=\"_blank\">www.edenai.co/text</a>. * Speech & Audio: <a href=\"https://www.edenai.co/speech\" target=\"_blank\">www.edenai.co/speech</a>. * OCR: <a href=\"https://www.edenai.co/ocr\" target=\"_blank\">www.edenai.co/ocr</a>. * Machine Translation: <a href=\"https://www.edenai.co/translation\" target=\"_blank\">www.edenai.co/translation</a>. * Prediction: <a href=\"https://www.edenai.co/prediction\" target=\"_blank\">www.edenai.co/prediction</a>.  For all the proposed technologies, we provide a single endpoint:  the service provider is only a parameter that can be changed very easily. All the engines available on Eden AI are listed here: www.edenai.co/catalog  # Support & community  ### 1- Support If you have any problems, please contact us at this email address: contact@edenai.co. We will be happy to help you in the use of Eden AI.   ### 2- Community  You can interact personally with other people actively using and working with Eden AI and join our  <a href=\"https://join.slack.com/t/edenai/shared_invite/zt-t68c2pr9-4lDKQ_qEqmLiWNptQzB_6w\" target=\"_blank\">Slack community</a>.  We are always updating our docs, so a good way to always stay up to date is to watch our documentation repo on Github: <a href=\"https://github.com/edenai\" target=\"_blank\">https://github.com/edenai</a>.  ### 3- Blog  We also regularly publish various articles with Eden AI news and technical articles on the different AI engines that exist. You can find these articles here: <a href=\"https://www.edenai.co/blog\" target=\"_blank\">https://www.edenai.co/blog</a>.   # Authentication  ## Create account ![Register](/static/images/register.png)  To create an account, please go to this link: <a href=\"https://app.edenai.run/user/login\" target=\"_blank\">app.edenai.run/user/login</a>. You can create an account with your email address or by using your account on available platforms (Gmail, Github, etc.).   By creating an account with your email address, you will receive a confirmation email with a link to click. Check your spam if needed and contact us if you have any problem: contact@edenai.co  ![Login](/static/images/login.png) ## API key  By going to your account page on the platform: <a href=\"https://app.edenai.run/admin/account\" target=\"_blank\">https://app.edenai.run/admin/account</a>, you will have access to your API key to start using the different AI engines offered by Eden AI.   ![api_key](/static/images/api_key.png)  ## Sandbox API key  By going to your account page on the platform: <a href=\"https://app.edenai.run/admin/account\" target=\"_blank\">https://app.edenai.run/admin/account</a>, you will also have access to your **Sandbox** API key that will allow you to make free calls and get dummy responses in order to implement and debug Eden AI without consuming credits.   ![api_key](/static/images/sandbox_api_key.png)  # Portal Guide  Eden AI provides a web portal that allows you to do several tasks:  ![portal](/static/images/portal.png)  ### 1- Benchmark and test The platform allows you to easily compare competing engines without having to code. By uploading your data, you have access to the prediction results of the different engines. This gives you a first overview of the performance of AI engines.   ![benchmark](/static/images/benchmark.png)  ### 2- Cost management The <a href=\"https://app.edenai.run/admin/cost-management\" target=\"_blank\">cost management page</a> also allows you to centralize the costs associated with the different engines with various filters to simplify the analysis.   This page also allows you to define monthly budget limits not to be exceeded to secure the use of different AI engines.   ![cost-management](/static/images/cost_management.png) ### 3- Account The <a href=\"https://app.edenai.run/admin/account\" target=\"_blank\">account page</a> allows you to change your information and password. It also gives you access to your API key that you can renew if needed.   This page also allows you to add a credit card and to buy with credits to use all the engines offered by Eden AI.   ![account](/static/images/account.png)   # API Guide  Eden AI API has different endpoints that refer to different AI services. The connected providers are thus parameters that the user can easily change.   # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@edenai.co
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from edenai.models.inline_response200 import InlineResponse200
from edenai.models.inline_response2001 import InlineResponse2001
from edenai.models.inline_response20010 import InlineResponse20010
from edenai.models.inline_response20010_result import InlineResponse20010Result
from edenai.models.inline_response20010_result1 import InlineResponse20010Result1
from edenai.models.inline_response20011 import InlineResponse20011
from edenai.models.inline_response20011_result import InlineResponse20011Result
from edenai.models.inline_response20011_result1 import InlineResponse20011Result1
from edenai.models.inline_response20012 import InlineResponse20012
from edenai.models.inline_response20012_result import InlineResponse20012Result
from edenai.models.inline_response20012_result1 import InlineResponse20012Result1
from edenai.models.inline_response20013 import InlineResponse20013
from edenai.models.inline_response20013_result import InlineResponse20013Result
from edenai.models.inline_response20013_result1 import InlineResponse20013Result1
from edenai.models.inline_response20014 import InlineResponse20014
from edenai.models.inline_response20014_result import InlineResponse20014Result
from edenai.models.inline_response20014_result1 import InlineResponse20014Result1
from edenai.models.inline_response20015 import InlineResponse20015
from edenai.models.inline_response20015_result import InlineResponse20015Result
from edenai.models.inline_response20015_result1 import InlineResponse20015Result1
from edenai.models.inline_response20016 import InlineResponse20016
from edenai.models.inline_response20016_result import InlineResponse20016Result
from edenai.models.inline_response20016_result1 import InlineResponse20016Result1
from edenai.models.inline_response20017 import InlineResponse20017
from edenai.models.inline_response20017_result import InlineResponse20017Result
from edenai.models.inline_response20017_result1 import InlineResponse20017Result1
from edenai.models.inline_response20017_result_landmarks import InlineResponse20017ResultLandmarks
from edenai.models.inline_response20018 import InlineResponse20018
from edenai.models.inline_response20018_result import InlineResponse20018Result
from edenai.models.inline_response20018_result1 import InlineResponse20018Result1
from edenai.models.inline_response20019 import InlineResponse20019
from edenai.models.inline_response20019_result import InlineResponse20019Result
from edenai.models.inline_response2001_result import InlineResponse2001Result
from edenai.models.inline_response2001_result1 import InlineResponse2001Result1
from edenai.models.inline_response2002 import InlineResponse2002
from edenai.models.inline_response2002_bounding_box import InlineResponse2002BoundingBox
from edenai.models.inline_response2002_cells import InlineResponse2002Cells
from edenai.models.inline_response2002_pages import InlineResponse2002Pages
from edenai.models.inline_response2002_result import InlineResponse2002Result
from edenai.models.inline_response2002_result1 import InlineResponse2002Result1
from edenai.models.inline_response2002_rows import InlineResponse2002Rows
from edenai.models.inline_response2002_tables import InlineResponse2002Tables
from edenai.models.inline_response2003 import InlineResponse2003
from edenai.models.inline_response2004 import InlineResponse2004
from edenai.models.inline_response2004_results import InlineResponse2004Results
from edenai.models.inline_response2005 import InlineResponse2005
from edenai.models.inline_response2005_result import InlineResponse2005Result
from edenai.models.inline_response2005_result1 import InlineResponse2005Result1
from edenai.models.inline_response2005_result_bounding_boxes import InlineResponse2005ResultBoundingBoxes
from edenai.models.inline_response2006 import InlineResponse2006
from edenai.models.inline_response2006_customer_information import InlineResponse2006CustomerInformation
from edenai.models.inline_response2006_item_lines import InlineResponse2006ItemLines
from edenai.models.inline_response2006_locale import InlineResponse2006Locale
from edenai.models.inline_response2006_merchant_information import InlineResponse2006MerchantInformation
from edenai.models.inline_response2006_result import InlineResponse2006Result
from edenai.models.inline_response2006_result1 import InlineResponse2006Result1
from edenai.models.inline_response2006_results import InlineResponse2006Results
from edenai.models.inline_response2007 import InlineResponse2007
from edenai.models.inline_response2007_result import InlineResponse2007Result
from edenai.models.inline_response2007_result1 import InlineResponse2007Result1
from edenai.models.inline_response2008 import InlineResponse2008
from edenai.models.inline_response2008_result import InlineResponse2008Result
from edenai.models.inline_response2008_result1 import InlineResponse2008Result1
from edenai.models.inline_response2009 import InlineResponse2009
from edenai.models.inline_response2009_result import InlineResponse2009Result
from edenai.models.inline_response201 import InlineResponse201
from edenai.models.inline_response2011 import InlineResponse2011
from edenai.models.inline_response2011_result import InlineResponse2011Result
from edenai.models.inline_response2011_result1 import InlineResponse2011Result1
from edenai.models.inline_response201_result import InlineResponse201Result
from edenai.models.inline_response201_result1 import InlineResponse201Result1
from edenai.models.inline_response204 import InlineResponse204
from edenai.models.inline_response204_result import InlineResponse204Result
from edenai.models.inline_response204_result1 import InlineResponse204Result1

from kavenegar import *
from urllib.error import HTTPError


def send_sms_with_template(receptor, tokens: dict, template):
    """
        sending sms that needs template
    """
    try:
        api = KavenegarAPI(
            '41696451664D362F4354504364393356416954524C6B5A4B65475536412F2B787459465A65796855384F493D'
        )
        params = {
            'receptor': receptor,
            'template': template,
        }
        for key, value in tokens.items():
            params[key] = value

        response = api.verify_lookup(params)
        print(response)
        return True
    except APIException as e:
        print(e)
        return False
    except HTTPError as e:
        print(e)
        return False


def send_sms_normal(receptor, message):
    try:
        api = KavenegarAPI(
            '41696451664D362F4354504364393356416954524C6B5A4B65475536412F2B787459465A65796855384F493D')
        params_buyer = {
            'receptor': receptor,
            'message': message,
            'sender': '2000500666'
        }
        response = api.sms_send(params_buyer)
        print(response)
    except APIException as e:
        print(e)
    except HTTPError as e:
        print(e)

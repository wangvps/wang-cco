import json
import requests

from loguru import logger


def deepl_remote_rust(text: str, to_lang: str = None, **kargs) -> str:
    if to_lang:
        lang_tgt = to_lang
    else:
        lang_tgt = 'ZH'
    payload = {
        'text': str(text),
        'source_lang': 'auto',
        'target_lang': lang_tgt.upper()
    }
    r = requests.post('https://api.deepl.com/v2/translate?auth_key=f6a13b32-b08b-3567-5e41-916a8f76058b',
                      data=json.dumps(payload))
    try:
        if r.status_code == 200 and 'application/json' in r.headers.get(
                'Content-Type', ''):
            if r.json()['code'] == 200:
                result = r.json()['data']
                # logger.info(result)
                return result
            else:
                pass
    except Exception as e:
        logger.exception('DeepL: ' + str(e))


if __name__ == "__main__":
    logger.info(deepl_remote_rust('have a look for me', to_lang='ZH'))
    pass

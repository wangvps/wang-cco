import re

from loguru import logger


# @logger.catch()
def clean(text: str) -> str:
    text = filter_forward(text)
    text = filter_flag(text)
    text = filter_emoji(text)
    text = filter_bot(text)
    return (text)


# @logger.catch()
def filter_forward(text: str) -> str:
    text = re.sub('(\[θ½¬εθͺ.*\])\n', '', text)
    return (text)


# @logger.catch()
def filter_bot(text: str) -> str:
    text = text.replace('@fanyi_bot', '').strip()
    return (text)


# @logger.catch()
def filter_flag(text: str) -> str:
    text = text.replace('πΊπΈ', '').replace('π¨π³', '')
    return (text)


# @logger.catch()
def filter_emoji(desstr: str, restr: str = '') -> str:
    try:
        res = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        res = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return res.sub(restr, desstr)


# @logger.catch()
def output_clean(text: str) -> str:
    # text = text.replace('οΌ', '(').replace('οΌ', ') ')
    # text = text.replace('γ', 'β').replace('γ', 'β')
    # text = text.replace('@', ' @')
    # text = text.replace('οΌ//', '://')
    # text = text.replace('HTTPSοΌ/ /', 'https://')
    # text = text.replace('/////', '\n')
    # text = re.sub('//*', '\n', text)
    # text = re.sub('\/{2,}', '', text)
    text = text.replace('@fanyi_bot ', '')
    return text


# @logger.catch()
def inline_clean(text: str) -> str:
    text = text.replace('*', '\*')
    return (text)


# def output(result: str, end_str_id: int = 1) -> str:
#     end_str = ''
#     if end_str_id == 2:
#         end_str = ''
#     msg_str = output_clean(result)
#     try:
#         logger.info('γ' + msg_str.replace('\n', '').replace(
#             '\n', ' | ').replace('πΊπΈ', '').replace('π¨π³', ''))
#     except Exception as e:
#         logger.info('γ' + msg_str.replace('\n', '').replace('\n', ' | '))
#         logger.exception("Output:" + str(e))
#     msg_str += end_str
#     return msg_str

# def get_text(msg: str) -> str:
#     if 'text' in msg:
#         return msg['text']
#     else:
#         return msg['caption']

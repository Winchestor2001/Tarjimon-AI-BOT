from googletrans import Translator


async def text_trans(text: str, lang: str):
    trans = Translator()
    result = trans.translate(
        text,
        dest=lang
    )
    return result.text





import string


def clean_text(text):
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    text = " ".join(text.split())

    return text
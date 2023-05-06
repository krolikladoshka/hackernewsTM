from bs4 import BeautifulSoup


def append_tm_to_string(text: str) -> str:
    """
    performs tmization of text with spaces formatting preserved
    assuming the word does not contain numerics or special symbols
    :param text: text for tmization
    :return: tmized text
    """

    tmed_text = []

    i = 0
    while i < len(text):
        if not text[i].isalpha():
            tmed_text.append(text[i])
            i += 1

            continue

        # scroll to the end of the word
        current_word_length = 0
        while i < len(text) and text[i].isalpha():
            tmed_text.append(text[i])
            current_word_length += 1
            i += 1

        if current_word_length >= 6:
            tmed_text.append('™')

    return ''.join(tmed_text)


def transform_tm(html: str) -> str:
    """
    performs tmization of the text inside entire `html`
    :param html: html string
    :return: tmized html string
    """
    soup = BeautifulSoup(html, 'html.parser')

    # if handling of something like <b><i>testi</i>ng</i></b> -> <b><i>testi</i>ng™</b> is desired
    # than I can't come up with something simpler than recursive syntax parsing
    # for simplicity assuming that we're parsing only simple web pages
    for node in soup.find_all(text=True):
        tmed_text = append_tm_to_string(node.text)
        node.replace_with(tmed_text)

    return str(soup)

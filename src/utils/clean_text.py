def clean_text(text: str) -> str:
    """
    Cleans inputted text to the end of the last complete sentence,
    dropping any partial sentences following it.

    Parameters:
        text (str): Input text

    Returns:
        str: Input text, truncated to the end of the last complete sentence.
    """

    last_period: int = text.rfind(".")
    last_question: int = text.rfind("?")
    last_exclamation: int = text.rfind("!")
    last_punctuation: int = max(last_exclamation, last_period, last_question)
    return text[:last_punctuation+1]

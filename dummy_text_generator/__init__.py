"""A Python library for generating random texts, sentences,
paragraphs, comments, and names in multiple languages like
English, Spanish, French, and German.

The generated content is assembled using predefined templates
and words. It does not use any machine learning models or
external APIs. It is intended for generating dummy content for
testing and development purposes.
"""

import random

from .actions import ACTIONS
from .comments import COMMENTS
from .details import DETAILS
from .hashtags import HASHTAGS
from .mail_domains import MAIL_DOMAINS
from .names import NAMES, SURNAMES
from .starts import STARTS
from .topics import TOPICS


def generate_sentence(
    lang: str = 'en',
    topic: str | None = None,
    add_hashtag: bool = False,
) -> str:
    """Generates a random sentence.

    .. note::
        It is recommended to add the article before the topic,
        for example, 'the sports' instead of 'sports'.

    Parameters
    ----------
    lang : str, optional
        Language, by default 'en'.
    topic : str, optional
        Topic about which to generate the sentence.
        If not provided, a random topic will be used.
    add_hashtag : bool, optional
        Add a random hashtag at the end, by default False.

    Returns
    -------
    str
        Randomly generated sentence.

    Raises
    ------
    KeyError
        If the language is not supported.

    Examples
    --------
    >>> generate_sentence('es')
    'Hoy estuve pensando en lo increíble que es aprender algo nuevo sobre deportes y descubrí algo sorprendente.'
    >>> generate_sentence('en', 'the sports')
    'Today I was thinking about how amazing it is to learning something new about sports and discovered something surprising.'
    >>> generate_sentence('en', True)
    'Today I was thinking about how amazing it is to learning something new about sports and discovered something surprising. #Amazing'
    """
    try:
        start = random.choice(STARTS[lang])
        action = random.choice(ACTIONS[lang])
        topic = random.choice(TOPICS[lang]) if topic is None else topic
        detail = random.choice(DETAILS[lang])
        hashtag = random.choice(HASHTAGS[lang])
        sentence = f'{start} {action} {topic} {detail}'
        if add_hashtag:
            sentence += f' {hashtag}'
        return sentence
    except KeyError:
        raise KeyError(f'language {lang!r} is not supported')


def generate_paragraph(
    lang: str = 'en', sentences: int = 3, topic: str | None = None
) -> str:
    """Generates a random paragraph.

    .. note::
        It is recommended to add the article before the topic,
        for example, 'the sports' instead of 'sports'.

    Parameters
    ----------
    lang : str, optional
        Language, by default 'en'.
    sentences : int, optional
        Number of sentences, by default 3.
    topic : str, optional
        Topic about which to generate the paragraph.
        If not provided, a random topic will be used.

    Returns
    -------
    str
        Randomly generated paragraph.

    Raises
    ------
    KeyError
        If the language is not supported.

    Examples
    --------
    >>> generate_paragraph('es', 2)
    '''Hoy estuve pensando en lo increíble que es aprender algo nuevo sobre deportes y descubrí algo sorprendente.
    Nunca imaginé cuánto podríamos aprender de autos. Siempre he querido aprender más sobre autos. Esto me motiva aun más.
    '''
    >>> generate_paragraph('en', 2, 'sports')
    '''Today I was thinking about how amazing it is to learning something new about sports and discovered something surprising.
    Nothing can compare to the joy of learning something new about sports.
    '''
    """
    return '\n'.join(generate_sentence(lang, topic) for _ in range(sentences))


def generate_comment(lang: str = 'en', topic: str | None = None) -> str:
    """Generates a random comment about a ``topic``.

    .. note::
        It is recommended to add the article before the topic,
        for example, 'the sports' instead of 'sports'.

    Parameters
    ----------
    lang : str, optional
        Language, by default 'en'.
    topic : str, optional
        Topic about which to generate the comment.
        If not provided, a random topic will be used.

    Returns
    -------
    str
        Randomly generated comment.

    Raises
    ------
    KeyError
        If the language is not supported.

    Examples
    --------
    >>> generate_comment(topic='deportes')
    'Cada vez que veo algo sobre deportes, me siento inspirado. ¡Gracias por compartir!'
    >>> generate_comment('en', topic='sports')
    'Every time I see something about sports, I feel inspired. Thanks for sharing!'
    """
    try:
        if topic is None:
            topic = random.choice(TOPICS[lang])
        return random.choice(COMMENTS[lang]).format(topic=topic)
    except KeyError:
        raise KeyError(f'language {lang!r} is not supported')


def generate_fullname(lang: str = 'en') -> str:
    """Generates a random fullname.

    Parameters
    ----------
    lang : str, optional
        Language, by default 'en'.

    Returns
    -------
    str
        Randomly generated name.

    Raises
    ------
    KeyError
        If the language is not supported.

    Examples
    --------
    >>> generate_fullname()
    'John Miller'
    >>> generate_fullname('es')
    'Alejandro Reyes'
    >>> generate_fullname('fr')
    'Béatrice Moreau'
    >>> generate_fullname('de')
    'Franziska Schneider'
    """
    try:
        return f'{random.choice(NAMES[lang])} {random.choice(SURNAMES[lang])}'
    except KeyError:
        raise KeyError(f'language {lang!r} is not supported')


def generate_username_from_fullname(fullname: str) -> str:
    """Generates a username from a ``fullname``.

    Parameters
    ----------
    fullname : str
        Fullname.

    Returns
    -------
    str
        Generated username.

    Examples
    --------
    >>> generate_username_from_fullname('John Miller')
    'johnmill28'
    >>> generate_username_from_fullname('Alejandro Reyes')
    'alejreye82'
    """
    name, surname = fullname.split(' ', 1)
    username = (
        (name[:4] + surname[:4]).lower()
        + str(random.randint(0, 9))
        + str(random.randint(0, 9))
    )

    while len(username) < 10:
        username += str(random.randint(0, 9))

    return username


def generate_email_from_username(username: str) -> str:
    """Generates an email from a ``username``.

    Parameters
    ----------
    username : str
        Username.

    Returns
    -------
    str
        Generated email.

    Examples
    --------
    >>> generate_email_from_username('johnmill28')
    'johnmill28@yopmail.com'
    >>> generate_email_from_username('alejreye82')
    'alejreye82@temp-mail.org'
    """
    return f'{username}@{random.choice(MAIL_DOMAINS)}'


__all__ = [
    'STARTS',
    'ACTIONS',
    'TOPICS',
    'DETAILS',
    'HASHTAGS',
    'COMMENTS',
    'NAMES',
    'SURNAMES',
    'MAIL_DOMAINS',
    'generate_comment',
    'generate_email_from_username',
    'generate_fullname',
    'generate_paragraph',
    'generate_sentence',
    'generate_username_from_fullname',
]

__version__ = '0.1.0'

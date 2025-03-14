import pytest

from dummy_text_generator import (
    generate_comment,
    generate_email_from_username,
    generate_fullname,
    generate_paragraph,
    generate_sentence,
    generate_username_from_fullname,
)
from dummy_text_generator.mail_domains import MAIL_DOMAINS
from dummy_text_generator.names import NAMES, SURNAMES


class TestSentenceGeneration:
    def test_default_sentence_generation(self):
        sentence = generate_sentence()
        assert isinstance(sentence, str)
        assert len(sentence) > 0

    @pytest.mark.parametrize('lang', ['en', 'es', 'fr', 'de'])
    def test_sentence_generation_different_languages(self, lang):
        sentence = generate_sentence(lang=lang)
        assert isinstance(sentence, str)
        assert len(sentence) > 0

    def test_sentence_generation_with_topic(self):
        topic = 'the technology'
        sentence = generate_sentence(topic=topic)
        assert topic in sentence.lower()

    def test_sentence_generation_with_hashtag(self):
        sentence = generate_sentence(add_hashtag=True)
        assert '#' in sentence

    def test_invalid_language_raises_error(self):
        with pytest.raises(KeyError):
            generate_sentence(lang='invalid')


class TestParagraphGeneration:
    def test_default_paragraph_generation(self):
        paragraph = generate_paragraph()
        assert isinstance(paragraph, str)
        assert len(paragraph.split('\n')) == 3  # default sentences = 3

    @pytest.mark.parametrize('sentences', [1, 2, 5])
    def test_paragraph_with_different_sentence_counts(self, sentences):
        paragraph = generate_paragraph(sentences=sentences)
        assert len(paragraph.split('\n')) == sentences

    @pytest.mark.parametrize('lang', ['en', 'es', 'fr', 'de'])
    def test_paragraph_generation_different_languages(self, lang):
        paragraph = generate_paragraph(lang=lang)
        assert isinstance(paragraph, str)
        assert len(paragraph.split('\n')) == 3

    def test_paragraph_generation_with_topic(self):
        topic = 'the sports'
        paragraph = generate_paragraph(topic=topic)
        assert topic in paragraph.lower()

    def test_invalid_language_raises_error(self):
        with pytest.raises(KeyError):
            generate_paragraph(lang='invalid')


class TestCommentGeneration:
    def test_default_comment_generation(self):
        comment = generate_comment()
        assert isinstance(comment, str)
        assert len(comment) > 0

    @pytest.mark.parametrize('lang', ['en', 'es', 'fr', 'de'])
    def test_comment_generation_different_languages(self, lang):
        comment = generate_comment(lang=lang)
        assert isinstance(comment, str)
        assert len(comment) > 0

    def test_comment_generation_with_topic(self):
        topic = 'the music'
        comment = generate_comment(topic=topic)
        assert topic in comment.lower()

    def test_invalid_language_raises_error(self):
        with pytest.raises(KeyError):
            generate_comment(lang='invalid')


class TestNameGeneration:
    def test_default_fullname_generation(self):
        name = generate_fullname()
        assert isinstance(name, str)
        assert len(name.split()) == 2  # Should have first and last name

    @pytest.mark.parametrize('lang', ['en', 'es', 'fr', 'de'])
    def test_fullname_generation_different_languages(self, lang):
        name = generate_fullname(lang=lang)
        first_name, last_name = name.split()
        assert first_name in NAMES[lang]
        assert last_name in SURNAMES[lang]

    def test_invalid_language_raises_error(self):
        with pytest.raises(KeyError):
            generate_fullname(lang='invalid')


class TestUsernameGeneration:
    @pytest.mark.parametrize(
        'fullname',
        [
            'John Miller',
            'Ana Rodriguez',
            'Bob Smith',
        ],
    )
    def test_username_generation(self, fullname):
        EXPECTED_LENGTH = 10
        username = generate_username_from_fullname(fullname)
        assert len(username) == EXPECTED_LENGTH
        name, surname = fullname.split(' ', 1)
        assert username[:8].startswith(name[:4].lower() + surname[:4].lower())
        assert username[-2:].isdigit()

    def test_username_handles_spaces(self):
        username = generate_username_from_fullname('Mary Jane Smith')
        assert len(username) == 10
        assert username[:4] == 'mary'
        assert username[4:8] == 'jane'
        assert username[-2:].isdigit()


class TestEmailGeneration:
    def test_email_generation(self):
        username = 'johnmill28'
        email = generate_email_from_username(username)
        assert '@' in email
        assert email.startswith(username)
        domain = email.split('@')[1]
        assert domain in MAIL_DOMAINS

    @pytest.mark.parametrize(
        'username',
        ['test123', 'user_name', 'john.doe'],
    )
    def test_email_generation_different_usernames(self, username):
        email = generate_email_from_username(username)
        assert email.startswith(username)
        assert '@' in email
        domain = email.split('@')[1]
        assert domain in MAIL_DOMAINS


class TestIntegrationScenarios:
    def test_full_generation_flow(self):
        # Generate a full name
        fullname = generate_fullname()
        assert isinstance(fullname, str)
        assert len(fullname.split()) == 2

        # Generate username from the full name
        username = generate_username_from_fullname(fullname)
        assert isinstance(username, str)
        assert len(username) == 10

        # Generate email from username
        email = generate_email_from_username(username)
        assert isinstance(email, str)
        assert '@' in email

        # Generate a comment
        comment = generate_comment()
        assert isinstance(comment, str)
        assert len(comment) > 0

        # Generate a paragraph
        paragraph = generate_paragraph()
        assert isinstance(paragraph, str)
        assert len(paragraph.split('\n')) == 3

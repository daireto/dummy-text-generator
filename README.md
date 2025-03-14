<!-- omit in toc -->
# Dummy Text Generator

A Python library for generating random texts, sentences, paragraphs, comments,
and names in multiple languages like English, Spanish, French, and German.

The generated content is assembled using predefined templates and words. It does
not use any machine learning models or external APIs. It is intended for
generating dummy content for testing and development purposes.

<!-- omit in toc -->
## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
    - [Basic Examples](#basic-examples)
    - [Available Languages](#available-languages)
    - [Available Topics](#available-topics)
- [API Reference](#api-reference)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Features

- Generate random sentences with customizable topics
- Create paragraphs with multiple sentences
- Generate engaging comments about specific topics
- Create random full names based on language/region
- Generate usernames from full names
- Generate email addresses from usernames
- Support for multiple languages:
  - English (en)
  - Spanish (es)
  - French (fr)
  - German (de)

## Installation

```bash
pip install dummy-text-generator
```

## Usage

### Basic Examples

```python
from dummy_text_generator import (
    generate_comment,
    generate_email_from_username,
    generate_fullname,
    generate_paragraph,
    generate_sentence,
    generate_username_from_fullname,
)

# Generate a random sentence in English
sentence = generate_sentence(lang='en')
# Output: "Today I was thinking about how amazing it is to learn something new about technology and discovered something surprising."

# Generate a sentence about a specific topic with a hashtag
sentence = generate_sentence(lang='es', topic='los deportes', add_hashtag=True)
# Output: "Hoy estuve pensando en lo increíble que es aprender algo nuevo sobre deportes y descubrí algo sorprendente. #Increible"

# Generate a paragraph with multiple sentences
paragraph = generate_paragraph(lang='en', sentences=3)
# Output: Multiple sentences about random topics

# Generate a comment about a specific topic
comment = generate_comment(lang='fr', topic='la technologie')
# Output: "J'aime tout ce qui concerne technologie. Il y a toujours quelque chose nouveau à découvrir !"

# Generate a random full name
name = generate_fullname(lang='de')
# Output: "Franziska Schneider"

# Generate a username from a full name
username = generate_username_from_fullname("John Miller")
# Output: "johnmill28"

# Generate an email from a username
email = generate_email_from_username("johnmill28")
# Output: "johnmill28@example.com"
```

> [!NOTE]
> It is recommended to add the article before the topic,
> for example, **"the sports"** instead of **"sports"**.

### Available Languages

- `en`: English
- `es`: Spanish
- `fr`: French
- `de`: German

### Available Topics

The library includes a wide range of topics such as:
- Technology
- Travel
- Cooking
- Sports
- Music
- Science
- Fashion
- Art
- And many more...

## API Reference

<!-- omit in toc -->
#### `generate_sentence(lang='en', topic=None, add_hashtag=False)`
Generates a random sentence.
- `lang`: Language code (default: 'en')
- `topic`: Specific topic (optional)
- `add_hashtag`: Add a random hashtag at the end (default: False)

<!-- omit in toc -->
#### `generate_paragraph(lang='en', sentences=3, topic=None)`
Generates a random paragraph.
- `lang`: Language code (default: 'en')
- `sentences`: Number of sentences (default: 3)
- `topic`: Specific topic (optional)

<!-- omit in toc -->
#### `generate_comment(lang='en', topic=None)`
Generates a random comment about a topic.
- `lang`: Language code (default: 'en')
- `topic`: Specific topic (optional)

<!-- omit in toc -->
#### `generate_fullname(lang='en')`
Generates a random full name based on the specified language/region.
- `lang`: Language code (default: 'en')

<!-- omit in toc -->
#### `generate_username_from_fullname(fullname)`
Generates a username from a given full name.
- `fullname`: Full name string

<!-- omit in toc -->
#### `generate_email_from_username(username)`
Generates an email address from a username.
- `username`: Username string

## Error Handling

The library raises `KeyError` when an unsupported language code is provided.

## Contributing

Contributions are welcome! Feel free to:
- Add support for new languages.
- Expand or modify the existing vocabulary.
- Improve generation algorithms.
- Fix bugs or suggest improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE)
file for details.

## Support

If you find this project useful, give it a ⭐ on GitHub!

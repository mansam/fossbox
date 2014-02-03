"""
Libravatar plugin for Pelican
=============================

This plugin assigns the ``author_gravatar`` variable to the Libravatar URL and
makes the variable available within the article's context.
"""

import hashlib
import six

from pelican import signals


def add_libravatar(generator, metadata):

    #first check email
    if 'email' not in metadata.keys():
        if 'AUTHOR_EMAILS' in generator.settings:
            if 'author' in metadata:
                author = metadata['author']
                metadata['email'] = generator.settings['AUTHOR_EMAILS'].get(author, '')
        elif 'AUTHOR_EMAIL' in generator.settings:
            metadata['email'] = generator.settings['AUTHOR_EMAIL']

    #then add gravatar url
    if 'email' in metadata.keys():
        email_bytes = six.b(metadata['email']).lower()
        gravatar_url = "http://cdn.libravatar.org/avatar/" + \
                        hashlib.md5(email_bytes).hexdigest()
        metadata["author_gravatar"] = gravatar_url


def register():
    signals.article_generator_context.connect(add_libravatar)

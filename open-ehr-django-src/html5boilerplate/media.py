# Usage:

# Either use this file wholesale:

# from html5boilerplate.media import HTML5_MEDIA_BUNDLES
# MEDIA_BUNDLES += HTML5_MEDIA_BUNDLES

# Or copy the required parts from below to your MEDIA_BUNDLES in settings.py

_js_head_bundle = (
    'js/libs/modernizr-2.0.min.js',
    'js/libs/respond.js',
)

_js_main_bundle = (
    {'filter': 'mediagenerator.filters.media_url.MediaURL'},
    'js/libs/jquery-1.6.1.js',
    'js/plugins.js',
    'js/script.js',
)

HTML5_MEDIA_BUNDLES = (
    ('style.css',
        'css/style.css',
    ),

    ('head-ie.js',)
        + _js_head_bundle,
    ('main-ie.js',)
        + _js_main_bundle,
    ('main.js',)
        + _js_head_bundle
        + _js_main_bundle,
)

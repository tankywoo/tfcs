# Flask Code Snippet #

Collect code snippet, powered by [Flask](http://flask.pocoo.org/)

**WARNING**: Write this just for fun, and not stable, be used with caution...

## Config ##

* `configs.py`: set `SNIPPETS_ROOT`, root path of snippets.
* `site.yaml`: set `title`, used by template, site title.
* `uwsgi.ini`: set `base`, `home` by comment.

## Snippet Format ##

    ---
    title: 'xxx'
    description: 'xxx'
    tag: xxx1,xxx2
    date: 2015-10-23 00:00
    id: xxx
    ---

    ...
    ...

<!-- -->

* `title`: snippet post title
* `description`: optional, not used by now
* `tag`: optional, as keyword, separated by comma
* `date`: datetime format in `YYYY-MM-DD HH:MM`
* `id`: 8-digits letters or digits

Generate random 8-digits id:

    $ python -c "import string,random; print ''.join(random.choice(string.ascii_letters + string.digits) for x in range(8))"

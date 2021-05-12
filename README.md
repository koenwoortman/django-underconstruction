# 🛠️ Django Under Construction
> *Put your Django website "under construction" with a single setting.*

[![PyPI](https://img.shields.io/pypi/v/django-underconstruction?color=blue)](https://pypi.org/project/django-underconstruction/)
[![Build Status](https://travis-ci.org/koenwoortman/django-underconstruction.svg?branch=main)](https://travis-ci.org/koenwoortman/django-underconstruction)

<div align="center">
	<div>
		<img src="https://github.com/koenwoortman/django-underconstruction/raw/main/media/screenshot.png" alt="Example screenshot">
	</div>
	<br>
	<br>
</div>

## Install

Install the package from [pypi](https://pypi.org/project/django-underconstruction/).

```
$ pip install django-underconstruction
```

Add `django_underconstruction` to your INSTALLED_APPS.

```python
# settings.py

INSTALLED_APPS = [
    ...
    'django_underconstruction',
    ...
]
```

Add the `UnderConstructionMiddleware` middleware class to your MIDDLEWARE.

```python
# settings.py

MIDDLEWARE = [
    ...
    'django_underconstruction.middleware.UnderConstructionMiddleware',
    ...
]
```

Once you set `settings.UNDER_CONSTRUCTION` to `True` the under construction page is shown.

```python
# settings.py

UNDER_CONSTRUCTION = not DEBUG
```

## Settings

| Option                            | Description                                     | Default        |
| :-------------------------------- | :---------------------------------------------- | :------------- |
| **`UNDER_CONSTRUCTION`**          | Whether the site is under construction.         | `False`    |
| **`UNDER_CONSTRUCTION_TEMPLATE`** | HTML template to show while under construction. | `'django_underconstruction/construction.html'`    |


## License

Released under the [MIT license](https://github.com/koenwoortman/django-underconstruction/blob/main/LICENSE).

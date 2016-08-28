# sw-delta-python

**sw-delta-python** is a Python server-side implementation for **sw-delta**.

**sw-delta** is a browser cache - based on a Service Worker - that only loads the delta (=diff) of a file when it's modified.

Please have a look at [the sw-delta repository](https://github.com/gmetais/sw-delta) for more information.


## Usage example with Flask

```Python
from flask import Flask, Response, request
from sw_delta import get_delta

app = Flask(__name__)

@app.route('/assets/scripts/<name>-<version>.js')
def get_script_diff(name, version):

    cached_version = request.args.get('cached')

    print("Asked version: %s - Cached version: %s" % (version, cached_version))

    filename = "%s-%s.js" % (name, version)
    asked_file_path = "/your/folder/%s" % filename
    cached_file_path = "/your/folder/%s" % filename.replace(version, cached_version)

    try:
        body, mimetype = get_delta(asked_file_path, cached_file_path)
    except IOError as ex:
        print("Something went wrong: %r" % ex)
        return Response("Bad request", status=400)
    else:
        return Response(body, status=200, content_type=mimetype)

```

## How to run tests (nose)

```Python
pip install -r requirements-dev.txt
nosetests

```

## API explanation

### sw_delta.get_delta(asked_file_path, cached_file_path)

The function checks if both files exist and calculates the delta between them. `asked_file_path` and `cached_file_path` need to be file system paths of the files on your server.

It returns a tuple containing the resulting body and its content type.

```js
body, mimetype = sw_delta.get_delta(file1, file2)
```

**Exceptions:**
- `InvalidAskedFile` - when the asked file doesn't exist (extends IOError).
- `InvalidCachedFile` - when the cached file doesn't exist (extends IOError)..



## Author
Alex Casalboni. I'm a software engineer at Cloud Academy. Follow me on Twitter [@alex_casalboni](https://twitter.com/alex_casalboni).

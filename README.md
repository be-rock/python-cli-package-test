# python-cli-package-test

> ref:
> 
> https://pybit.es/articles/how-to-package-and-deploy-cli-apps/

## testing

```bash
pip install build
python -m build
```

This will result in two output files in the dist directory:

```shell
dist/mypackage-0.0.1.tar.gz
dist/mypackage-0.0.1-py3-none-any.whl
```

Then in a new virtual environment:
```shell
python -m venv ~/.venv/test1
source ~/.venv/test1/bin/activate
pip install dist/mypackage-0.0.1-py3-none-any.whl
```

Then run the executable as named in the `setup.cfg`
```shell
my-application
hello world
```
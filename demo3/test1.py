import functools

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text if text is not None else 'call', func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('hello')

now()

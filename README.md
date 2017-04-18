Aiomandrill is a Python API client for the Mandrill email as a platform service.

It is based on original Mandrill Python API [library](https://bitbucket.org/mailchimp/mandrill-api-python) and [aiohttp](https://github.com/aio-libs/aiohttp).

Examples:

```python
import asyncio
import aiomandrill


@asyncio.coroutine
def main():
    m = aiomandrill.Mandrill('YOUR_API_KEY')
    pong = yield from m.users.ping()
    print(pong)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

TODO:
* Write docs
* Update aiohttp library to the latest version

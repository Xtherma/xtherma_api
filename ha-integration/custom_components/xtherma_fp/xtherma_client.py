"""
REST API client for Xtherma Fernportal cloud integration
"""

import asyncio
import aiohttp
import datetime

from .const import LOGGER

class RateLimitError(Exception):
    def __init__(self):
        super().__init__("API is busy")

class GeneralError(Exception):
    def __init__(self, code: int):
        super().__init__("General error")
        self.code = code

class TimeoutError(Exception):
    def __init__(self):
        super().__init__("timeout")

class XthermaClient:
    def __init__(self, url: str, api_key: str, serial_number: str, session: aiohttp.ClientSession):
        self._url = f"{url}/{serial_number}"
        self._api_key = api_key
        self._session = session

    def _now(self) -> int:
        return int(datetime.datetime.now(datetime.timezone.utc).timestamp())

    async def async_get_data(self):
        headers = {"Authorization": f"Bearer {self._api_key}"}
        try:
            # return test_data
            async with self._session.get(self._url, headers=headers) as response:
                response.raise_for_status()
                data = await response.json()
                self._ts_last_request = self._now()
                return data
        except aiohttp.ClientResponseError as err:
            LOGGER.error("API error: %s", err)
            if err.status == 429:
                raise RateLimitError()
            raise GeneralError(err.status)
        except asyncio.TimeoutError:
            LOGGER.error("API request timed out")
            raise TimeoutError()
        except Exception as err:
            LOGGER.error("Unknown API error: %s", err)
            return None

async def test():
    from const import FERNPORTAL_URL, KEY_DATA, KEY_DB_DATA, KEY_ENTRY_NAME, KEY_ENTRY_UNIT, KEY_ENTRY_VALUE
    import os
    api_key = os.environ['API_KEY']
    serial_number = os.environ['SERIAL_NUMBER']
    print("creating client session")
    session = aiohttp.ClientSession()
    print("creating instance")
    inst = XthermaClient(url=FERNPORTAL_URL, api_key=api_key, serial_number=serial_number, session=session)
    print("request data")
    raw = await inst.async_get_data()
    print(raw)
    for e in raw[KEY_DATA]:
        print(e[KEY_ENTRY_NAME], "=", e[KEY_ENTRY_VALUE], e[KEY_ENTRY_UNIT])
    for e in raw[KEY_DB_DATA]:
        print(e[KEY_ENTRY_NAME], "=", e[KEY_ENTRY_VALUE], e[KEY_ENTRY_UNIT])

if __name__ == "__main__":
    asyncio.run(test())

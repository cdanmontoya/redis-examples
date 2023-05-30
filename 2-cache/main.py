import time

import redis

from loguru import logger

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def expensive_function(delay: int = 5) -> dict:
    logger.error("Ejecutando una función muy demorada")
    time.sleep(delay)

    return {'name': 'John', 'surname': 'Smith', 'company': 'Redis', 'age': '29'}


def query(param: str):
    logger.info('Consultando el valor')

    if not r.exists(param):
        res = expensive_function()
        logger.error('Valor retornado')
        r.hset(param, mapping=res)

    else:
        logger.info('Obteniendo el valor desde la caché')
        return r.hgetall(param)


query('jojo')
query('jojo')

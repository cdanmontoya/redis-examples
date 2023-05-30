import redis

from loguru import logger

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

logger.warning('Inserción clave-valor de un primitivo')
logger.info('Asignando a la clave foo el valor bar')
r.set('foo', 'bar')
print(r.get('foo'))


logger.warning('Inserción clave-valor de un diccionario')
sample_dict = {
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
}
logger.info(f'Asignando a la clave "user-session:123" el objeto {sample_dict}')

r.hset('user-session:123', mapping=sample_dict)
print(r.hgetall('user-session:123'))
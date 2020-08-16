import os


class SystemConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/scp_db?charset=utf8'.format(**{
      'user': os.getenv('DB_USER','administrator'),
      'password': os.getenv('DB_PASSWORD','adminal'),
      'host': os.getenv('DB_HOST','localhost'),
  })

Config = SystemConfig
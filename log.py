#123
import logging

#logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'mylog.log')

# Сообщение отладочное
logging.debug( u'This is a debug message' )
# Сообщение информационное
logging.info( u'This is an info message' )
# Сообщение предупреждение
logging.warning( u'This is a warning' )
# Сообщение ошибки
logging.error( u'This is an error message' )
# Сообщение критическое
logging.critical( u'FATAL!!!' )

#branch master
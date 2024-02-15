import logging


class ErrorLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        print(dir(record))
        return record.levelname == 'ERROR' and 'важно' in record.msg.lower()


logger = logging.getLogger(__name__)

stderr_handler = logging.StreamHandler()

stderr_handler.addFilter(ErrorLogFilter())

logger.addHandler(stderr_handler)



logger.warning('важно')
logger.error('важно')


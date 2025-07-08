import logging.config
from pathlib import Path

logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
root_logger = logging.getLogger('root')
sample_logger = logging.getLogger('sampleLogger')

root_logger.warning("Root - Warning")
root_logger.warning("SampleLogger - Warning")

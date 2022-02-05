"""Running the Xetra ETL application"""
import logging
import logging.config

from pyyaml import yaml

def main():
    """
    entry point to run the extra ETL job
    """
    # Parsing YAML file
    config_path = 'C:/Daten/xetra_project/xetra_1234/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")


if __name__ == '__main__':
    main()
# import dotenv
import logging
import os

import hydra
from hydra import utils as hydra_utils
from omegaconf import DictConfig, OmegaConf

from src import utils
from src.experiment_manager import ExperimentManager

log = utils.get_pylogger(__name__)

# load environment variables from `.env` file if it exists
# recursively searches for `.env` in all folders starting from work dir
# dotenv.load_dotenv(override=True)


@hydra.main(version_base="1.2", config_path="configs/", config_name="default_config.yaml")
def main(config: DictConfig):

    # pretty print config tree using Rich library
    if config.extras.get("print_config"):
        log.info("Printing config tree with Rich! <cfg.extras.print_config=True>")
        utils.print_config_tree(config, resolve=True, save_to_file=True)

    experiment_manager = ExperimentManager(config)
    experiment_manager.init_experiment()
    experiment_manager.start_experiment()
    experiment_manager.finish_experiment()

    # log.info(OmegaConf.to_yaml(config))
    # log.info(config.paths.root_dir)
    # log.info(config.paths.project_dir)
    # log.info(f'Data dir: {config.paths.data_dir}')
    # log.info(f'Logs dir: {config.paths.log_dir}')
    # log.info(f'Output dir: {config.paths.output_dir}')
    # log.info("Working directory : {}".format(os.getcwd()))
    # log.info("Current working directory  : {}".format(os.getcwd()))
    # log.info("Original working directory : {}".format(hydra_utils.get_original_cwd()))
    # log.info("to_absolute_path('foo')    : {}".format(hydra_utils.to_absolute_path("foo")))
    # log.info("to_absolute_path('/foo')   : {}".format(hydra_utils.to_absolute_path("/foo")))


if __name__ == "__main__":
    main()

from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareBaseModel
from deepClassifier import logger


STAGE_NAME = "Prepare Base Model Stage"


def main():
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"{'>>'*30} stage {STAGE_NAME} started {'>>'*30}")
        main()
        logger.info(f"{'>>'*30} stage {STAGE_NAME} Completed {'>>'*30}")
    except Exception as e:
        logger.info(e)

        raise e
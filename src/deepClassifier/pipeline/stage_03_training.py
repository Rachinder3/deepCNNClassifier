from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareCallback
from deepClassifier import logger
from deepClassifier.components import Training

STAGE_NAME = "Training Stage"


def main():
   config = ConfigurationManager()
   prepare_callbacks_config = config.get_prepare_callback_config()
   prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
   callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
   
   training_config = config.get_training_config()
   training = Training(config=training_config)
   training.get_base_model()
   training.train_valid_generator()
   training.train(
        callback_list=callback_list
    )
    
if __name__ == "__main__":
    try:
        logger.info(f"{'>>'*30} stage {STAGE_NAME} started {'>>'*30}")
        main()
        logger.info(f"{'>>'*30} stage {STAGE_NAME} Completed {'>>'*30}")
    except Exception as e:
        logger.info(e)

        raise e
from sleep_efficiency.config.configuration import ConfigurationManager
from sleep_efficiency.components.model_evaluation import ModelEvaluation
from sleep_efficiency import logger

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_evaluation_config()
        model_trainer_config = ModelEvaluation(config=model_trainer_config)
        model_trainer_config.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
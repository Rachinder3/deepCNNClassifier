import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from deepClassifier.entity import TrainingConfig
from pathlib import Path

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255, # rescales images by this factor
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1], # Here channels not required, hence removing that dimension. This reshapes different sized images to the same dimension.
            batch_size=self.config.params_batch_size,
            interpolation="bilinear" # Using 2 points(bilinear), you want to create more points. Given an M-D point set, this function can be used to generate a new point set that is formed by interpolating a subset of points in the set.
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation", ## giving name to the subset
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40, ## rotate image by 40 radians
                horizontal_flip=True, ## flip horizontal
                width_shift_range=0.2, ## do we want to zoom in
                height_shift_range=0.2, 
                shear_range=0.2, ## just like sheer force in physics, we can apply here as well and tilt the ima
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        ### What data generator will do: At every epoch, it will give a different version of same image for training
        ### This makes the model very robust. Also helps where we don't have huge ammount of data
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)


    def train(self, callback_list: list):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )
# deep classifier project

## workflow

1. Update config.yaml

2. updation secrets.yaml (haven't been used in this project) [optional]

3. Update params.yaml

4. Go to src, then update the entity

5. Update Configuration manager in config.yaml

6. Update the components

7. Update the pipeline 

8. Test run pipeline stage.

9. Run tox for testing of package

10. May have created main.py, can update that. In this project, we are doing orchestration with dvc instead. Hence we update dvc.yaml instead.

11. rub "dvc repro" command for running all the stages in pipeline.



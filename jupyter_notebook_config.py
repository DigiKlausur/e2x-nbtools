from e2x_nbtools.contents.filecheckpoints import E2XFileCheckpoints

c = get_config()

c.ContentsManager.checkpoints_class = E2XFileCheckpoints
c.ContentsManager.checkpoints_class.number_of_checkpoints = 3

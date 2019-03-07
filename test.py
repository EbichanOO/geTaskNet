from neural_mmo.forge.trinity import smith, Trinity, Pantheon, God, Sword
trinity = Trinity(Pantheon, God, Sword)
envs = smith.Native(config, args, trinity)
envs.run()
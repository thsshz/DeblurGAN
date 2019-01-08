from .conditional_gan_model import ConditionalGAN

def create_model(opt):
	model = None
	if opt.model == 'test':
		assert (opt.dataset_mode == 'single')
		from .test_model import TestModel
		model = TestModel()
	elif opt.model == 'test_effect':
		assert (opt.dataset_mode == 'double')
		from .test_effect_model import TestEffectModel
		model = TestEffectModel()
	else:
		model = ConditionalGAN()
	model.initialize(opt)
	print("model [%s] was created" % (model.name()))
	return model

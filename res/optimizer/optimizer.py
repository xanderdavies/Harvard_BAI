import copy
import logging
import functools

from torch.optim import SGD
from torch.optim import Adam
from torch.optim import ASGD
from torch.optim import Adamax
from torch.optim import Adadelta
from torch.optim import Adagrad
from torch.optim import RMSprop

key2opt =  {'sgd': SGD,
            'adam': Adam,
            'asgd': ASGD,
            'adamax': Adamax,
            'adadelta': Adadelta,
            'adagrad': Adagrad,
            'rmsprop': RMSprop,}

def get_optimizer(opt_name):
    if opt_name not in key2opt:
        raise NotImplementedError('Optimizer {} not implemented'.format(opt_name))

    opt = key2opt[opt_name]
    return opt

# def exp_lr_scheduler(optimizer, epoch, init_lr=BASE_LR, lr_decay_epoch=EPOCH_DECAY):
#     """Decay learning rate by a factor of DECAY_WEIGHT every lr_decay_epoch epochs."""
#     lr = init_lr * (DECAY_WEIGHT**(epoch // lr_decay_epoch))
#
#     if epoch % lr_decay_epoch == 0:
#         print('LR is set to {}'.format(lr),file = LOG_FILE, flush = True)
#         sys.stdout.flush()
#
#     for param_group in optimizer.param_groups:
#         param_group['lr'] = lr
#
#     return optimizer

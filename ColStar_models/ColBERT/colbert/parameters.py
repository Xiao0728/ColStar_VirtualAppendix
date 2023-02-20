import torch

DEVICE = torch.device("cuda")

SAVED_CHECKPOINTS = [32*1000,100*1000,110*1000, 120*1000, 130*1000,140*1000, 150*1000, 160*1000, 170*1000,180*1000,190*1000]
SAVED_CHECKPOINTS += [200*1000,210*1000, 220*1000, 230*1000, 240*1000,250*1000,260*1000,270*1000, 280*1000,290*1000]
SAVED_CHECKPOINTS += [300*1000,310*1000,320*1000, 330*1000, 340*1000,350*1000,380*1000, 400*1000,430*1000]
SAVED_CHECKPOINTS += [450*1000,480*1000, 500*1000,550*1000,600*1000,650*1000, 700*1000, 750*1000, 800*1000]
SAVED_CHECKPOINTS += [10*1000, 20*1000, 30*1000, 40*1000, 44*1000, 50*1000, 60*1000, 70*1000, 80*1000, 90*1000]
SAVED_CHECKPOINTS += [25*1000, 55*1000, 75*1000]
SAVED_CHECKPOINTS = set(SAVED_CHECKPOINTS)
"""
    Main file to execute PPO algorithm
"""

import torch.optim as optim
from ppo import *
from network import *

# tolerance for std
EPS = 1e-6

# discount function
gamma = 0.99
# TD_lambda method factor
lambda_ = 0.97
# no of patches at the surface of cylinder
n_sensor = 54

# coefficients for reward function
r_1 = 3
r_2 = 0.1

# policy model and value model instances
policy_model = FCCA(n_sensor, 64)
value_model = FCV(n_sensor, 64)

# no of workers
n_worker = 1
# no of total buffer size
buffer_size = 3
# range to randomly start control
control_between = [0.1, 4]
# env instance
env = env(n_worker, buffer_size, control_between)

# learning rate for policy model and value model
policy_lr = 0.006
value_lr = 0.003

# policy optimizer
policy_optimizer = optim.Adam(policy_model.parameters(), policy_lr)
# no of epochs for value model
policy_optimization_epochs = 80
# ration for no of trajectory to take for training (1 = 100%)
policy_sample_ratio = 1
# clipping parameter of policy loss
policy_clip_range = 0.1
# maximum norm tolerance of policy optimization
policy_model_max_grad_norm = float('inf')
# tolerance for training of policy net
policy_stopping_kl = 0.2
# factor for entropy loss
entropy_loss_weight = 0.01

# value optimizer
value_optimizer = optim.Adam(value_model.parameters(), policy_lr)
# no of epochs for value model
value_optimization_epochs = 80
# ration for no of trajectory to take for training (1 = 100%)
value_sample_ratio = 1
# clipping parameter of value model loss
value_clip_range = float('inf')
# maximum norm tolerance of value optimization
value_model_max_grad_norm = float('inf')
# tolerance for trainig of value net
value_stopping_mse = 25

# main PPO algorithm iteration
main_ppo_iteration = 10

evaluation_score = []

# iteration for PPO algorithm
for i in range(main_ppo_iteration):
    sample = i
    train_model(value_model,
                policy_model,
                env,
                policy_optimizer,
                policy_optimization_epochs,
                policy_sample_ratio,
                policy_clip_range,
                policy_model_max_grad_norm,
                policy_stopping_kl,
                entropy_loss_weight,
                value_optimization_epochs,
                value_optimizer,
                value_sample_ratio,
                value_clip_range,
                value_model_max_grad_norm,
                value_stopping_mse,
                gamma,
                lambda_,
                r_1,
                r_2,
                sample,
                n_sensor,
                EPS,
                evaluation_score)
    print(f'The Iteration {sample} is completed')

import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PFPC experiments.')
    parser.add_argument('--device', type=str, default=None)
    parser.add_argument('--start_seed', type=int, default=None)
    parser.add_argument('--end_seed', type=int, default=None)
    args = parser.parse_args()
    for i in range(args.start_seed, args.end_seed):
        os.system('python code/synthetic_experiment.py --seed {} --config lorenz_stochastic_infonce_exploration --device {}'
                  .format(i, args.device))

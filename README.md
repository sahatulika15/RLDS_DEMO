# RLDMS

## This is the readme file that contains the guidelines and information about the compilation the code of the following paper

**Paper Name:-** Reinforcement Learning Based Dialogue Management Strategy
>This paper proposes a novel Markov Decision Process (MDP) to solve the problem of learning an optimal strategy by a Dialogue Manager for a flight enquiry system. A unique representation of state is presented followed by a relevant action set and a reward model which is specific to different time-steps. Different Reinforcement Learning (RL) algorithms based on classical methods and Deep Learning techniques have been implemented for the execution of the Dialogue Management component. To establish the robustness of the system, existing Slot-Filling (SF) module has been integrated with the system. The system can still generate valid responses to act sensibly even if the SF module falters. The experimental results indicate that the proposed MDP and the system hold promise to be scalable across satisfying the intent of the user.

* **Authors:** Tulika Saha, Dhawal Gupta, Sriparna Saha and Pushpak Bhattacharyya
* **Affiliation:** Indian Institute of Technology Patna, India
* **Corresponding Author:** [Tulika Saha] (sahatulika15@gmail.com / pratik.pcs16@iitp.ac.in)
* **Accepted(August, 2018):**  [International Conference on Neural Information Processing], ICONIP, 2018, pp 359-372

If you consider this work as useful, please cite it as
```bash
@InProceedings{10.1007/978-3-030-04182-3_32,
author="Saha, Tulika and Gupta, Dhawal and Saha, Sriparna and Bhattacharyya, Pushpak",
editor="Cheng, Long and Leung, Andrew Chi Sing and Ozawa, Seiichi",
title="Reinforcement Learning Based Dialogue Management Strategy",
booktitle="Neural Information Processing",
year="2018",
publisher="Springer International Publishing",
address="Cham",
pages="359--372",
isbn="978-3-030-04182-3"
}
```

## Prerequisities
* **[Python 2.7+](https://www.python.org/downloads/release/python-2713/)**
* **[sklearn](https://scikit-learn.org/stable/install.html)**
* **[keras 2.0+]**
* **[tensorflow]**
* **[numpy 1.10+](https://pypi.org/project/numpy/)**




# How to replicate for the given model
The name of the folder describes the type of implementation.</br>
* SVM : uses SVM
* woSVM : doesn't use SVM
* PER : Uses Priority Experience Replay
* DDQN : Works on the Double DQN algorithm
* DQN : Works on the DQN algorithm
This describes how to train the model and test the model with differet reward functions

## Training
1. Training with old reward of +-1 
```
python train_modified.py
```

2. Training with the new reward
```
python train_modified1.py
```

The models of each are stored in ./save/ folder along with the time_date and model architecture information


## Testing

The model can be tested to see the actions taken using the  following script

```
python test_policy.py ./save/<model_name>
```



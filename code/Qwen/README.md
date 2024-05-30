
## Code

When running the inference code for each MLLM, please refer to the instruction in the corresponding projects ([GPT-4V](https://platform.openai.com/docs/models), [BLIP-2](https://github.com/salesforce/LAVIS/tree/main/projects/blip2), [InstructBLIP](https://github.com/salesforce/LAVIS/tree/main/projects/instructblip), [LLaVA](https://github.com/haotian-liu/LLaVA?tab=readme-ov-file), [Qwen-VL](https://github.com/QwenLM/Qwen-VL), and [Qwen-VL-Chat](https://github.com/QwenLM/Qwen-VL)) for environment setup and package installation. 

Here we provide an example for running the inference & evaluation code for Qwen-VL:

## Setup
### Install Package 
```bash
conda create -n Qwen python=3.9 -y
conda activate Qwen

# install pytorch
conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 pytorch-cuda=11.8 -c pytorch -c nvidia

# install dependency
pip install -r requirements.txt
```

## Evaluation

To start the inference and evaluation, simply run `Qwen_VL_7B.ipynb` and `Qwen_VL_Chat.ipynb` notebooks.


You might need to change the paths to your own data paths and replace the model names with other variants you would like to use.
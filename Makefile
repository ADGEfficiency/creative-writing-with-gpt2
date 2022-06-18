app: pulls3
	streamlit run app.py

setup:
	pip3 install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio==0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

pulls3:
	pip install awscli -q
	aws s3 sync s3://adgefficiency-public/creative-writing-with-gpt2/models ./models --no-sign-request

pushs3:
	pip install awscli -q
	aws s3 sync ./models s3://adgefficiency-public/creative-writing-with-gpt2/models

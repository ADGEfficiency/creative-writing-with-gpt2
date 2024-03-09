app: setup
	streamlit run creative/app.py

setup:
	pip3 install -r requirements.txt -U
	pip3 install torch torchvision torchaudio -f https://download.pytorch.org/whl/cu113/torch_stable.html
	pip3 install -e .

lint:
	black **/*.py
	isort **/*.py

pulls3:
	aws s3 sync s3://adgefficiency-public/creative-writing-with-gpt2/models ./models --no-sign-request

pushs3:
	aws s3 sync ./models s3://adgefficiency-public/creative-writing-with-gpt2/models

suite:
	python3 creative/fine_tune.py harry
	python3 creative/fine_tune.py tolkien
	python3 creative/fine_tune.py asimov
	python3 creative/fine_tune.py bible

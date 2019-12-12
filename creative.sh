creative-write() {
if [ $1 = "gpt2" ]; then
python run_generation.py \
  --model_type=gpt2 \
  --model_name_or_path="$1" \
  --length=$2

else
python run_generation.py \
  --model_type=gpt2 \
  --model_name_or_path="./models/$1" \
  --length=$2
fi
}
alias c-write='creative-write'

creative-learn() {
python run_lm_finetuning.py \
  --output_dir="./models/$1" \
  --model_type=gpt2 \
  --model_name_or_path=gpt2 \
  --do_train \
  --train_data_file="./data/$1/clean.txt" \
  --num_train_epochs=$2 \
  --overwrite_output_dir \
  --save_steps 10000
}
alias c-learn='creative-learn'

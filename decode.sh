EXP_NAME=$1
shift
CUDA=$1
shift
MODE=$1
shift
CUDA_VISIBLE_DEVICES=$CUDA python run_summarization.py --mode=decode \
                                                       --data_path=$DATA/chunked/${MODE}_* \
                                                       --vocab_path=$DATA/vocab \
                                                       --log_root=./log \
                                                       --exp_name=$EXP_NAME \
                                                       $@

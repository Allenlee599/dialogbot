# -*- coding: utf-8 -*-
"""
@author:XuMing（xuming624@qq.com)
@description: 
"""
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

pwd_path = os.path.abspath(os.path.dirname(__file__))

# knowledge graph
host = "127.0.0.1"
kg_port = 7474
user = "neo4j"
password = "123456"
answer_num_limit = 20

# word2vec param
# train_file_path = os.path.join(pwd_path, 'data/reduce_weight/reduce_weight.txt')
# train_seg_file_path = os.path.join(pwd_path, 'data/reduce_weight/reduce_weight_seg.txt')
# train_model_path = os.path.join(pwd_path, 'data/reduce_weight/reduce_weight_model.pkl')
# emb_model_path = os.path.join(pwd_path, 'data/reduce_weight/reduce_weight_emb.bin')

# mongodb
mongo_host = 'localhost'
mongo_port = 27017

# preprocess
train_path = os.path.join(pwd_path, 'data/taobao/dev.txt')
dev_path = os.path.join(pwd_path, 'data/taobao/dev.txt')
test_path = os.path.join(pwd_path, 'data/taobao/test.txt')

question_answer_path = os.path.join(pwd_path, 'data/taobao/question_answer.txt')
context_response_path = os.path.join(pwd_path, 'data/taobao/context_response.txt')

word2vec_path = os.path.join(pwd_path, "data/taobao/v1.w2v_sgns_win2_d128.w2v")
similarity_index_path = os.path.join(pwd_path, "data/taobao/similarity_index.txt")
sent_emb_index_path = os.path.join(pwd_path, "data/taobao/sent_emb_index.txt")

# Tokenize config file
punctuations_path = os.path.join(pwd_path, "data/punctuations.txt")
stopwords_path = os.path.join(pwd_path, "data/stopwords.txt")
user_define_words_path = os.path.join(pwd_path, "data/user_define_words.txt")
remove_words_path = os.path.join(pwd_path, "data/remove_words.txt")

order_info_path = os.path.join(pwd_path, "data/order/order.txt")
# Tfidf config file
corpus_dict_path = os.path.join(pwd_path, "data/order/corpus_dict.txt")
corpus_tfidf_path = os.path.join(pwd_path, "data/order/corpus_tfidf.txt")

vocab_path = os.path.join(pwd_path, "data", "taobao/vocab.txt")


# dialog
class Params(object):
    rnn_size = 256
    num_layers = 1
    embedding_size = 300
    vocab_size = 10000
    learning_rate = 0.001
    batch_size = 80
    numEpochs = 15
    steps_per_checkpoint = 300
    model_name = "chatbot.ckpt"
    beam_size = 10
    max_gradient_norm = 5.0
    use_attention = True
    bidirectional_rnn = False

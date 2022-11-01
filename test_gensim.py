import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('model/sgns.wiki.word')
# print(model.most_similar(['男人']))     # 返回与指定词语最相近的几个词以及与对应的相似度
# print(model.similarity('男人','女人'))   # 返回给定两个词语的相似度
# print(model.index_to_key)       # 返回列表，列表中的元素是词语
# print(model.key_to_index)    #  返回字典，key是词语，value是索引（index）
print(model.vectors)    # 返回一个列表，列表中每个元素是一个向量列表
print(len(model.vectors))    # 返回词向量的个数
print(model.vector_size)    #  返回向量的维度

from DataGeneratorSeq import DataGeneratorSeq

#Long Short-Term Memory model
#predicting based on momentum
#ref: http://colah.github.io/posts/2015-08-Understanding-LSTMs/

#Formulars
#it = σ(WixXt + Wihht-1 + bi)
#c~_t=σ(W_cxx_t+W_chht−1+bc)
#f_t=σ(W_fxx_t+W_fhht−1+bf)
#ct=f_tc_t−1+itc~t
#o_t=σ(W_oxx_t+W_ohht−1+bo)
#ht=ottanh(ct)

def LSTM(train_data,batch_size,num_unroll):

    dg = DataGeneratorSeq(train_data, batch_size, num_unroll)
    u_data, u_labels = dg.unroll_batches()

    for ui,(dat,lbl) in enumerate(zip(u_data,u_labels)):   
        print('\n\nUnrolled index %d'%ui)
        dat_ind = dat
        lbl_ind = lbl
        print('\tInputs: ',dat )
        print('\n\tOutput:',lbl)
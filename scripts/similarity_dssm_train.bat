md dssm
md dssm\model

REM shuffle the training data
REM ..\..\bin\WordHash.exe --shuffle data\_myhtml.tsv data\train.sf.tsv

REM generate features
..\..\bin\WordHash.exe --pair2seqfea data\_myhtml.tsv data\l3g.txt data\l3g.txt 1 dssm\train

REM convert feature files into binary files
..\..\bin\WordHash.exe --seqfea2bin  dssm\train.src.seq.fea 1024 dssm\train.src.seq.fea.bin
..\..\bin\WordHash.exe --seqfea2bin  dssm\train.tgt.seq.fea 1024 dssm\train.tgt.seq.fea.bin

REM compute "noise distribution" which is approximated by scaled unigram distribution for NCE training.
..\..\bin\ComputelogPD.exe /i data\_myhtml.tsv /o mix\train.logpD.s75 /C 1 /S 0.75
..\..\bin\ComputelogPD.exe /i data\_myhtml.tsv /o dssm\train.logpD.s75 /C 1 /S 0.75

REM cdssm training
..\..\bin\DSSM_Train.exe similarity_dssm_config.txt

REM perform sent2vec using the trained model to dev set
..\..\bin\sent2vec /inSrcModel dssm\model\dssm_QUERY_DONE /inSrcVocab data\l3g.txt /inSrcModelType DSSM /inTgtModel dssm\model\dssm_DOC_DONE /inTgtVocab data\l3g.txt /inTgtModelType DSSM /inFilename data\_myhtml.tsv /outFilenamePrefix dssm\_myhtml.sent2vec

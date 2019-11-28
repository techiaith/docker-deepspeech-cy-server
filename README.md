# docker-deepspeech-server

```
root@cdb55156f308:/deepspeech/server# ./transcriber.py --aggressive 0 --model /deepspeech/models --audio /deepspeech/data/clips/11ca9350-8080-11e9-a63e-812683
7dd92a/288015140e31ca6859ba94c0d4284da5.wav
DEBUG:root:Transcribing audio file @ /deepspeech/data/clips/11ca9350-8080-11e9-a63e-8126837dd92a/288015140e31ca6859ba94c0d4284da5.wav
DEBUG:root:Found Model: /deepspeech/models/output_graph.pb
DEBUG:root:Found Alphabet: /deepspeech/models/alphabet.txt
DEBUG:root:Found Language Model: /deepspeech/models/lm.binary
DEBUG:root:Found Trie: /deepspeech/models/trie
TensorFlow: v1.13.1-10-g3e0cc53
DeepSpeech: v0.5.1-0-g4b29b78
Warning: reading entire model file into memory. Transform model file into an mmapped graph to reduce heap usage.
2019-11-28 13:18:54.331941: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled t
o use: AVX2 FMA
2019-11-28 13:18:54.390883: E tensorflow/core/framework/op_kernel.cc:1325] OpKernel ('op: "UnwrapDatasetVariant" device_type: "CPU"') for unknown op: UnwrapDa
tasetVariant
2019-11-28 13:18:54.390910: E tensorflow/core/framework/op_kernel.cc:1325] OpKernel ('op: "WrapDatasetVariant" device_type: "GPU" host_memory_arg: "input_hand
le" host_memory_arg: "output_handle"') for unknown op: WrapDatasetVariant
2019-11-28 13:18:54.390916: E tensorflow/core/framework/op_kernel.cc:1325] OpKernel ('op: "WrapDatasetVariant" device_type: "CPU"') for unknown op: WrapDatase
tVariant
2019-11-28 13:18:54.390972: E tensorflow/core/framework/op_kernel.cc:1325] OpKernel ('op: "UnwrapDatasetVariant" device_type: "GPU" host_memory_arg: "input_ha
ndle" host_memory_arg: "output_handle"') for unknown op: UnwrapDatasetVariant
DEBUG:root:Loaded model in 0.060s.
DEBUG:root:Loaded language model in 0.000s.
Filename                       Duration(s)          Inference Time(s)    Model Load Time(s)   LM Load Time(s)
DEBUG:root:Found Transcript @: /deepspeech/data/clips/11ca9350-8080-11e9-a63e-8126837dd92a/288015140e31ca6859ba94c0d4284da5.txt
DEBUG:root:Caught the wav file @: /deepspeech/data/clips/11ca9350-8080-11e9-a63e-8126837dd92a/288015140e31ca6859ba94c0d4284da5.wav
DEBUG:root:Processing chunk 00
DEBUG:root:Running inference...
DEBUG:root:Inference took 4.541s for 3.150s audio file.
DEBUG:root:Transcript: beth ywr newyddion chwaraeon
DEBUG:root:Expected: Beth yw'r newyddion chwaraeon?
DEBUG:root:WER: 0.5
DEBUG:root:************************************************************************************************************
DEBUG:root:Filename                       Duration(s)          Inference Time(s)    Model Load Time(s)   LM Load Time(s)
DEBUG:root:288015140e31ca6859ba94c0d4284da5.wav 3.240                4.541                0.175                0.000
DEBUG:root:************************************************************************************************************
288015140e31ca6859ba94c0d4284da5.wav 3.240                4.541                0.175                0.000

```

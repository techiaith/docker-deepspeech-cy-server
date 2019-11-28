```
root@4523baca8854:/deepspeech/server# python3 transcriber.py --audio /deepspeech/data/clips/11ca9350-8080-11e9-a63e-8126837dd92a/1f86af61ca1b6737b9e9a7e1e702a
bab.wav --model /deepspeech/models --aggressive 0
DEBUG:root:Transcribing audio file @ /deepspeech/data/clips/11ca9350-8080-11e9-a63e-8126837dd92a/1f86af61ca1b6737b9e9a7e1e702abab.wav
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
DEBUG:root:Caught the wav file @: /deepspeech/data/clips/11ca9350-8080-11e9-a63e-8126837dd92a/1f86af61ca1b6737b9e9a7e1e702abab.wav
DEBUG:root:Processing chunk 00
DEBUG:root:Running inference...
DEBUG:root:Inference took 1.262s for 1.470s audio file.
DEBUG:root:Transcript: di dyddiad
DEBUG:root:************************************************************************************************************
DEBUG:root:Filename                       Duration(s)          Inference Time(s)    Model Load Time(s)   LM Load Time(s)
DEBUG:root:1f86af61ca1b6737b9e9a7e1e702abab.wav 2.320                1.262                0.060                0.000
DEBUG:root:************************************************************************************************************
1f86af61ca1b6737b9e9a7e1e702abab.wav 2.320                1.262                0.060                0.000
root@4523baca8854:/deepspeech/server# more /deepspeech/data/clips/11ca9350-8080-11e9-a63e-8126837dd92a/1f86af61ca1b6737b9e9a7e1e702abab.txt
Be di'r dyddiad?
root@4523baca8854:/deepspeech/server# exit
exit
techiaith@lwk1900002:~/docker/docker-deepspeech-server-cy$ git status
fatal: not a git repository (or any of the parent directories): .git
techiaith@lwk1900002:~/docker/docker-deepspeech-server-cy$ git init
Initialized empty Git repository in /home/techiaith/docker/docker-deepspeech-server-cy/.git/
```

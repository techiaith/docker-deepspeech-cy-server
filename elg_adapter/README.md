# ELG Adapter for DeepSpeech Server

As the adapter is using the ELG python SDK, you need to have it installed. If it is not the case, run: 

`$ pip install elg==0.4.5` 

and make sure it is accessible from your PATH. Run the following to verify: 

```
$ elg
usage: elg <command> [<args>]

positional arguments:
  {run,download,info,search,docker}
                        commands

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         Display ELG version

For more information about a command, run: `elg <command> --help`
```

If you get a respone from the `elg` command, then use the Makefile to build and run the adapter for either the 'transcibe' or 'macsen' engine :

```
$ make build-transcribe

$ make run-transcribe
```

('macsen' is a speech recognition engine optimized for recognizing command or questions for a voice assistant app. See http://techiaith.cymru/macsen) 


You can test with :

`$ python3 test-transcribe.py`

which should result with:

```
$ python3 test.py
Using authentication object
Calling:
        [0] techiaith/deepspeech-0.9.3-adapter:transcribe
with request:
        type: audio - format: linear16

type='texts' warnings=None texts=[TextsResponseObject(role=None, content='mae ganddynt ddau o blant mab a merch', texts=None, score=None, features=None, annotations=None)]
```

N.B. only one container/model can be executed at a time, since the Dockerfile and docker-entrypoint.sh is regenerated each time. 



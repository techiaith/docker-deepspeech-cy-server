# docker-deepspeech-server

## Sut i gychwyn arni..

Mae na ddwy fath o beiriant adnabod lleferydd Cymraeg - y ddau wedi eu hyfforddi i ymateb yn well i wahanol defnyddiau..

 1 - peiriant adnabod cwestiynau neu gorchmynion i'r ap Macsen (gelwir y peiriant felly yn 'macsen')
 2 - peiriant adnabod lleferydd fwy rhydd ac agored - h.y. gyd-destun defnydd arddweud (dictation) (gelwir felly y peiriant yn 'arddweud')
 
Os hoffwch chi'r peiriant arddweud, yna dyma'r camau i'w ddilyn ar beiriant Mac OS X/Linux a Windows (os oes gennych chi Docker wedi'i osod) i osod yn gyntaf

 
```
$ git clone https://github.com/techiaith/docker-deepspeech-server-cy
$ cd docker-deepspeech-server-cy
$ make build-arddweud
```


Yna i redeg, does ond angen un gorchymyn ychwanegol..

```
$ make run-arddweud
```

I'w brofi'n syml, mae'n bosib yrru'r ffeil wav enghreifftiol sydd wedi'i gynnwys o fewn y project. Felly...

``` 
$ curl -F 'soundfile=@speech.wav' localhost:5501/speech_to_text/
{"success": true, "version": 1, "text": "mae ganddynt ddau o blant mab a merch"}
```

Mae modd defnyddio ffeiliau wav eich hunain, cyn belled a'u bod ar ffurf wav ac yn 16kHz, un sianel. 



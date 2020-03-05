# docker-deepspeech-server-cy

## Cefndir

Mae 'na ddwy fath o beiriant adnabod lleferydd Cymraeg - y ddau wedi eu hyfforddi i ymateb yn well i wahanol ddefnyddiau..

 1 - peiriant adnabod cwestiynau neu orchmynion i'r ap Macsen (gelwir y peiriant felly yn '*macsen*')
 
 2 - peiriant adnabod lleferydd mwy rhydd ac agored - h.y. gyd-destun defnydd arddweud (dictation) (gelwir felly'r peiriant yn '*arddweud*')
 
 
## Gosod

Os hoffwch chi'r peiriant arddweud, yna dyma'r camau i'w ddilyn ar beiriant Mac OS X/Linux a Windows (os oes gennych chi Docker wedi'i osod) i osod yn gyntaf

 
```
$ git clone https://github.com/techiaith/docker-deepspeech-server-cy
$ cd docker-deepspeech-server-cy
$ make build-arddweud
```

## Defnyddio

Yna i redeg, does ond angen un gorchymyn ychwanegol..

```
$ make run-arddweud
```

I ei brofi'n syml, mae'n bosib gyrru'r ffeil wav enghreifftiol sydd wedi'i gynnwys o fewn y project. Felly...

``` 
$ curl -F 'soundfile=@speech.wav' localhost:5501/speech_to_text/
{"success": true, "version": 1, "text": "mae ganddynt ddau o blant mab a merch"}
```

Mae modd defnyddio recordiadau eich hunain, cyn belled â'u bod ar ffurf wav ac yn 16kHz, un sianel. 

## Rhybudd

Rhaid cofio *ni fydd y canlyniadau pob tro yn hollol gywir*. Rydyn wedi mesur y gyfradd gwallau yn 33%, sydd yn uchel iawn i'w gymharu â Saesneg ac ieithoedd mawr eraill sydd â chyfraddau o dan 8%. 

Mae mesur gallu'r peiriant yn ogystal â'i wella yn waith sy'n dal yn parhau. 

Yn y cyfamser, os hoffwch chi weld y peiriannau yn gwella, yna recordiwch rhai brawddegau wefan Mozilla CommonVoice (https://voice.mozilla.org/cy), fel bydd gennyn ni ragor o ddata hyfforddi'r peiriannau. 
Neu defnyddiwch ein hap Macsen! (http://techiaith.cymru/macsen)



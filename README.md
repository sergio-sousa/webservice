# WebService
IntegraÆ de venda com a Boavista.

### ExecuÆ com os dados colocados manual
```sh
$ python3 venda_boavista.py 
$ CODIGO LOJA OU CODIGO ESTABELECIMENTO OBRIGATORIOS

```
### ExecuÆ passando o documento 

```sh
$  python3 venda_boavista_para.py docimp.imp
$ Traceback (most recent call last):
  File "venda_boavista_para.py", line 47, in <module>
    response = requests.request("POST", url, data=payload, headers=headers)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 53, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 454, in request
    prep = self.prepare_request(req)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 388, in prepare_request
    hooks=merge_hooks(request.hooks, self.hooks),
  File "/usr/lib/python3/dist-packages/requests/models.py", line 296, in prepare
    self.prepare_body(data, files, json)
  File "/usr/lib/python3/dist-packages/requests/models.py", line 450, in prepare_body
    body = self._encode_params(data)
  File "/usr/lib/python3/dist-packages/requests/models.py", line 89, in _encode_params
    for k, vs in to_key_val_list(data):
ValueError: too many values to unpack (expected 2)


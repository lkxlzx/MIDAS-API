# 其他语言示例 (C# · Java · Dart · C · Node.js)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../OTHER_LANGUAGES.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../docs/zh-cn/GLOSSARY.md)）

REST API 不依赖平台，因此除本文介绍的语言之外，只要某种语言具备 HTTP 客户端，
就可以调用 MIDAS NX Open API。以下是把通过 `POST /db/node` 创建 1 个节点的
同一请求改写为多种语言的代码片段（只收录没有专属文件夹的语言 —
Python 见 [`python/`](../../python/)，JavaScript(Node.js/axios) 见 [`javascript/`](../javascript/)，
cURL 见 [`curl/`](../curl/)，Excel VBA 见 [`vba/`](../vba/)）。

出处：[MIDAS Support "Example: Various Programming Languages"](https://support.midasuser.com/hc/en-us/articles/30506872725017-Example-Various-Programming-Languages)
（原样搬运原文片段，仅修正了 Node.js/Axios 示例中箭头函数的笔误（`= {` → `=> {`）
与缺失的 baseURL 组合。）

通用请求：

```json
POST {baseURL}/db/node
{
  "Assign": {
    "1": { "X": 1, "Y": 2, "Z": 3 }
  }
}
```

## C# — HttpClient

```csharp
var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Post, "https://moa-engineers.midasit.com:443/civil/db/node");
request.Headers.Add("MAPI-Key", "your_api_key_here");
var content = new StringContent(
    "{\"Assign\":{\"1\":{\"X\":1,\"Y\":2,\"Z\":3}}}",
    null, "application/json");
request.Content = content;
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
```

## JavaScript — Fetch (浏览器)

```javascript
const myHeaders = new Headers();
myHeaders.append("MAPI-Key", "your_api_key_here");
myHeaders.append("Content-Type", "application/json");

const raw = JSON.stringify({
  Assign: { "1": { X: 1, Y: 2, Z: 3 } },
});

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow",
};

fetch("https://moa-engineers.midasit.com:443/civil/db/node", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.log("error", error));
```

## Java — OkHttp

```java
OkHttpClient client = new OkHttpClient().newBuilder().build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"Assign\":{\"1\":{\"X\":1,\"Y\":2,\"Z\":3}}}");
Request request = new Request.Builder()
    .url("https://moa-engineers.midasit.com:443/civil/db/node")
    .method("POST", body)
    .addHeader("MAPI-Key", "your_api_key_here")
    .addHeader("Content-Type", "application/json")
    .build();
Response response = client.newCall(request).execute();
```

## Dart — Dio

```dart
import 'dart:convert';
import 'package:dio/dio.dart';

var headers = {
  'MAPI-Key': 'your_api_key_here',
  'Content-Type': 'application/json',
};
var data = json.encode({
  "Assign": {
    "1": {"X": 1, "Y": 2, "Z": 3}
  }
});
var dio = Dio();
var response = await dio.request(
  'https://moa-engineers.midasit.com:443/civil/db/node',
  options: Options(method: 'POST', headers: headers),
  data: data,
);

if (response.statusCode == 200) {
  print(json.encode(response.data));
} else {
  print(response.statusMessage);
}
```

## C — libcurl

```c
#include <curl/curl.h>

CURL *curl;
CURLcode res;
curl = curl_easy_init();
if (curl) {
    curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "POST");
    curl_easy_setopt(curl, CURLOPT_URL, "https://moa-engineers.midasit.com:443/civil/db/node");
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, "MAPI-Key: your_api_key_here");
    headers = curl_slist_append(headers, "Content-Type: application/json");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    const char *data = "{\"Assign\":{\"1\":{\"X\":1,\"Y\":2,\"Z\":3}}}";
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
    res = curl_easy_perform(curl);
    curl_slist_free_all(headers);
}
curl_easy_cleanup(curl);
```

## Node.js — Axios

> 原文示例只有 `url: '/db/node'` 而没有 `baseURL`，并且存在像 `.then((response) = {` 这样
> 箭头函数的笔误（`=` 应为 `=>`），照搬会出现语法错误。以下是修正这两处后的版本。Node.js 中更完整地
> 使用 axios 的示例请参考 [`javascript/README.md`](../javascript/README.zh-cn.md)。

```javascript
const axios = require("axios");

const data = JSON.stringify({
  Assign: { "1": { X: 1, Y: 2, Z: 3 } },
});

const config = {
  method: "post",
  maxBodyLength: Infinity,
  baseURL: "https://moa-engineers.midasit.com:443/civil",
  url: "/db/node",
  headers: {
    "MAPI-Key": "your_api_key_here",
    "Content-Type": "application/json",
  },
  data,
};

axios
  .request(config)
  .then((response) => {
    console.log(JSON.stringify(response.data));
  })
  .catch((error) => {
    console.log(error);
  });
```

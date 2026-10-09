---
title: Crashsight OpenAPI
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.23"

---

# Base Url

Need to access different sites based on user's registration region：


Website： https://crashsight.wetest.net



# Signatures and restrictions

## Public request parameters

### 1.1 URL Signature Parameters

| Name | Type | Required？ | Description |
| ---- | ---- | --------- | ----------- |
| t | int | Yes | The request’s unix timestamp which the base unit of time is sencod. |
| userSecret | String | Yes | The signature result string. See Signature for the signature calculation method. |
| localUserId | String | Yes | UserID |

### 1.2 Generic Header Parameters

| Name | Required？ | Description |
| ---- | --------- | ----------- |
| Content-Type | Yes | application/json |
| Accept-Encoding | Yes | \* |

### 1.3 Signature

localUserId：You can be obtained in personal information.\
![企业微信截图_16937999612475.png](https://data.eolink.com/ENGqJLJ6feb91e37022b13085117d4cb342b0bc78087c33)
user\_key：OpenAPI Secret Key，example：<YOUR_OPENAPI_SECRET_KEY>
![企业微信截图_16938002196859.png](https://data.eolink.com/h9pldCab2a138f87a6f8f5166d94a119749338822823483)
t: current unix timestamp，example：1618199626

## Procedure

```
base64.b64encode(bytes(hmac.new(bytes(self.user_key, 'utf-8'), bytes(str(self.local_user_id) + '_' + str(self.t), 'utf-8'), digestmod=hashlib.sha256).hexdigest(), encoding=utf8))
```

The following method is used to sign the access request:

1. Construct Canonicalized Query String using the request parameters.

    ```
    message = localUserId + '_' + t
    key = userOpenapiKey
    base64_encode(hash_hmac('sha256', message, key, false));
    ```
2. Follow the following rules to construct the string for signature calculation using the Canonicalized Query String constructed in the previous step
3. Encode the HMAC value into a string based on Base64 encoding rules, and you can get the signature value (Signature).
4. Add the obtained signature value to the request parameters as the Signature parameter. The request signing process is completed，example:&userSecret=<SIGNATURE_VALUE>&localUserId=<LOCAL_USER_ID>&t=1693818679.
https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/signature.py

## Error Codes


![企业微信截图_16945729271867.png](https://api.apifox.cn/api/v1/projects/3281673/resources/400048/image-preview)

# API Reference/Overview Statistics

## POST Get hourly  top issue list

POST /env/uniform/openapi/getTopIssueHourlysignature

Hourly TOP issue list

Website： https://crashsight.wetest.net

download python code example：https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getTopIssueHourly.py

> Body Parameters

```json
{
  "appId": "<APP_ID>",
  "platformId": 1,
  "version": "-1",
  "startHour": "2022101404",
  "type": "crash",
  "limit": 5,
  "topIssueDataType": "",
  "needCountryDimension": true,
  "countryList": [
    "中国"
  ],
  "fsn": ""
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» appId|body|string| yes |Project ID|
|» platformId|body|integer| yes |Platform ID Android：1，IOS：2，PC：10|
|» version|body|string| yes |Project version, -1 represents all versions|
|» startHour|body|string| yes |Start time.  Format is YYMMDDHH|
|» type|body|string| yes |Support Three types - crash, anr, error|
|» limit|body|integer| yes |Row limit, how many rows to get|
|» topIssueDataType|body|string| yes |System exit keywords are divided into two cases. SystemExit represents matching system exit keywords, and unSystemExit represents not matching system exit keywords..|
|» needCountryDimension|body|boolean| yes |True: Get the TOP issues in the specified country; False: Get the TOP issues without distinguishing regions.|
|» countryList|body|[string]| no |It only takes effect when needCountryDimension is true, specifying the list of countries to be queried.|
|» fsn|body|string| no |RequestID. The fsn value can be fixed|

> Response Examples

```json
{
  "versionCrashUser": 200,
  "preDayVersionCrashUser": 200,
  "topIssueList": [
    {
      "appId": "<APP_ID>",
      "platformId": 1,
      "version": "-1",
      "issueId": "<ISSUE_ID>",
      "firstUploadTime": "2021-01-13 14:22:00 671",
      "firstUploadTimestamp": 0,
      "crashUser": 45,
      "crashNum": 45,
      "accumulateCrashNum": 511153,
      "accumulateCrashUser": 510012,
      "state": 2,
      "processors": "<PROCESSOR_HASH>",
      "exceptionName": "java.lang.RuntimeException",
      "exceptionMessage": "yyY9Wfe9uXCw6lgPTmpZ2SECbHoQXT",
      "keyStack": "",
      "lastUpdateTime": "2022-10-14 11:54:02 132",
      "lastUpdateTimestamp": 0,
      "issueVersions": [
        {
          "version": "<APP_VERSION>",
          "firstUploadTimestamp": 0,
          "lastUploadTimestamp": 0,
          "count": 0,
          "deviceCount": 0,
          "systemExitCount": 0,
          "systemExitDeviceCount": 0
        }
      ],
      "preDayCrashUser": 36,
      "preDayCrashNum": 36,
      "prevHourCrashDevices": 27,
      "tags": []
    },
    {
      "appId": "<APP_ID>",
      "platformId": 1,
      "version": "-1",
      "issueId": "<ISSUE_ID>",
      "firstUploadTime": "2021-01-13 14:23:33 958",
      "firstUploadTimestamp": 0,
      "crashUser": 39,
      "crashNum": 39,
      "accumulateCrashNum": 512885,
      "accumulateCrashUser": 511680,
      "state": 0,
      "processors": "",
      "exceptionName": "java.lang.RuntimeException",
      "exceptionMessage": "27jkgiefwsuqrstq1bd9a784vwstqr",
      "keyStack": "",
      "lastUpdateTime": "2022-10-14 11:51:32 587",
      "lastUpdateTimestamp": 0,
      "issueVersions": [
        {
          "version": "<APP_VERSION>",
          "firstUploadTimestamp": 0,
          "lastUploadTimestamp": 0,
          "count": 0,
          "deviceCount": 0,
          "systemExitCount": 0,
          "systemExitDeviceCount": 0
        }
      ],
      "preDayCrashUser": 36,
      "preDayCrashNum": 36,
      "prevHourCrashDevices": 36,
      "tags": []
    },
    {
      "appId": "<APP_ID>",
      "platformId": 1,
      "version": "-1",
      "issueId": "<ISSUE_ID>",
      "firstUploadTime": "2021-01-13 14:22:13 862",
      "firstUploadTimestamp": 0,
      "crashUser": 35,
      "crashNum": 35,
      "accumulateCrashNum": 512108,
      "accumulateCrashUser": 510964,
      "state": 1,
      "processors": "<PROCESSOR_HASH>",
      "exceptionName": "java.lang.RuntimeException",
      "exceptionMessage": "DmNcPX1JULMgruOClJAzOTWy9zjm01",
      "keyStack": "",
      "lastUpdateTime": "2022-10-14 11:54:37 794",
      "lastUpdateTimestamp": 0,
      "issueVersions": [
        {
          "version": "<APP_VERSION>",
          "firstUploadTimestamp": 0,
          "lastUploadTimestamp": 0,
          "count": 0,
          "deviceCount": 0,
          "systemExitCount": 0,
          "systemExitDeviceCount": 0
        }
      ],
      "preDayCrashUser": 28,
      "preDayCrashNum": 28,
      "prevHourCrashDevices": 32,
      "tags": [
        {
          "tagId": 2855,
          "tagType": 0,
          "tagCount": 0,
          "tagName": "test"
        }
      ]
    },
    {
      "appId": "<APP_ID>",
      "platformId": 1,
      "version": "-1",
      "issueId": "<ISSUE_ID>",
      "firstUploadTime": "2021-01-13 14:22:23 880",
      "firstUploadTimestamp": 0,
      "crashUser": 31,
      "crashNum": 31,
      "accumulateCrashNum": 512224,
      "accumulateCrashUser": 511079,
      "state": 0,
      "processors": "",
      "exceptionName": "java.lang.RuntimeException",
      "exceptionMessage": "sNSXTvFGp6ZGrorljP6WPxsGtKc5px",
      "keyStack": "",
      "lastUpdateTime": "2022-10-14 11:54:55 679",
      "lastUpdateTimestamp": 0,
      "issueVersions": [
        {
          "version": "<APP_VERSION>",
          "firstUploadTimestamp": 0,
          "lastUploadTimestamp": 0,
          "count": 0,
          "deviceCount": 0,
          "systemExitCount": 0,
          "systemExitDeviceCount": 0
        }
      ],
      "preDayCrashUser": 30,
      "preDayCrashNum": 30,
      "prevHourCrashDevices": 42,
      "tags": []
    },
    {
      "appId": "<APP_ID>",
      "platformId": 1,
      "version": "-1",
      "issueId": "<ISSUE_ID>",
      "firstUploadTime": "2021-01-13 14:21:57 297",
      "firstUploadTimestamp": 0,
      "crashUser": 25,
      "crashNum": 25,
      "accumulateCrashNum": 512851,
      "accumulateCrashUser": 511653,
      "state": 0,
      "processors": "<PROCESSOR_HASH>",
      "exceptionName": "java.lang.RuntimeException",
      "exceptionMessage": "SRdSbQ3h0XOjLF90pGHvwCu5vZBLwl",
      "keyStack": "",
      "lastUpdateTime": "2022-10-14 11:54:19 854",
      "lastUpdateTimestamp": 0,
      "issueVersions": [
        {
          "version": "<APP_VERSION>",
          "firstUploadTimestamp": 0,
          "lastUploadTimestamp": 0,
          "count": 0,
          "deviceCount": 0,
          "systemExitCount": 0,
          "systemExitDeviceCount": 0
        }
      ],
      "preDayCrashUser": 38,
      "preDayCrashNum": 38,
      "prevHourCrashDevices": 29,
      "tags": []
    }
  ],
  "crashDevices": 200,
  "prevHourCrashDevices": 200,
  "prevDaySameHourCrashDevices": 200,
  "accessDevices": 1000,
  "prevHourAccessDevices": 1000,
  "prevDaySameHourAccessDevices": 1000
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» versionCrashUser|integer|true|none||Affected device count|
|» preDayVersionCrashUser|integer|true|none||Affected device count of the previous day|
|» topIssueList|[object]|true|none||none|
|»» appId|string|true|none||Project ID|
|»» platformId|integer|true|none||Platform ID|
|»» version|string|true|none||Project version|
|»» issueId|string|true|none||Issue ID|
|»» firstUploadTime|string|true|none||First report time|
|»» firstUploadTimestamp|integer|true|none||Fist report timestamp|
|»» crashUser|integer|true|none||Crashed devices|
|»» crashNum|integer|true|none||Crash count|
|»» accumulateCrashNum|integer|true|none||Total  crash count|
|»» accumulateCrashUser|integer|true|none||Total crashed devices|
|»» state|integer|true|none||Processing status|
|»» processors|string|true|none||Handler|
|»» exceptionName|string|true|none||Exception type|
|»» exceptionMessage|string|true|none||Exception information|
|»» keyStack|string|true|none||Stack information|
|»» lastUpdateTime|string|true|none||Latest update time|
|»» lastUpdateTimestamp|integer|true|none||none|
|»» issueVersions|[object]|true|none||Issue version collection|
|»»» version|string|true|none||none|
|»»» firstUploadTimestamp|integer|true|none||none|
|»»» lastUploadTimestamp|integer|true|none||none|
|»»» count|integer|true|none||none|
|»»» deviceCount|integer|true|none||none|
|»»» systemExitCount|integer|true|none||none|
|»»» systemExitDeviceCount|integer|true|none||none|
|»» preDayCrashUser|integer|true|none||Total affected devices of the previous day|
|»» preDayCrashNum|integer|true|none||Total affected Times of  the previous day|
|»» prevHourCrashDevices|integer|true|none||none|
|»» tags|[object]|true|none||Tag collection|
|»»» tagId|integer|false|none||none|
|»»» tagType|integer|false|none||none|
|»»» tagCount|integer|false|none||none|
|»»» tagName|string|false|none||none|
|» crashDevices|integer|true|none||Crashed Devices|
|» prevHourCrashDevices|integer|true|none||none|
|» prevDaySameHourCrashDevices|integer|true|none||none|
|» accessDevices|integer|true|none||Active Devices|
|» prevHourAccessDevices|integer|true|none||none|
|» prevDaySameHourAccessDevices|integer|true|none||none|

## POST Get trend data for the last N days

POST /env/uniform/openapi/getTrendEx

Get trend data for the last N days

Website： https://crashsight.wetest.net

download python code example: https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getTrendEx.py

> Body Parameters

```json
{
  "appId": "<APP_ID>",
  "platformId": 1,
  "startDate": "20230605",
  "endDate": "20230704",
  "type": "crash",
  "fsn": "",
  "dataType": "trendData",
  "vm": 0,
  "versionList": "[\"8.4.1.1.804010199\",\"3.82.1.4\"]",
  "needCountryDimension": false,
  "countryList": "[]",
  "mergeMultipleVersionsWithInaccurateResult": true
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» appId|body|string| yes |Project ID|
|» platformId|body|integer| yes |Platform ID Android：1，IOS：2，PC：10|
|» startDate|body|string| yes |Start Time YYMMDD|
|» endDate|body|string| yes |End Time YYMMDD|
|» type|body|string| yes |All types of errors.Three types - crash, ANR, and error.|
|» fsn|body|string| yes |RequestID. The fsn value can be fixed|
|» dataType|body|string| yes |Data Type :trendData|
|» vm|body|integer| yes |Emulator identifier. 0 : Full device 1: Real device 2: Emulator|
|» versionList|body|string| yes |Version list. Version support wildcard *|
|» needCountryDimension|body|boolean| yes |True: need country-level statistics, false: do not need it|
|» countryList|body|string| yes |If you set the statistics to be country-level, please provide a list of country names to be queried. When you set the needCountryDimension to true but countryList is an empty array, it indicates that you want to query all countries.|
|» mergeMultipleVersionsWithInaccurateResult|body|boolean| yes |Whether multiple version results should be merged into a single result. The merging method is to directly add the device count and times of each individual version.|

> Response Examples

```json
{
  "appId": "<APP_ID>",
  "platformId": 1,
  "version": "MERGED",
  "date": "20230605",
  "country": "-1",
  "crashNum": 0,
  "crashUser": 0,
  "reportNumAllData": 0,
  "reportDeviceAllData": 0,
  "accessNum": 0,
  "accessUser": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» appId|string|true|none||Project ID|
|» platformId|integer|true|none||Platform ID|
|» version|string|true|none||Project Version|
|» date|string|true|none||Time|
|» country|string|true|none||Country|
|» crashNum|integer|true|none||Crash count|
|» crashUser|integer|true|none||Crashed Devices|
|» reportNumAllData|integer|true|none||none|
|» reportDeviceAllData|integer|true|none||none|
|» accessNum|integer|true|none||Number of connections|
|» accessUser|integer|true|none||Active Devices|

## GET Get overview of data analysis for a single day, including crash, ANR and error

GET /env/uniform/openapi/getRealTimeAppendStatsignature

To get the anomaly overview data for a single day, including crash, ANR and error

Website： https://crashsight.wetest.net

download python code example: https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getRealTimeAppendStat.py

> Body Parameters

```json
{}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|appId|query|string| yes |Project ID|
|platformId|query|string| yes |Platform ID Android：1，IOS：2，PC：10|
|startHour|query|string| yes |The format for the date should be YYYYMMDDHH, with the hour part being 00 only.|
|endHour|query|string| yes |The format for the date should be YYYYMMDDHH, and it must be the same day as startHour.|
|type|query|string| yes | All error types including crash, error, error. The field can be assigned a default value：all.|
|fsn|query|string| yes |RequestID. The fsn value can be fixed|
|Accept-Encoding|header|string| yes |none|
|Content-Type|header|string| yes |none|
|body|body|object| no |none|

> Response Examples

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "data": [
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040818",
        "type": "",
        "accessNum": 1255365,
        "accessUser": 832770,
        "crashNum": 1164,
        "crashUser": 566,
        "anrNum": 0,
        "anrUser": 0,
        "errorNum": 67962,
        "errorUser": 33322,
        "vmCrashNum": 0,
        "vmCrashUser": 0,
        "vmAnrNum": 0,
        "vmAnrUser": 0,
        "vmErrorNum": 0,
        "vmErrorUser": 0
      }
    ]
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» status|integer|true|none||none|
|» ret|object|true|none||none|
|»» code|integer|true|none||none|
|»» message|string|true|none||none|
|»» data|[object]|true|none||none|
|»»» appId|string|false|none||Project ID|
|»»» platformId|integer|false|none||Platform ID|
|»»» version|string|false|none||Project  Version|
|»»» date|string|false|none||Time|
|»»» accessNum|integer|false|none||The number of network accesses.|
|»»» accessUser|integer|false|none||Active devices.|
|»»» crashNum|integer|false|none||Crash count|
|»»» crashUser|integer|false|none||Crashed devices|
|»»» anrNum|integer|false|none||ANR Count.|
|»»» anrUser|integer|false|none||ANR devices.|
|»»» errorNum|integer|false|none||Error count|
|»»» errorUser|integer|false|none||Error devices|
|»»» vmCrashNum|integer|false|none||Emulator crash count|
|»»» vmCrashUser|integer|false|none||Emulator Crashed devices|
|»»» vmAnrNum|integer|false|none||Emulator ANR count.|
|»»» vmAnrUser|integer|false|none||Emulator ANR devices.|
|»»» vmErrorNum|integer|false|none||Emulator error count|
|»»» vmErrorUser|integer|false|none||Emulator error devices|

## POST Get cumulative trend data

POST /env/uniform/openapi/getAppRealTimeTrendAppendsignature

Get cumulative trend data

Website： https://crashsight.wetest.net

download python code example: https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getAppRealTimeTrendAppend.py

> Body Parameters

```json
{
  "appId": "<APP_ID>",
  "platformId": 1,
  "startHour": "2020060400",
  "endHour": "2020060423",
  "type": "crash",
  "fsn": "<DEVICE_UUID>",
  "version": "<APP_VERSION>",
  "dataType": "realTimeTrendData",
  "vm": 0
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» appId|body|string| yes |none|
|» platformId|body|integer| yes |none|
|» startHour|body|string| yes |none|
|» endHour|body|string| yes |none|
|» type|body|string| yes |none|
|» fsn|body|string| yes |none|
|» version|body|string| yes |none|
|» dataType|body|string| yes |none|
|» vm|body|integer| yes |none|

> Response Examples

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "data": [
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040800",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040801",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040802",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040803",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040804",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040805",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040806",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040807",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040808",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040809",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040810",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040811",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040812",
        "crashNum": 0,
        "crashUser": 0,
        "accessNum": 0,
        "accessUser": 0
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040813",
        "crashNum": 132,
        "crashUser": 60,
        "accessNum": 141249,
        "accessUser": 115041
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040814",
        "crashNum": 338,
        "crashUser": 163,
        "accessNum": 363494,
        "accessUser": 276739
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040815",
        "crashNum": 610,
        "crashUser": 297,
        "accessNum": 615874,
        "accessUser": 442173
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040816",
        "crashNum": 872,
        "crashUser": 425,
        "accessNum": 900313,
        "accessUser": 621881
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040817",
        "crashNum": 1122,
        "crashUser": 546,
        "accessNum": 1202687,
        "accessUser": 800755
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040818",
        "crashNum": 1386,
        "crashUser": 673,
        "accessNum": 1524840,
        "accessUser": 986791
      },
      {
        "appId": "<APP_ID>",
        "platformId": 2,
        "version": "-1",
        "date": "2021040819",
        "crashNum": 1538,
        "crashUser": 748,
        "accessNum": 1692083,
        "accessUser": 1076518
      }
    ]
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» status|integer|true|none||none|
|» ret|object|true|none||none|
|»» code|integer|true|none||none|
|»» message|string|true|none||none|
|»» data|[object]|true|none||none|
|»»» appId|string|true|none||Project ID|
|»»» platformId|integer|true|none||Platform ID|
|»»» version|string|true|none||Project version|
|»»» date|string|true|none||Time|
|»»» crashNum|integer|true|none||Crash count|
|»»» crashUser|integer|true|none||Crash device count|
|»»» accessNum|integer|true|none||access count|
|»»» accessUser|integer|true|none||Internet-connected device count|

## POST Get hourly trend data

POST /env/uniform/openapi/getRealTimeHourlyStatsignature

Get hourly trend data

Website： https://crashsight.wetest.net

download python code example:https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getRealTimeHourlyStat.py

> Body Parameters

```json
{
  "appId": "",
  "platformId": 0,
  "version": "",
  "versionList": "",
  "startHour": "",
  "endHour": "",
  "type": "",
  "fsn": "",
  "dataType": "",
  "vm": 0,
  "needCountryDimension": false,
  "countryList": "",
  "mergeMultipleVersionsWithInaccurateResult": false
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» appId|body|string| yes |Project ID|
|» platformId|body|integer| yes |Platform ID Android：1，IOS：2，PC：10|
|» version|body|string| yes |Project version. -1: All versions|
|» versionList|body|string| yes |Version list. Version support wildcard *|
|» startHour|body|string| yes |Start Time YYMMDDHH|
|» endHour|body|string| yes |End Time YYMMDDHH|
|» type|body|string| yes |All types of errors.Three types - crash, ANR, and error.|
|» fsn|body|string| yes |RequestID. The fsn value can be fixed|
|» dataType|body|string| yes |realTimeTrendData|
|» vm|body|integer| yes |Emulator identifier. 0 : Full device 1: Real device 2: Emulator|
|» needCountryDimension|body|boolean| yes |True: need country-level statistics, false: do not need it|
|» countryList|body|string| yes |If you set the statistics to be country-level, please provide a list of country names to be queried. When you set the needCountryDimension to true but countryList is an empty array, it indicates that you want to query all countries.|
|» mergeMultipleVersionsWithInaccurateResult|body|boolean| yes |Whether multiple version results should be merged into a single result. The merging method is to directly add the device count and times of each individual version.|

> Response Examples

```json
{
  "appId": "<APP_ID>",
  "platformId": 2,
  "version": "-1",
  "date": "2021040800",
  "crashNum": 0,
  "crashUser": 0,
  "accessNum": 0,
  "accessUser": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» appId|string|true|none||Project ID|
|» platformId|integer|true|none||Platform ID|
|» version|string|true|none||Project version|
|» date|string|true|none||Time|
|» crashNum|integer|true|none||The number of crashes|
|» crashUser|integer|true|none||The number of crash devices|
|» accessNum|integer|true|none||The number of network accesses|
|» accessUser|integer|true|none||The number of networked devices|

## POST Get cumulative trend data

POST /env/uniform/openapi/getAppRealTimeTrendAppendExsignature

Get cumulative trend data

Website： https://crashsight.wetest.net

download python code example:https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getAppRealTimeTrendAppendEx.py

> Body Parameters

```json
{
  "appId": "<APP_ID>",
  "platformId": 1,
  "type": "crash",
  "vm": 0,
  "dataType": "realTimeTrendData",
  "mergeMultipleVersionsWithInaccurateResult": true,
  "versionList": [
    "495.4.19303",
    "272.6.9207",
    "221.2.5954"
  ],
  "startDate": "2023092700",
  "endDate": "2023092723",
  "needCountryDimension": false,
  "countryList": []
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» appId|body|string| yes |Project ID|
|» platformId|body|integer| yes |Platform ID Android：1，IOS：2，PC：10|
|» startHour|body|string| yes |Start Time YYMMDDHH|
|» endHour|body|string| yes |End Time YYMMDDHH. No more than 360 hours.|
|» type|body|string| yes |All types of errors.Three types - crash, ANR, and error.|
|» fsn|body|string| yes |RequestID. The fsn value can be fixed|
|» dataType|body|string| yes |realTimeTrendData|
|» vm|body|integer| yes |Emulator identifier. 0 : Full device 1: Real device 2: Emulator|
|» versionList|body|string| yes |Version list. Version support wildcard *|
|» needCountryDimension|body|boolean| yes |True: need country-level statistics, false: do not need it|
|» countryList|body|string| yes |If you set the statistics to be country-level, please provide a list of country names to be queried. When you set the needCountryDimension to true but countryList is an empty array, it indicates that you want to query all countries.|
|» mergeMultipleVersionsWithInaccurateResult|body|boolean| yes |Whether multiple version results should be merged into a single result. The merging method is to directly add the device count and times of each individual version.|

> Response Examples

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "errorCode": "",
    "data": [
      {
        "appId": "<APP_ID>",
        "platformId": 1,
        "version": "NO_STATS_DATA",
        "date": "2023062800",
        "crashNum": 0,
        "crashUser": 0,
        "reportNumAllData": 0,
        "reportDeviceAllData": 0,
        "accessNum": 0,
        "accessUser": 0,
        "country": "NO_STATS_DATA"
      }
    ]
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» status|integer|true|none||none|
|» ret|object|true|none||none|
|»» code|integer|true|none||none|
|»» message|string|true|none||none|
|»» errorCode|string|true|none||none|
|»» data|[object]|true|none||none|
|»»» appId|string|false|none||Project ID|
|»»» platformId|integer|false|none||Platform ID|
|»»» version|string|false|none||Project Version|
|»»» date|string|false|none||Time|
|»»» crashNum|integer|false|none||Crash count|
|»»» crashUser|integer|false|none||Crashed devices|
|»»» reportNumAllData|integer|false|none||none|
|»»» reportDeviceAllData|integer|false|none||none|
|»»» accessNum|integer|false|none||The number of network accesses.|
|»»» accessUser|integer|false|none||Active Devices|
|»»» country|string|false|none||none|

## POST Get top issue list

POST /env/uniform/openapi/getTopIssueExsignature

To get top issue list

Website： https://crashsight.wetest.net

download python code example:https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getTopIssueEx.py

> Body Parameters

```json
{
  "appId": "<APP_ID>",
  "platformId": 1,
  "type": "crash",
  "limit": 20,
  "topIssueDataType": "unSystemExit",
  "fsn": "<DEVICE_UUID>",
  "mergeMultipleVersionsWithInaccurateResult": false,
  "countryList": "",
  "versionList": [
    "1.0.0",
    "2.0.0",
    "3.0.*"
  ],
  "mergeMultipleDatesWithInaccurateResult": false,
  "minDate": "20230706",
  "maxDate": "20230708"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» appId|body|string| yes |Project ID|
|» platformId|body|integer| yes |Platform ID Android：1，IOS：2，PC：10|
|» type|body|string| yes |All types of errors.Three types - crash, ANR, and error.|
|» limit|body|integer| yes |row limit|
|» topIssueDataType|body|string| yes |System Exit Keyword can be divided into two cases, with the values of SystemExit and unSystemExit, which represent that the keyword matching system exit keyword, and the keyword matching system exit keyword is not found.|
|» fsn|body|string| yes |RequestID. The fsn value can be fixed|
|» mergeMultipleVersionsWithInaccurateResult|body|boolean| yes |When querying multiple versions, setting the mergeMultipleVersionsWithInaccurateResult field to true.The query result for the number of devices and the number of times should be combined by directly.|
|» countryList|body|string| yes |countries|
|» versionList|body|[string]| yes |Project version, -1 represents the full version.When querying multiple versions, you must set mergeMultipleVersionsWithInaccurateResult to true.To specify one or more version numbers, support * wildcard.|
|» mergeMultipleDatesWithInaccurateResult|body|boolean| yes |whether to query multiple days' data|
|» minDate|body|string| yes |Start Time.When querying data for multiple days, you can specify the start  of the date range (inclusive) using the format YYYYMMDD.|
|» maxDate|body|string| yes |End Time.When querying data for multiple days, you can specify the start  of the date range (inclusive) using the format YYYYMMDD.|

> Response Examples

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "data": {
      "prevDayCrashDevices": 1342,
      "prevDayAccessDevices": 3103,
      "topIssueList": [
        {
          "appId": "<APP_ID>",
          "platformId": 2,
          "version": "-1",
          "date": "20210412",
          "type": "crash",
          "issueId": "<ISSUE_ID>",
          "firstUploadTime": "2021-03-25 11:02:39",
          "crashUser": 808,
          "crashNum": 1662,
          "accumulateCrashNum": 15588,
          "accumulateCrashUser": 7510,
          "state": 0,
          "processors": "",
          "exceptionName": "SIGSEGV",
          "exceptionMessage": "SEGV_ACCERR",
          "keyStack": "ShadowTrackerExtra physx::PxVehicleConstraintShader::visualiseConstraint(physx::PxConstraintVisualizer&, void const*, physx::PxTransform const&, physx::PxTransform const&, unsigned int)",
          "lastUpdateTime": "2021-03-25 11:02:39",
          "issueVersions": [],
          "preDayCrashUser": 1888,
          "preDayCrashNum": 0,
          "is_system_exit": "false",
          "tags": []
        },
        {
          "appId": "<APP_ID>",
          "platformId": 2,
          "version": "-1",
          "date": "20210412",
          "type": "crash",
          "issueId": "<ISSUE_ID>",
          "firstUploadTime": "2021-04-08 13:26:31",
          "crashUser": 137,
          "crashNum": 274,
          "accumulateCrashNum": 2610,
          "accumulateCrashUser": 1292,
          "state": 0,
          "processors": "",
          "exceptionName": "SIGBUS",
          "exceptionMessage": "BUS_ADRALN",
          "keyStack": "ShadowTrackerExtra physx::PxVehicleConstraintShader::visualiseConstraint(physx::PxConstraintVisualizer&, void const*, physx::PxTransform const&, physx::PxTransform const&, unsigned int)",
          "lastUpdateTime": "2021-04-08 13:26:31",
          "issueVersions": [],
          "preDayCrashUser": 354,
          "preDayCrashNum": 400,
          "is_system_exit": "false",
          "bugs": []
        },
        {
          "appId": "<APP_ID>",
          "platformId": 2,
          "version": "-1",
          "date": "20210412",
          "type": "crash",
          "issueId": "<ISSUE_ID>",
          "firstUploadTime": "2021-03-25 11:01:38",
          "crashUser": 38,
          "crashNum": 76,
          "accumulateCrashNum": 718,
          "accumulateCrashUser": 338,
          "state": 0,
          "processors": "",
          "exceptionName": "SIGABRT",
          "exceptionMessage": "",
          "keyStack": "ShadowTrackerExtra physx::PxVehicleConstraintShader::visualiseConstraint(physx::PxConstraintVisualizer&, void const*, physx::PxTransform const&, physx::PxTransform const&, unsigned int)",
          "lastUpdateTime": "2021-03-25 11:01:38",
          "issueVersions": [],
          "preDayCrashUser": 84,
          "preDayCrashNum": 100,
          "is_system_exit": "false",
          "tags": [],
          "bugs": []
        }
      ]
    }
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» status|integer|true|none||response status|
|» data|object|true|none||query results|
|»» topIssueList|[object]|true|none||top issue list|
|»»» appId|string|false|none||Project ID|
|»»» platformId|integer|false|none||Platform ID|
|»»» date|string|false|none||Time：YYYYMMDD|
|»»» type|string|false|none||Type|
|»»» issueId|string|false|none||Issue ID|
|»»» firstUploadTime|string|false|none||First Report Time|
|»»» crashUser|integer|false|none||Affected devices|
|»»» crashNum|integer|false|none||Affected Times|
|»»» accumulateCrashNum|integer|false|none||Total Affected Times|
|»»» accumulateCrashUser|integer|false|none||Total Affected Devices|
|»»» state|integer|false|none||handling status|
|»»» processors|string|false|none||handlers|
|»»» exceptionName|string|false|none||exception type|
|»»» exceptionMessage|string|false|none||Exception information|
|»»» keyStack|string|false|none||Stack information|
|»»» lastUpdateTime|string|false|none||Recent update time|
|»»» issueVersions|[object]|false|none||Issue version set|
|»»»» version|string|false|none||version|
|»»»» firstUploadTime|string|false|none||First Report Time|
|»»»» firstUploadTimestamp|integer|false|none||First Report Timestamp|
|»»»» lastUploadTime|string|false|none||Recent report time|
|»»»» lastUploadTimestamp|integer|false|none||Recent report timestamp|
|»»»» count|integer|false|none||Affected Times|
|»»»» deviceCount|integer|false|none||Affected devices|
|»»»» systemExitCount|integer|false|none||System exit count|
|»»»» systemExitDeviceCount|integer|false|none||System exit device count|
|»»» preDayCrashUser|integer|false|none||The previous day's affected devices.This feature is not supported when querying data for multiple days.|
|»»» preDayCrashNum|integer|false|none||The number of times affected the previous day.This feature is not supported when querying data for multiple days.|
|»»» prevHourCrashDevices|integer|false|none||crashed devices in the last hour.This feature is not supported when querying data for multiple days.|
|»»» is_system_exit|string|false|none||whether the system is marked as being exited|
|»»» tags|[object]|false|none||none|
|»»»» tagId|integer|false|none||none|
|»»»» tagType|integer|false|none||none|
|»»»» tagCount|integer|false|none||none|
|»»»» tagName|string|false|none||none|
|»»» bugs|[object]|false|none||none|
|»»»» id|string|false|none||tapd bug ID|
|»»»» title|string|false|none||tapd title|
|»»»» workspaceId|string|true|none||tapd workspace id|
|»» crashDevices|integer|true|none||the number of crashed devices.|
|»» accessDevices|integer|false|none||the number of connected devices.|
|»» prevDayCrashDevices|integer|true|none||The number of connected devices the day before, multi-day data queries are not supported.|
|»» prevDayAccessDevices|integer|true|none||The number of connected devices the day before, multi-day data queries are not supported.|
|» message|string|true|none||Error details|

## POST Get hourly trend data

POST /env/uniform/openapi/getRealTimeHourlyStatExsignature

Get hourly trend data

Website： https://crashsight.wetest.net

download python code example:https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getRealTimeHourlyStatEx.py

> Body Parameters

```json
{
  "appId": "<APP_ID>",
  "platformId": 1,
  "version": "",
  "versionList": "[\"8.4.1.1.804010199\",\"3.82.1.4\"]",
  "startHour": "2023070500",
  "endHour": "2023070523",
  "type": "",
  "fsn": "",
  "dataType": "realTimeTrendData",
  "vm": 0,
  "needCountryDimension": false,
  "countryList": "[]",
  "mergeMultipleVersionsWithInaccurateResult": true
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» appId|body|string| yes |Project ID|
|» platformId|body|integer| yes |Platform ID Android：1，IOS：2，PC：10|
|» versionList|body|string| yes |Project Version list. Version support wildcard *. -1: All versions|
|» startHour|body|string| yes |Start Time YYMMDDHH|
|» endHour|body|string| yes |End Time YYMMDDHH|
|» type|body|string| yes |All types of errors.Three types - crash, ANR, and error.|
|» fsn|body|string| yes |RequestID. The fsn value can be fixed|
|» dataType|body|string| yes |realTimeTrendData|
|» vm|body|integer| yes |Emulator identifier. 0 : Full device 1: Real device 2: Emulator|
|» countryList|body|string| yes |Whether multiple version results should be merged into a single result. The merging method is to directly add the device count and times of each individual version.|

> Response Examples

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "errorCode": "",
    "data": [
      {
        "appId": "<APP_ID>",
        "platformId": 1,
        "version": "MERGED",
        "date": "2023070500",
        "crashNum": 1,
        "crashUser": 1,
        "reportNumAllData": 0,
        "reportDeviceAllData": 0,
        "accessNum": 53,
        "accessUser": 19,
        "country": "-1"
      }
    ]
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» appId|string|true|none||Project ID|
|» platformId|integer|true|none||Platform ID|
|» version|string|true|none||Project Version|
|» date|string|true|none||Date|
|» crashNum|integer|true|none||The Number of crashes|
|» crashUser|integer|true|none||The Number of crashed devices|
|» reportNumAllData|integer|true|none||Private field. Original reported statistics.|
|» reportDeviceAllData|integer|true|none||Private field. Original reported statistics.|
|» accessNum|integer|true|none||The number of network accesses.|
|» accessUser|integer|true|none||The number of connected devices.|
|» country|string|true|none||Country|

# API Reference/Crash/Exception Analysis

## POST Get Advanced Trends（Private test）

POST /env/uniform/openapi/queryAdvancedTrend

Get advanced trends（Private test）

Website： https://crashsight.wetest.net

Download Python code example:https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_queryAdvancedTrend.py

> Body Parameters

```json
{
  "appId": "xxx",
  "searchConditionGroup": {
    "conditions": [
      {
        "field": "version"
      }
    ]
  },
  "minDatetime": "2024-07-24T00:00:00Z",
  "maxDatetime": "2024-07-30T23:59:59Z",
  "granularityUnit": "DAY"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» appId|body|string| yes |none|
|» searchConditionGroup|body|object| yes |none|
|»» conditions|body|[object]| no |none|
|»»» field|body|string| no |none|
|» minDatetime|body|string(date-time)| yes |none|
|» maxDatetime|body|string(date-time)| yes |none|
|» granularityUnit|body|string| yes |none|

> Response Examples

```json
{
  "status": 200,
  "ret": 200,
  "data": {
    "trendList": [
      {
        "date": "2024-07-24 00:00:00",
        "crashNum": 1111,
        "crashUser": 1111,
        "anrNum": 0,
        "anrUser": 0,
        "errorNum": 0,
        "errorUser": 0,
        "accessNum": 1111,
        "accessUser": 1111
      }
    ]
  },
  "message": "OK",
  "errorCode": ""
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» data|object|true|none||none|
|»» trendList|[object]|true|none||none|
|»»» date|string|false|none||none|
|»»» crashNum|integer|false|none||none|
|»»» crashUser|integer|false|none||none|
|»»» anrNum|integer|false|none||none|
|»»» anrUser|integer|false|none||none|
|»»» errorNum|integer|false|none||none|
|»»» errorUser|integer|false|none||none|
|»»» accessNum|integer|false|none||none|
|»»» accessUser|integer|false|none||none|
|» status|integer|true|none||none|
|» ret|integer|true|none||none|
|» message|string|true|none||none|
|» errorCode|string|true|none||none|

## POST To set issue-level tags.

POST /env/uniform/openapi/addTagsignature

To set issue-level tags.

Website： https://crashsight.wetest.net

> Body Parameters

```json
{
  "appId": "string",
  "platformId": 0,
  "issueId": "string",
  "tagName": "string"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» appId|body|string| yes |Project ID|
|» platformId|body|integer| yes |Platform ID Android：1，IOS：2，PC：10|
|» issueId|body|string| yes |Issue ID|
|» tagName|body|string| yes |Issue tags|

> Response Examples

```json
{
  "status": 200,
  "ret": {
    "statusCode": 0,
    "message": null,
    "tagInfoList": [
      {
        "tagId": 6807,
        "tagName": "1111"
      }
    ]
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» status|integer|true|none||Response status.|
|» ret|object|true|none||Query results.|
|»» statusCode|integer|true|none||query status code|
|»» message|string|true|none||error details|
|»» tagInfoList|object|true|none||error details|
|»»» tagId|integer|true|none||tag ID|
|»»» tagName|string|true|none||tag name|

## POST Get device list based on stack keyword

POST /env/uniform/openapi/getStackDeviceInfo/platformId/platformId/signature

Website： https://crashsight.wetest.net

> Body Parameters

```json
{
  "requestid": "string",
  "stime": "string",
  "etime": "string",
  "appId": "string",
  "params": {
    "keyName": "string"
  },
  "limit": 0,
  "type": "string"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» requestid|body|string| yes |Request ID|
|» stime|body|string| yes |Start Time|
|» etime|body|string| yes |End Time|
|» appId|body|string| yes |Project ID|
|» params|body|object| yes |filtering conditions|
|»» keyName|body|string| yes |stack keywords (supports * wildcard)|
|» limit|body|integer| yes |number of  returns|
|» type|body|string| yes |Default Return Values and fields. " type": "pretty" Returns the JSON format.|

> Response Examples

```json
{
  "requestid": "<REQUEST_ID>",
  "code": 200,
  "errmsg": null,
  "data": {
    "columns": null,
    "values": null,
    "results": [
      {
        "keyName": "*",
        "model": "<DEVICE_MODEL>",
        "osVersion": "Android 4.4.2,level 20",
        "crashNums": 4800,
        "crashUsers": 4800
      }
    ]
  },
  "cost": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» requestid|string|true|none||Request ID|
|» code|integer|true|none||Status Code|
|» errmsg|null|true|none||Error details|
|» data|object|true|none||query results|
|»» columns|null|true|none||fields|
|»» values|null|true|none||values|
|»» results|[object]|true|none||details|
|»»» keyName|string|false|none||none|
|»»» model|string|false|none||none|
|»»» osVersion|string|false|none||none|
|»»» crashNums|integer|false|none||none|
|»»» crashUsers|integer|false|none||none|
|» cost|integer|true|none||time-consuming|

## POST Get crash user list within a specific time period

POST /env/uniform/openapi/getCrashUserList/platformId/platformId/signature

Website： https://crashsight.wetest.net

download python code example:https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getCrashUserList.py

> Body Parameters

```json
{
  "stime": "2023-10-02 00:00:00",
  "etime": "2023-10-03 00:00:00",
  "appId": "<APP_ID>"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» requestid|body|string| yes |Request ID|
|» stime|body|string| yes |Start Time|
|» etime|body|string| yes |End Time.within 30d.|
|» limit|body|integer| yes |number of returns|
|» type|body|string| yes |response JSON format，"type":"pretty" default return value domain and column values|
|» appId|body|string| yes |Project ID|

> Response Examples

```json
{
  "requestid": null,
  "code": 200,
  "errmsg": null,
  "data": {
    "columns": [
      "user"
    ],
    "values": [
      [
        "xxxxxxx"
      ]
    ],
    "results": null
  },
  "cost": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» requestid|null|true|none||Request ID|
|» code|integer|true|none||Status Code|
|» errmsg|null|true|none||Error details|
|» data|object|true|none||none|
|»» columns|[string]|true|none||fields|
|»» values|[array]|true|none||values|
|»» results|null|true|none||none|
|» cost|integer|true|none||query duration|

## POST Get crash statistics based on stack keyword

POST /env/uniform/openapi/getStackCrashStat/platformId/platformId/signature

get crash statistics based on stack keyword

download python code example:https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getStackCrashStat.py

> Body Parameters

```json
{
  "requestid": "<REQUEST_ID>",
  "stime": "2023-10-13 00:00:00",
  "etime": "2023-10-16 00:00:00",
  "params": {
    "keyName": "*"
  },
  "type": "pretty",
  "appId": "<APP_ID>"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» requestid|body|string| yes |Request ID|
|» stime|body|string| yes |Start Time|
|» etime|body|string| yes |End Time.within 30d.|
|» appId|body|string| yes |Project ID|
|» params|body|object| yes |filtering conditions|
|»» keyName|body|string| yes |stack keywords (supports * wildcard)|
|» limit|body|integer| yes |number of  returns|
|» type|body|string| yes |Default Return Values and fields. " type": "pretty" Returns the JSON format.|

> Response Examples

```json
{
  "requestid": "<REQUEST_ID>",
  "code": 200,
  "errmsg": "null",
  "data": {
    "columns": null,
    "values": null,
    "results": [
      {
        "keyName": "*",
        "crashNums": 4799,
        "crashUsers": 4799
      }
    ]
  },
  "cost": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» requestid|string|true|none||Request ID|
|» code|integer|true|none||Status Code|
|» errmsg|null|true|none||Error details|
|» data|object|true|none||query result|
|»» columns|null|true|none||fields|
|»» values|null|true|none||values|
|»» results|[object]|true|none||details|
|»»» keyName|string|false|none||none|
|»»» crashNums|integer|false|none||none|
|»»» crashUsers|integer|false|none||none|
|» cost|integer|true|none||query duration|

## POST Get crash Stat based on device ID

POST /env/uniform/openapi/getCrashDeviceStat/platformId/platformId/signature

> Body Parameters

```json
{
  "requestid": "string",
  "stime": "string",
  "etime": "string",
  "appId": "string",
  "filters": {
    "deviceId": "string"
  },
  "limit": 0,
  "type": "string"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» requestid|body|string| yes |Request ID|
|» stime|body|string| yes |Start Time|
|» etime|body|string| yes |End Time|
|» appId|body|string| yes |none|
|» filters|body|object| yes |filtering conditions|
|»» deviceId|body|string| yes |device ID|
|» limit|body|integer| yes |Row limit, how many rows to get|
|» type|body|string| yes |Default Return Values and fields. " type": "pretty" Returns the JSON format.|

> Response Examples

```json
{
  "requestid": "<REQUEST_ID>",
  "code": 200,
  "errmsg": "null",
  "data": {
    "columns": null,
    "values": null,
    "results": [
      {
        "exceptionType": "java.lang.NullPointerException",
        "deviceId": "<DEVICE_UUID>",
        "issueId": "<ISSUE_ID>",
        "crashId": "<CRASH_ID>",
        "user": "979878",
        "hardware": "<DEVICE_MODEL>",
        "model": "<DEVICE_MODEL>"
      }
    ]
  },
  "cost": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» requestid|string|true|none||Request ID|
|» code|integer|true|none||Status Code|
|» errmsg|string|true|none||Error details|
|» data|object|true|none||query results|
|»» columns|null|true|none||fields|
|»» values|null|true|none||values|
|»» results|[object]|true|none||details|
|»»» exceptionType|string|false|none||none|
|»»» deviceId|string|false|none||none|
|»»» issueId|string|false|none||none|
|»»» crashId|string|false|none||none|
|»»» user|string|false|none||none|
|»»» hardware|string|false|none||none|
|»»» model|string|false|none||none|
|» cost|integer|true|none||Query Duration|

## POST Get crashHash list based on issue ID

POST /env/uniform/openapi/getCrashDeviceInfo/platformId/platformId/signature

> Body Parameters

```json
{
  "requestid": "string",
  "stime": "string",
  "etime": "string",
  "filters": {
    "issue": "string"
  },
  "limit": 0,
  "type": "string",
  "appId": "string"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» requestid|body|string| yes |none|
|» stime|body|string| yes |none|
|» etime|body|string| yes |none|
|» filters|body|object| yes |none|
|»» issue|body|string| yes |none|
|» limit|body|integer| yes |none|
|» type|body|string| yes |none|
|» appId|body|string| yes |none|

> Response Examples

```json
{
  "requestid": "<REQUEST_ID>",
  "code": 200,
  "errmsg": "null",
  "data": {
    "columns": "null",
    "values": null,
    "results": {
      "issueId": "<ISSUE_ID>",
      "crashTime": "2021-11-26 20:52:10 354",
      "crashId": "<CRASH_ID>",
      "user": "597862998"
    }
  },
  "cost": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» requestid|string|true|none||Request ID|
|» code|integer|true|none||Status Code|
|» errmsg|string|true|none||Error details|
|» data|object|true|none||Query  results|
|»» columns|string|true|none||fields|
|»» values|null|true|none||values|
|»» results|object|true|none||details|
|»»» issueId|string|true|none||Issue ID|
|»»» crashTime|string|true|none||crash Time|
|»»» crashId|string|true|none||crash ID|
|»»» user|string|true|none||user ID|
|» cost|integer|true|none||Query Duration|

## POST Get OpenId base on device ID

POST /env/uniform/openapi/getDeviceUserInfo/platformId/platformId/signature

> Body Parameters

```json
{
  "requestid": "",
  "stime": "",
  "etime": "",
  "filters": {
    "deviceId": ""
  },
  "limit": 0,
  "type": "",
  "appId": ""
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» requestid|body|string| yes |Request ID|
|» stime|body|string| yes |Start Time|
|» etime|body|string| yes |End Time|
|» filters|body|object| yes |filtering conditions|
|»» deviceId|body|string| yes |device ID|
|» limit|body|integer| yes |Row limit, how many rows to get|
|» type|body|string| yes |response JSON format，"type":"pretty" default return value domain and column values|
|» appId|body|string| yes |Project ID|

> Response Examples

```json
{
  "requestid": "<REQUEST_ID>",
  "code": 200,
  "errmsg": null,
  "data": {
    "columns": [
      "time",
      "userId"
    ],
    "values": [
      [
        "2022-01-12 11:45:55",
        "Unknown"
      ],
      [
        "2022-01-12 11:49:00",
        "Unknown"
      ],
      [
        "2022-01-12 11:38:27",
        "Unknown"
      ],
      [
        "2022-01-12 11:38:31",
        "Unknown"
      ],
      [
        "2022-01-12 11:39:17",
        "Unknown"
      ],
      [
        "2022-01-12 11:39:34",
        "Unknown"
      ],
      [
        "2022-01-12 11:42:40",
        "Unknown"
      ]
    ],
    "results": null
  },
  "cost": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» requestid|string|true|none||Request ID|
|» code|integer|true|none||Status Code|
|» errmsg|null|true|none||Error details|
|» data|object|true|none||Query  results|
|»» columns|[string]|true|none||none|
|»» values|[array]|true|none||Values|
|»» results|null|true|none||details|
|» cost|integer|true|none||Query Duration|

## GET Get notes based on issue ID

GET /env/uniform/openapi/noteListsignature

Website： https://crashsight.wetest.net

download python code example:https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_noteList.py

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|appId|query|string| no |Project ID|
|platformId|query|string| no |Platform ID Android：1，IOS：2，PC：10|
|issueId|query|string| no |Issue ID|
|crashDataType|query|string| no |Data Type|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|

> Response Examples

```json
{
  "status": 200,
  "ret": [
    {
      "appId": "<APP_ID>",
      "platformId": 1,
      "issueIds": "<ISSUE_ID>",
      "note": "mike",
      "createTime": "2021-06-25 09:56:16",
      "userId": "<USER_ID>",
      "newUserId": "",
      "issueStatus": 3,
      "processors": "",
      "tapdId": "",
      "bugUrl": "",
      "workspaceId": ""
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» status|integer|true|none||none|
|» ret|[object]|true|none||none|
|»» appId|string|false|none||Project ID|
|»» platformId|integer|false|none||Platform ID|
|»» issueIds|string|false|none||Issue ID|
|»» note|string|false|none||Note|
|»» createTime|string|false|none||Date of occurrence|
|»» userId|string|false|none||User ID|
|»» issueStatus|integer|false|none||Issue Status|
|»» processors|string|false|none||Handler|
|»» tapdId|string|false|none||tapd ID|
|»» bugUrl|string|false|none||tapd url|
|»» workspaceId|string|false|none||tapd_workspaceId|

## GET Get issue details

GET /env/uniform/openapi/issueInfosignature

get issue details

Website： https://crashsight.wetest.net

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|appId|query|string| yes |Project ID|
|platformId|query|string| yes |Platform ID Android：1，IOS：2，PC：10|
|issueId|query|string| yes |Issue ID|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|

> Response Examples

```json
{
  "status": 200,
  "ret": {
    "issueId": "<ISSUE_ID>",
    "exceptionName": "SIGILL(ILL_ILLOPC)",
    "exceptionMessage": "",
    "keyStack": "#00 pc 0000000002f0248c libUE4.so Reset (D:/SA_Client\\SA\\branches\\obt\\UE4Engine\\Engine\\Source\\Runtime\\Core\\Public\\Containers/SparseArray.h:254) [arm64-v8a]",
    "lastestUploadTime": "2021-06-15 11:54:36 199",
    "latestUploadTimestamp": 0,
    "imeiCount": 1,
    "sysImeiCount": 0,
    "count": 1,
    "sysCount": 0,
    "version": "#$cv#$",
    "tagInfoList": [],
    "processor": "",
    "status": 0,
    "firstUploadTime": "2021-06-15 11:54:36 199",
    "firstUploadTimestamp": 1623729276199,
    "issueHash": "E9:1C:FD:D6:B0:AD:F3:29:B3:DF:C7:C7:EE:0E:D9:52",
    "ftName": "",
    "issueVersions": [
      {
        "version": "<APP_VERSION>",
        "firstUploadTime": "2021-06-15 11:54:36 199",
        "firstUploadTimestamp": 0,
        "lastUploadTime": "2021-06-15 11:54:36 199",
        "lastUploadTimestamp": 0,
        "count": 1,
        "deviceCount": 1
      }
    ],
    "detailId": "",
    "parentHash": "",
    "bugs": null
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» status|integer|true|none||none|
|» ret|object|true|none||none|
|»» issueId|string|true|none||Issue ID|
|»» exceptionName|string|true|none||none|
|»» exceptionMessage|string|true|none||none|
|»» keyStack|string|true|none||none|
|»» lastestUploadTime|string|true|none||none|
|»» latestUploadTimestamp|integer|true|none||none|
|»» imeiCount|integer|true|none||Affected Devices|
|»» sysImeiCount|integer|true|none||none|
|»» count|integer|true|none||Affected Times|
|»» sysCount|integer|true|none||none|
|»» version|string|true|none||none|
|»» tagInfoList|[string]|true|none||tag information|
|»» processor|string|true|none||none|
|»» status|integer|true|none||none|
|»» firstUploadTime|string|true|none||none|
|»» firstUploadTimestamp|integer|true|none||none|
|»» issueHash|string|true|none||none|
|»» ftName|string|true|none||none|
|»» issueVersions|[object]|true|none||version list|
|»»» version|string|false|none||none|
|»»» firstUploadTime|string|false|none||none|
|»»» firstUploadTimestamp|integer|false|none||none|
|»»» lastUploadTime|string|false|none||none|
|»»» lastUploadTimestamp|integer|false|none||none|
|»»» count|integer|false|none||Affected Times|
|»»» deviceCount|integer|false|none||Affected Devices|
|»» detailId|string|true|none||none|
|»» parentHash|string|true|none||none|
|»» bugs|null|true|none||none|

## GET Get the most recent crash hash based on issue ID

GET /env/uniform/openapi/lastCrashInfosignature

Website： https://crashsight.wetest.net

download python code example:https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_lastCrashInfo.py

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|appId|query|string| no |Project ID|
|platformId|query|integer| no |Platform ID Android：1，IOS：2，PC：10|
|issues|query|string| no |Issue ID|
|crashDataType|query|string| no |Data Type. This is a fixed value.|
|fsn|query|string| no |request ID|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|

> Response Examples

```json
{
  "code": 100000,
  "msg": "成功",
  "data": {
    "userId": null,
    "processName": "com.example.demo",
    "threadName": "Thread-221(221)",
    "crashId": "<CRASH_ID>",
    "crashHash": "A2:84:49:50:BA:6B:2A:2D:9F:42:EB:C2:F1:F6:4E:77",
    "crashTime": "2020-05-07 18:36:48",
    "uploadTime": "2021-06-11 13:20:12",
    "bundleId": "com.example.demo",
    "productVersion": "<APP_VERSION>",
    "startTime": "1588837884696",
    "appInBack": "false",
    "hardware": "<DEVICE_MODEL>",
    "modelOriginalName": "<DEVICE_MODEL>",
    "osVersion": "Android 4.4.2,level 20",
    "rom": "fail%2Ffail",
    "cpuName": "fail",
    "cpuType": "i686",
    "type": "100",
    "callStack": "2020507Test4",
    "retraceCrashDetail": "2020507Test4",
    "gpuName": null,
    "dumpId": null,
    "new_dumpid": null,
    "mac": null,
    "launchTime": 9924
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» userId|null|true|none||none|
|»» processName|string|true|none||none|
|»» threadName|string|true|none||none|
|»» crashId|string|true|none||none|
|»» crashHash|string|true|none||none|
|»» crashTime|string|true|none||none|
|»» uploadTime|string|true|none||none|
|»» bundleId|string|true|none||none|
|»» productVersion|string|true|none||none|
|»» startTime|string|true|none||none|
|»» appInBack|string|true|none||none|
|»» hardware|string|true|none||none|
|»» modelOriginalName|string|true|none||none|
|»» osVersion|string|true|none||none|
|»» rom|string|true|none||none|
|»» cpuName|string|true|none||none|
|»» cpuType|string|true|none||none|
|»» type|string|true|none||none|
|»» callStack|string|true|none||none|
|»» retraceCrashDetail|string|true|none||none|
|»» gpuName|null|true|none||none|
|»» dumpId|null|true|none||none|
|»» new_dumpid|null|true|none||none|
|»» mac|null|true|none||none|
|»» launchTime|integer|true|none||none|

## POST Get the list of crash hashes based on an issue ID

POST /env/uniform/openapi/crashListsignature

To get a list of crash hashes based on an issue,

Website： https://crashsight.wetest.net
download python code example: https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_crashList.py

> Body Parameters

```json
{
  "appId": "<APP_ID>",
  "crashDataType": "undefined",
  "start": 0,
  "searchType": "detail",
  "exceptionTypeList": "",
  "platformId": 1,
  "issueId": "<ISSUE_ID>",
  "rows": 10,
  "version": ""
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» appId|body|string| yes |none|
|» crashDataType|body|string| yes |none|
|» start|body|integer| yes |none|
|» searchType|body|string| yes |none|
|» exceptionTypeList|body|string| yes |none|
|» platformId|body|integer| yes |none|
|» issueId|body|string| yes |none|
|» rows|body|integer| yes |none|
|» version|body|string| yes |none|

> Response Examples

```json
{
  "status": 200,
  "ret": {
    "statusCode": 0,
    "message": null,
    "reqSendstamp": 0,
    "rspReceivedTiamp": 0,
    "rspSendTimestamp": 0,
    "numFound": 1,
    "issueList": [],
    "crashIdList": [
      "<CRASH_ID>"
    ],
    "crashDatas": {
      "<CRASH_ID>": {
        "productVersion": "<APP_VERSION>",
        "dumpId": "A9179A653872743CD2A11891B9120",
        "model": "<DEVICE_MODEL>",
        "id": "<CRASH_ID>",
        "uploadTime": "2021-06-17 12:53:22",
        "crashId": "<CRASH_ID>",
        "osVer": "Microsoft Windows 10-sp0.0",
        "deviceId": "[secret_info]",
        "userId": "[secret_info]"
      }
    },
    "detailDatas": null,
    "tagInfoList": null,
    "tagList": null,
    "crashNums": 0,
    "anrNums": 0,
    "errorNums": 0,
    "scrollId": null
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» status|integer|true|none||none|
|» ret|object|true|none||none|
|»» statusCode|integer|true|none||none|
|»» message|null|true|none||none|
|»» reqSendstamp|integer|true|none||Private field|
|»» rspReceivedTiamp|integer|true|none||Private field|
|»» rspSendTimestamp|integer|true|none||Private field|
|»» numFound|integer|true|none||none|
|»» issueList|[string]|true|none||none|
|»» crashIdList|[string]|true|none||none|
|»» crashDatas|object|true|none||none|
|»»» <CRASH_ID>|object|true|none||none|
|»»»» productVersion|string|true|none||none|
|»»»» dumpId|string|true|none||none|
|»»»» model|string|true|none||none|
|»»»» id|string|true|none||none|
|»»»» uploadTime|string|true|none||none|
|»»»» crashId|string|true|none||none|
|»»»» osVer|string|true|none||none|
|»»»» deviceId|string|true|none||none|
|»»»» userId|string|true|none||none|
|»» detailDatas|null|true|none||none|
|»» tagInfoList|null|true|none||none|
|»» tagList|null|true|none||none|
|»» crashNums|integer|true|none||none|
|»» anrNums|integer|true|none||none|
|»» errorNums|integer|true|none||none|
|»» scrollId|null|true|none||none|

## GET Get the trace data, trace logs, additional information, and custom key-value pairs

GET /env/uniform/openapi/appDetailCrashsignature

To get the trace data, trace logs, additional information, and custom key-value pairs

Website： https://crashsight.wetest.net

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|appId|query|string| no |Project ID|
|platformId|query|integer| no |Platform ID|
|crashHash|query|string| no |crashHash|
|fsn|query|string| no |Request ID|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|

> Response Examples

```json
{
  "status": 200,
  "ret": {
    "attachName": "valueMapOthers.txt;log.txt;",
    "stackName": "FileObserver(202);main(1);FinalizerWatchdogDaemon(191);crashsightThread-1(200);OkHttp ConnectionPool(219);Signal Catcher(187);AsyncTask #3(196);Binder_2(193);crashsightThread-2(201);JDWP(188);AsyncTask #2(195);FinalizerDaemon(190);ReferenceQueueDaemon(189);crashsightThread-3(203);java.lang.ProcessManager(206);Thread-220(220);Binder_3(207);Binder_1(192);AsyncTask #1(194);GC(186);",
    "attachList": [
      {
        "fileName": "valueMapOthers.txt",
        "fileType": 3,
        "content": "A23:3.2.5;A24:Android 4.4.2,level 16;A25:hx6DLV78mm9ChnvC;F09:1;C03_testkey:testvalue;C04_APP_ID:a81f9c7e38;"
      },
      {
        "fileName": "log.txt",
        "fileType": 1,
        "content": "Report: stack frame :2, has cause false\n05-07 17:20:13.626  4883  5108 I CrashReport: try to upload right now\n05-07 17:20:13.626  4883  5108 D CrashReport: Uploading frequency will not be checked if SDK is in debug mode.\n05-07 17:20:13.626  4883  5108 D CrashReport: java.lang.RuntimeException rid:<UUID> sess:<UUID> ls:5328s isR:false isF:true isM:false isN:false mc:0 ,null ,isUp:false ,vm:33\n"
      },
      {
        "fileName": "testkey",
        "fileType": 6,
        "content": "testvalue"
      },
      {
        "fileName": "APP_ID",
        "fileType": 7,
        "content": "a81f9c7e38"
      },
      {
        "fileName": "main(1)",
        "fileType": 2,
        "content": "android.os.MessageQueue.nativePollOnce(Native Method)\nandroid.os.MessageQueue.next(MessageQueue.java:138)\nandroid.os.Looper.loop(Looper.java:123)\nandroid.app.ActivityThread.main(ActivityThread.java:5019)\njava.lang.reflect.Method.invokeNative(Native Method)\njava.lang.reflect.Method.invoke(Method.java:515)\ncom.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:779)\ncom.android.internal.os.ZygoteInit.main(ZygoteInit.java:595)\ndalvik.system.NativeStart.main(Native Method)\n"
      },
      {
        "fileName": "GC(186)",
        "fileType": 2,
        "content": "dalvik.system.NativeStart.run(Native Method)\n"
      },
      {
        "fileName": "Signal Catcher(187)",
        "fileType": 2,
        "content": "dalvik.system.NativeStart.run(Native Method)\n"
      },
      {
        "fileName": "JDWP(188)",
        "fileType": 2,
        "content": "dalvik.system.NativeStart.run(Native Method)\n"
      },
      {
        "fileName": "ReferenceQueueDaemon(189)",
        "fileType": 2,
        "content": "java.lang.Object.wait(Native Method)\njava.lang.Object.wait(Object.java:364)\njava.lang.Daemons$ReferenceQueueDaemon.run(Daemons.java:130)\njava.lang.Thread.run(Thread.java:841)\n"
      },
      {
        "fileName": "FinalizerDaemon(190)",
        "fileType": 2,
        "content": "java.lang.Object.wait(Native Method)\njava.lang.Object.wait(Object.java:401)\njava.lang.ref.ReferenceQueue.remove(ReferenceQueue.java:102)\njava.lang.ref.ReferenceQueue.remove(ReferenceQueue.java:73)\njava.lang.Daemons$FinalizerDaemon.run(Daemons.java:170)\njava.lang.Thread.run(Thread.java:841)\n"
      },
      {
        "fileName": "FinalizerWatchdogDaemon(191)",
        "fileType": 2,
        "content": "java.lang.VMThread.sleep(Native Method)\njava.lang.Thread.sleep(Thread.java:1013)\njava.lang.Thread.sleep(Thread.java:995)\njava.lang.Daemons$FinalizerWatchdogDaemon.sleepFor(Daemons.java:248)\njava.lang.Daemons$FinalizerWatchdogDaemon.waitForFinalization(Daemons.java:258)\njava.lang.Daemons$FinalizerWatchdogDaemon.run(Daemons.java:212)\njava.lang.Thread.run(Thread.java:841)\n"
      },
      {
        "fileName": "Binder_1(192)",
        "fileType": 2,
        "content": "dalvik.system.NativeStart.run(Native Method)\n"
      },
      {
        "fileName": "Binder_2(193)",
        "fileType": 2,
        "content": "dalvik.system.NativeStart.run(Native Method)\n"
      },
      {
        "fileName": "AsyncTask #1(194)",
        "fileType": 2,
        "content": "java.lang.Object.wait(Native Method)\njava.lang.Thread.parkFor(Thread.java:1205)\nsun.misc.Unsafe.park(Unsafe.java:325)\njava.util.concurrent.locks.LockSupport.park(LockSupport.java:157)\njava.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject.await(AbstractQueuedSynchronizer.java:2017)\njava.util.concurrent.LinkedBlockingQueue.take(LinkedBlockingQueue.java:410)\njava.util.concurrent.ThreadPoolExecutor.getTask(ThreadPoolExecutor.java:1035)\njava.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1097)\njava.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:587)\njava.lang.Thread.run(Thread.java:841)\n"
      },
      {
        "fileName": "AsyncTask #2(195)",
        "fileType": 2,
        "content": "java.lang.Object.wait(Native Method)\njava.lang.Thread.parkFor(Thread.java:1205)\nsun.misc.Unsafe.park(Unsafe.java:325)\njava.util.concurrent.locks.LockSupport.park(LockSupport.java:157)\njava.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject.await(AbstractQueuedSynchronizer.java:2017)\njava.util.concurrent.LinkedBlockingQueue.take(LinkedBlockingQueue.java:410)\njava.util.concurrent.ThreadPoolExecutor.getTask(ThreadPoolExecutor.java:1035)\njava.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1097)\njava.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:587)\njava.lang.Thread.run(Thread.java:841)\n"
      },
      {
        "fileName": "AsyncTask #3(196)",
        "fileType": 2,
        "content": "java.lang.Object.wait(Native Method)\njava.lang.Thread.parkFor(Thread.java:1205)\nsun.misc.Unsafe.park(Unsafe.java:325)\njava.util.concurrent.locks.LockSupport.park(LockSupport.java:157)\njava.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject.await(AbstractQueuedSynchronizer.java:2017)\njava.util.concurrent.LinkedBlockingQueue.take(LinkedBlockingQueue.java:410)\njava.util.concurrent.ThreadPoolExecutor.getTask(ThreadPoolExecutor.java:1035)\njava.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1097)\njava.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:587)\njava.lang.Thread.run(Thread.java:841)\n"
      },
      {
        "fileName": "crashsightThread-1(200)",
        "fileType": 2,
        "content": "java.lang.Object.wait(Native Method)\njava.lang.Thread.parkFor(Thread.java:1205)\nsun.misc.Unsafe.park(Unsafe.java:325)\njava.util.concurrent.locks.LockSupport.parkNanos(LockSupport.java:197)\njava.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject.awaitNanos(AbstractQueuedSynchronizer.java:2056)\njava.util.concurrent.ScheduledThreadPoolExecutor$DelayedWorkQueue.take(ScheduledThreadPoolExecutor.java:1062)\njava.util.concurrent.ScheduledThreadPoolExecutor$DelayedWorkQueue.take(ScheduledThreadPoolExecutor.java:778)\njava.util.concurrent.ThreadPoolExecutor.getTask(ThreadPoolExecutor.java:1035)\njava.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1097)\njava.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:587)\njava.lang.Thread.run(Thread.java:841)\n"
      },
      {
        "fileName": "crashsightThread-2(201)",
        "fileType": 2,
        "content": "java.lang.Object.wait(Native Method)\njava.lang.Thread.parkFor(Thread.java:1205)\nsun.misc.Unsafe.park(Unsafe.java:325)\njava.util.concurrent.locks.LockSupport.park(LockSupport.java:157)\njava.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject.await(AbstractQueuedSynchronizer.java:2017)\njava.util.concurrent.ScheduledThreadPoolExecutor$DelayedWorkQueue.take(ScheduledThreadPoolExecutor.java:1057)\njava.util.concurrent.ScheduledThreadPoolExecutor$DelayedWorkQueue.take(ScheduledThreadPoolExecutor.java:778)\njava.util.concurrent.ThreadPoolExecutor.getTask(ThreadPoolExecutor.java:1035)\njava.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1097)\njava.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:587)\njava.lang.Thread.run(Thread.java:841)\n"
      }
    ],
    "sysLogs": [
      "Report: stack frame :2, has cause false",
      "05-07 17:20:13.626  4883  5108 I CrashReport: try to upload right now",
      "05-07 17:20:13.626  4883  5108 D CrashReport: Uploading frequency will not be checked if SDK is in debug mode.",
      "05-07 17:20:13.626  4883  5108 D CrashReport: java.lang.RuntimeException rid:<UUID> sess:<UUID> ls:5328s isR:false isF:true isM:false isN:false mc:0 ,null ,isUp:false ,vm:33",
      "05-07 17:20:13.646  4883  5108 D dalvikvm: GC_FOR_ALLOC freed 494K, 54% free 4512K/9704K, paused 4ms, total 4ms",
      "05-07 17:20:13.646  4883  5108 D CrashReport: [UploadManager] Add upload task (pid=4883 | tid=5108)",
      "05-07 17:20:13.646  4883  5108 D CrashReport: [UploadManager] Sucessfully got session ID, try to execute upload task now (pid=4883 | tid=5108)"
    ],
    "userLogs": [
      ""
    ]
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» status|integer|true|none||none|
|» ret|object|true|none||none|
|»» attachName|string|true|none||none|
|»» stackName|string|true|none||none|
|»» attachList|[object]|true|none||none|
|»»» fileName|string|true|none||none|
|»»» fileType|integer|true|none||none|
|»»» content|string|true|none||none|
|»» sysLogs|[string]|true|none||none|
|»» userLogs|[string]|true|none||none|

## GET Get crash details

GET /env/uniform/openapi/crashDocsignature

Website： https://crashsight.wetest.net

download python code example: https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_crashDoc.py

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|appId|query|string| no |Project ID|
|platformId|query|string| no |Platform ID Android：1，IOS：2，PC：10|
|crashHash|query|string| no |crash ID|
|fsn|query|string| no |RequestID. The fsn value can be fixed|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|

> Response Examples

```json
{
  "statusCode": 0,
  "message": null,
  "reqSendTimestamp": 0,
  "rspReceivedTimestamp": 0,
  "rspSendTimestamp": 0,
  "numFound": 0,
  "crashMap": {
    "id": "<DEVICE_MAC>",
    "issueId": "<ISSUE_ID>",
    "productVersion": "<APP_VERSION>",
    "model": "<DEVICE_MODEL>",
    "userId": "<USER_ID>",
    "expMessage": "sNSXTvFGp6ZGrorljP6WPxsGtKc5px",
    "type": "100",
    "processName": "com.example.demo",
    "retraceStatus": -3,
    "uploadTime": "2021-04-09T12:21:25.663+0000",
    "uploadTimestamp": 1617970885663,
    "crashTime": "2020-05-07T10:36:48.991+0000",
    "crashTimestamp": 1588847808991,
    "mergeVersion": "11",
    "messageVersion": "2",
    "isSystemStack": 1,
    "rqdUuid": "<REPORT_UUID>",
    "retraceResult": "1_0_2_0_0_0_0_9_0",
    "appInBack": "false",
    "cpuType": "x86",
    "subVersionIssueId": "<ISSUE_ID>",
    "crashId": "<CRASH_ID>",
    "bundleId": "com.example.demo",
    "sdkVersion": "3.1.7(1.6.0)-3.7.1",
    "osVer": "Android 4.4.2,level 16",
    "expAddr": "com.example.demo.MainActivity$11$2.run(MainActivity.java:529)",
    "threadName": "Thread-221(221)",
    "memSize": "1587986432",
    "diskSize": "33999818752",
    "imei": "null",
    "imsi": "null",
    "cpuName": "fail",
    "brand": "samsung",
    "freeMem": "1168867328",
    "freeStorage": "31347867648",
    "freeSdCard": "31347867648",
    "mac": "null",
    "country": "CN",
    "totalSD": "33999818752",
    "channelId": "testchannel",
    "startTime": "1588837884696",
    "startTimestamp": 1588837884696,
    "callStack": "irgMyesZayrR",
    "retraceCrashDetail": "irgMyesZayrR",
    "buildNumber": "samsung",
    "rom": "fail%2Ffail",
    "retraceTimestamp": 0,
    "apn": "WIFI",
    "appInAppstore": false,
    "expName": "java.lang.RuntimeException",
    "deviceId": "hx6DLV78mm9ChnvC",
    "crashCount": 0,
    "isRooted": "true",
    "isVirtualMachine": 320,
    "modelOriginalName": "<DEVICE_MODEL>"
  },
  "detailMap": {
    "attatchCount": 0,
    "quaInner": null,
    "appInfo": null,
    "stackName": "FileObserver(202);main(1);FinalizerWatchdogDaemon(191);crashsightThread-1(200);OkHttp ConnectionPool(219);Signal Catcher(187);AsyncTask #3(196);Binder_2(193);crashsightThread-2(201);JDWP(188);AsyncTask #2(195);FinalizerDaemon(190);ReferenceQueueDaemon(189);crashsightThread-3(203);java.lang.ProcessManager(206);Thread-220(220);Binder_3(207);Binder_1(192);AsyncTask #1(194);GC(186);",
    "excepitonAddress": null,
    "retraceCrashDetail": "irgMyesZayrR",
    "freeMem": 0,
    "appBaseAddr": null,
    "battery": 0,
    "now": null,
    "archVersion": null,
    "attachName": "valueMapOthers.txt;log.txt;",
    "tel": null,
    "id": "<DEVICE_MAC>",
    "fileList": [
      {
        "fileName": "valueMapOthers.txt",
        "codeType": 0,
        "fileType": 3,
        "fileContent": "A23:3.2.5;A24:Android 4.4.2,level 16;A25:hx6DLV78mm9ChnvC;F09:1;C03_testkey:testvalue;C04_APP_ID:a81f9c7e38;"
      },
      {
        "fileName": "log.txt",
        "codeType": 0,
        "fileType": 1,
        "fileContent": "Report: stack frame :2, has cause false\n05-07 17:20:13.626  4883  5108 I CrashReport: try to upload right now\n05-07 17:20:13.626  4883  5108 D CrashReport: Uploading frequency will not be checked if SDK is in debug mode.\n05-07 17:20:13.626  4883  5108 D CrashReport: java.lang.RuntimeException rid:<UUID> sess:<UUID> ls:5328s isR:false isF:true isM:false isN:false mc:0 ,null ,isUp:false ,vm:33"
      },
      {
        "fileName": "main(1)",
        "codeType": 0,
        "fileType": 2,
        "fileContent": "android.os.MessageQueue.nativePollOnce(Native Method)\nandroid.os.MessageQueue.next(MessageQueue.java:138)\nandroid.os.Looper.loop(Looper.java:123)\nandroid.app.ActivityThread.main(ActivityThread.java:5019)\njava.lang.reflect.Method.invokeNative(Native Method)\njava.lang.reflect.Method.invoke(Method.java:515)\ncom.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:779)\ncom.android.internal.os.ZygoteInit.main(ZygoteInit.java:595)\ndalvik.system.NativeStart.main(Native Method)\n"
      },
      {
        "fileName": "GC(186)",
        "codeType": 0,
        "fileType": 2,
        "fileContent": "dalvik.system.NativeStart.run(Native Method)\n"
      },
      {
        "fileName": "Signal Catcher(187)",
        "codeType": 0,
        "fileType": 2,
        "fileContent": "dalvik.system.NativeStart.run(Native Method)\n"
      },
      {
        "fileName": "JDWP(188)",
        "codeType": 0,
        "fileType": 2,
        "fileContent": "dalvik.system.NativeStart.run(Native Method)\n"
      },
      {
        "fileName": "ReferenceQueueDaemon(189)",
        "codeType": 0,
        "fileType": 2,
        "fileContent": "java.lang.Object.wait(Native Method)\njava.lang.Object.wait(Object.java:364)\njava.lang.Daemons$ReferenceQueueDaemon.run(Daemons.java:130)\njava.lang.Thread.run(Thread.java:841)\n"
      },
      {
        "fileName": "Thread-220(220)",
        "codeType": 0,
        "fileType": 2,
        "fileContent": "com.example.demo.MainActivity$11$2.run(MainActivity.java:529)\njava.lang.Thread.run(Thread.java:841)\n"
      },
      {
        "fileName": "testkey",
        "codeType": 0,
        "fileType": 6,
        "fileContent": "testvalue"
      },
      {
        "fileName": "APP_ID",
        "codeType": 0,
        "fileType": 7,
        "fileContent": "<APP_ID>"
      }
    ],
    "email": null,
    "srcIp": "<DEVICE_IP>",
    "uploadTimestamp": 1617970885663,
    "productIdentity": null,
    "freeSdCard": 0,
    "serverKey": "APP_ID;",
    "isGZIP": 0,
    "cpu": 0,
    "uploadTime": "2021-04-09T12:21:25.663+0000",
    "userKey": "testkey;",
    "romName": "fail%2Ffail",
    "threadName": null,
    "contactAll": "<CONTACT_HASH>",
    "sdkId": null,
    "callStack": "irgMyesZayrR",
    "fileDir": null,
    "sdkVersion": "3.2.5",
    "comment": null,
    "freeStorage": 0
  },
  "launchTime": 9924
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» statusCode|integer|true|none||none|
|» message|null|true|none||none|
|» reqSendTimestamp|integer|true|none||none|
|» rspReceivedTimestamp|integer|true|none||none|
|» rspSendTimestamp|integer|true|none||none|
|» numFound|integer|true|none||none|
|» crashMap|object|true|none||none|
|»» id|string|true|none||none|
|»» issueId|string|true|none||none|
|»» productVersion|string|true|none||none|
|»» model|string|true|none||none|
|»» userId|string|true|none||none|
|»» expMessage|string|true|none||none|
|»» type|string|true|none||none|
|»» processName|string|true|none||none|
|»» retraceStatus|integer|true|none||none|
|»» uploadTime|string|true|none||none|
|»» uploadTimestamp|integer|true|none||none|
|»» crashTime|string|true|none||none|
|»» crashTimestamp|integer|true|none||none|
|»» mergeVersion|string|true|none||none|
|»» messageVersion|string|true|none||none|
|»» isSystemStack|integer|true|none||none|
|»» rqdUuid|string|true|none||none|
|»» retraceResult|string|true|none||none|
|»» appInBack|string|true|none||none|
|»» cpuType|string|true|none||none|
|»» subVersionIssueId|string|true|none||none|
|»» crashId|string|true|none||none|
|»» bundleId|string|true|none||none|
|»» sdkVersion|string|true|none||none|
|»» osVer|string|true|none||none|
|»» expAddr|string|true|none||none|
|»» threadName|string|true|none||none|
|»» memSize|string|true|none||none|
|»» diskSize|string|true|none||none|
|»» imei|string|true|none||none|
|»» imsi|string|true|none||none|
|»» cpuName|string|true|none||none|
|»» brand|string|true|none||none|
|»» freeMem|string|true|none||none|
|»» freeStorage|string|true|none||none|
|»» freeSdCard|string|true|none||none|
|»» mac|string|true|none||none|
|»» country|string|true|none||none|
|»» totalSD|string|true|none||none|
|»» channelId|string|true|none||none|
|»» startTime|string|true|none||none|
|»» startTimestamp|integer|true|none||none|
|»» callStack|string|true|none||none|
|»» retraceCrashDetail|string|true|none||none|
|»» buildNumber|string|true|none||none|
|»» rom|string|true|none||none|
|»» retraceTimestamp|integer|true|none||none|
|»» apn|string|true|none||none|
|»» appInAppstore|boolean|true|none||none|
|»» expName|string|true|none||none|
|»» deviceId|string|true|none||none|
|»» crashCount|integer|true|none||none|
|»» isRooted|string|true|none||none|
|»» isVirtualMachine|integer|true|none||none|
|»» modelOriginalName|string|true|none||none|
|» detailMap|object|true|none||none|
|»» attatchCount|integer|true|none||none|
|»» quaInner|null|true|none||none|
|»» appInfo|null|true|none||none|
|»» stackName|string|true|none||none|
|»» excepitonAddress|null|true|none||none|
|»» retraceCrashDetail|string|true|none||none|
|»» freeMem|integer|true|none||none|
|»» appBaseAddr|null|true|none||none|
|»» battery|integer|true|none||none|
|»» now|null|true|none||none|
|»» archVersion|null|true|none||none|
|»» attachName|string|true|none||none|
|»» tel|null|true|none||none|
|»» id|string|true|none||none|
|»» fileList|[object]|true|none||none|
|»»» fileName|string|true|none||none|
|»»» codeType|integer|true|none||none|
|»»» fileType|integer|true|none||none|
|»»» fileContent|string|true|none||none|
|»» email|null|true|none||none|
|»» srcIp|string|true|none||none|
|»» uploadTimestamp|integer|true|none||none|
|»» productIdentity|null|true|none||none|
|»» freeSdCard|integer|true|none||none|
|»» serverKey|string|true|none||none|
|»» isGZIP|integer|true|none||none|
|»» cpu|integer|true|none||none|
|»» uploadTime|string|true|none||none|
|»» userKey|string|true|none||none|
|»» romName|string|true|none||none|
|»» threadName|null|true|none||none|
|»» contactAll|string|true|none||none|
|»» sdkId|null|true|none||none|
|»» callStack|string|true|none||none|
|»» fileDir|null|true|none||none|
|»» sdkVersion|string|true|none||none|
|»» comment|null|true|none||none|
|»» freeStorage|integer|true|none||none|
|» launchTime|integer|true|none||none|

## POST Get Issue list

POST /env/uniform/openapi/queryIssueListsignature

Get Issue list

Website： https://crashsight.wetest.net

download python code example:https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_queryIssueList.py

> Body Parameters

```json
{
  "appId": "string",
  "platformId": 0,
  "rows": 0,
  "exceptionTypeList": "string",
  "sortOrder": "string",
  "status": "string",
  "sortField": "string",
  "date": "string"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» appId|body|string| yes |Project ID|
|» platformId|body|integer| yes |Platform ID Android：1，IOS：2，PC：10|
|» rows|body|integer| yes |Row limit, how many rows to get|
|» exceptionTypeList|body|string| yes |The array of exception types, separated by commas, with supported exception types: Crash, Native, AllCatched, ANR, Unity3D, AllCrash, ExtensionCrash, Lua, JS.|
|» sortOrder|body|string| yes |The sorting order.For example:  "desc" for descending order "asc" for ascending order|
|» status|body|string| yes |The optional parameter to filter by issue handling status. 0: Not Processed, 1: Processed, 2: In Progress, with multiple options supported.|
|» sortField|body|string| yes |sorting field|
|» date|body|string| yes |The parameter to filter by the latest time period for issues.|

> Response Examples

```json
{
  "status": 200,
  "ret": {
    "appId": "<APP_ID>",
    "platformId": "1",
    "issueList": [
      {
        "crashNum": 1184,
        "exceptionName": "java.lang.RuntimeException",
        "exceptionMessage": "sNSXTvFGp6ZGrorljP6WPxsGtKc5px",
        "keyStack": "",
        "lastestUploadTime": "2021-04-09 20:21:25 663",
        "issueId": "<ISSUE_ID>",
        "imeiCount": 596,
        "processor": "",
        "status": 0,
        "tagInfoList": [],
        "count": 1184,
        "version": "#$cv#$",
        "ftName": "",
        "issueVersions": [
          {
            "version": "<APP_VERSION>",
            "firstUploadTime": null,
            "firstUploadTimestamp": 0,
            "lastUploadTime": null,
            "lastUploadTimestamp": 0,
            "count": 0,
            "deviceCount": 0
          }
        ]
      }
    ],
    "numFound": 1
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» status|integer|true|none||none|
|» ret|object|true|none||none|
|»» appId|string|true|none||Project ID|
|»» platformId|string|true|none||Platform ID|
|»» issueList|[object]|true|none||Issue List|
|»»» crashNum|integer|false|none||Affected Times|
|»»» exceptionName|string|false|none||Exception Name|
|»»» exceptionMessage|string|false|none||Exception Message|
|»»» keyStack|string|false|none||Stack Information|
|»»» lastestUploadTime|string|false|none||Latest Report Time|
|»»» issueId|string|false|none||Issue ID|
|»»» imeiCount|integer|false|none||Affected Devices|
|»»» processor|string|false|none||Handlers|
|»»» status|integer|false|none||Issue Status|
|»»» tagInfoList|[string]|false|none||Tag info|
|»»» count|integer|false|none||Affected Times|
|»»» version|string|false|none||Tag info|
|»»» ftName|string|false|none||none|
|»»» issueVersions|[object]|false|none||Sub-issue versions|
|»»»» version|string|false|none||Version|
|»»»» firstUploadTime|null|false|none||First Report Time|
|»»»» firstUploadTimestamp|integer|false|none||First Report Timestamp|
|»»»» lastUploadTime|null|false|none||Recent report time|
|»»»» lastUploadTimestamp|integer|false|none||Recent report timestamp|
|»»»» count|integer|false|none||Affected Times|
|»»»» deviceCount|integer|false|none||Affected Devices|
|»» numFound|integer|true|none||Total crash count|

# API Reference/Others

## GET Get the list of versions, bundle, and handlers

GET /env/uniform/openapi/getSelectorDatassignature

Get the list of versions, bundle, and handlers

Website： https://crashsight.wetest.net

download python code example:https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getSelectorDatas.py

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|appId|query|string| yes |Project ID|
|pid|query|string| yes |Platform ID Android：1，IOS：2，PC：10|
|fsn|query|string| no |RequestID. The fsn value can be fixed|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|

> Response Examples

```json
{
  "status": 200,
  "ret": {
    "code": 200,
    "message": "OK",
    "errorCode": "",
    "data": {
      "versionList": [
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "productVersion": "<APP_VERSION>",
          "enable": 1,
          "isShow": true,
          "enableAutoUpgrade": false,
          "sdkVersion": "3.1.7(1.6.0)-3.7.1"
        }
      ],
      "tagList": [
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "tagId": 2099,
          "tagName": "哈哈哈哈哈",
          "isShow": 1
        }
      ],
      "processorList": [
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 1,
          "userId": "<USER_ID>",
          "registerTime": "2020-08-31 04:40:01",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 0
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 1,
          "userId": "<USER_ID>",
          "registerTime": "2020-08-31 03:36:54",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 0
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 1,
          "userId": "<USER_ID>",
          "registerTime": "2021-01-19 18:58:33",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 0
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 1,
          "userId": "<USER_ID>",
          "registerTime": "2021-05-13 14:43:02",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 0
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 2,
          "userId": "<USER_ID>",
          "registerTime": "2021-01-27 14:36:37",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 1
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 2,
          "userId": "<USER_ID>",
          "registerTime": "2020-11-23 14:26:10",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 1
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 2,
          "userId": "<USER_ID>",
          "registerTime": "2020-10-15 07:08:31",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 1
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 2,
          "userId": "<USER_ID>",
          "registerTime": "2021-04-27 16:23:53",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 1
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 2,
          "userId": "<USER_ID>",
          "registerTime": "2021-01-19 18:36:36",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 1
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 2,
          "userId": "<USER_ID>",
          "registerTime": "2020-08-31 03:37:27",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 1
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 2,
          "userId": "<USER_ID>",
          "registerTime": "2021-06-08 17:41:56",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 1
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 2,
          "userId": "<USER_ID_HASH>",
          "registerTime": "2021-06-07 11:59:33",
          "logoUrl": "",
          "wechat": "",
          "email": "<USER_EMAIL>@example.com",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 1
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 2,
          "userId": "<USER_ID>",
          "registerTime": "2021-06-07 12:11:25",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 1
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 2,
          "userId": "<USER_ID>",
          "registerTime": "2021-06-07 11:57:28",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 1
        },
        {
          "appId": "<APP_ID>",
          "platformId": 1,
          "type": 2,
          "userId": "<USER_ID>",
          "registerTime": "2021-06-09 14:33:12",
          "logoUrl": "",
          "wechat": "",
          "email": "",
          "phone": "",
          "isShow": "true",
          "qqNickName": "<USER_ID>",
          "name": "<USER_NAME>",
          "newUserId": "<USER_ID>",
          "isOperator": 1
        }
      ],
      "disableMemberInvitation": false,
      "channelList": [
        "testchannel",
        "1101"
      ],
      "bundleIdList": [
        "com.example.demo",
        "com.example.demo"
      ]
    }
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» status|integer|true|none||none|
|» ret|object|true|none||none|
|»» code|integer|true|none||none|
|»» message|string|true|none||none|
|»» errorCode|string|true|none||none|
|»» data|object|true|none||none|
|»»» versionList|[object]|true|none||Version List|
|»»»» appId|string|false|none||none|
|»»»» platformId|integer|false|none||none|
|»»»» productVersion|string|false|none||Project version number.|
|»»»» enable|integer|false|none||none|
|»»»» isShow|boolean|false|none||none|
|»»»» enableAutoUpgrade|boolean|false|none||none|
|»»»» sdkVersion|string|false|none||SDK version number.|
|»»» tagList|[object]|true|none||none|
|»»»» appId|string|false|none||none|
|»»»» platformId|integer|false|none||none|
|»»»» tagId|integer|false|none||none|
|»»»» tagName|string|false|none||none|
|»»»» isShow|integer|false|none||none|
|»»» processorList|[object]|true|none||handlers|
|»»»» appId|string|true|none||Project ID|
|»»»» platformId|integer|true|none||Project ID|
|»»»» type|integer|true|none||none|
|»»»» userId|string|true|none||none|
|»»»» registerTime|string|true|none||none|
|»»»» logoUrl|string|true|none||none|
|»»»» wechat|string|true|none||none|
|»»»» email|string|true|none||none|
|»»»» phone|string|true|none||none|
|»»»» isShow|string|true|none||none|
|»»»» qqNickName|string|true|none||none|
|»»»» name|string|true|none||Name|
|»»»» newUserId|string|true|none||User ID|
|»»»» isOperator|integer|true|none||none|
|»»» disableMemberInvitation|boolean|true|none||none|
|»»» channelList|[string]|true|none||none|
|»»» bundleIdList|[string]|true|none||The List of Bundle|

## POST Get the crash details based on OpenID

POST /env/uniform/openapi/getCrashUserInfosignature

Get the crash details based on OpenID

Website： https://crashsight.wetest.net

download python code example:https://crashsight-docs-1258344700.cos.ap-shanghai.myqcloud.com/global/crashsight_openapi_v1_getCrashUserInfo.py

> Body Parameters

```json
{
  "requestid": "<REQUEST_ID>",
  "stime": "2021-12-26 00:00:00",
  "etime": "2021-12-27 00:00:00",
  "appId": "xxx",
  "type": "pretty",
  "filters": {
    "user": [
      "597862998",
      "osewR0lNantT5rywYITNayOep-wA"
    ]
  },
  "limit": 10
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string| yes |none|
|Accept-Encoding|header|string| yes |none|
|body|body|object| no |none|
|» requestid|body|string| yes |Request ID|
|» stime|body|string| yes |Start Time|
|» etime|body|string| yes |End Time|
|» type|body|string| yes |Return Format|
|» appId|body|string| yes |Project ID|
|» filters|body|object| yes |Filter conditions|
|»» user|body|[string]| yes |user list|
|» limit|body|integer| yes |number of returns|

> Response Examples

```json
{
  "requestid": "<REQUEST_ID>",
  "code": 200,
  "errmsg": null,
  "data": {
    "columns": null,
    "values": null,
    "results": [
      {
        "issueId": "<ISSUE_ID>",
        "crashTime": "2021-11-26 20:52:10 354",
        "crashId": "<CRASH_ID>",
        "user": "597862998"
      },
      {
        "issueId": "<ISSUE_ID>",
        "crashTime": "2021-11-26 11:23:04 385",
        "crashId": "<CRASH_ID>",
        "user": "osewR0lNantT5rywYITNayOep-wA"
      }
    ]
  },
  "cost": 0
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» requestid|string|true|none||Request ID|
|» code|integer|true|none||Status Codes|
|» errmsg|string|true|none||Status Codes|
|» data|object|true|none||query results|
|»» columns|string|true|none||fields|
|»» values|string|true|none||values|
|»» results|[object]|true|none||details|
|»»» issueId|string|false|none||issue ID|
|»»» crashTime|string|false|none||crash time|
|»»» crashId|string|false|none||crash ID|
|»»» user|string|false|none||userID|
|» cost|integer|true|none||query duration|

# Data Schema


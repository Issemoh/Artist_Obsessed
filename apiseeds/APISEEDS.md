
APISEEDS offers 10,000 request for free to their Lyrics API

Sign up for a key at https://apiseeds.com/ and make a request via their dashboard https://apiseeds.com/documentation/lyrics


## Obtain APISEEDS lyrics API KEY
1. Sign up for APISEEDS API key here - https://www.apiseeds.com

2. Obtain your applicaion key from your dashboard https://apiseeds.com/account/dashboard

3. Create `.env` file in your project's root directory if not already created and add the api key to the file in this format `apiseeds_api_key = 0000000000000000000000000` where the `0s` represent your application key 


## Example Request
```bash
$ curl https://orion.apiseeds.com/api/music/lyric/:artist/:track?apikey={apikey}
```


## Response headers include:

X-Credits: 9999 `remaining credits`

X-Credits-Premium: 0 `number of premium credits`

X-RateLimit-Limit: 100 `request limit per hour`

X-RateLimit-Remaining: 99 `number of requests left for the time period`

# Example Response
Example Reponse Fields:
```
result - Object
result.artist - Object
result.artist.name - String
result.track - Object
result.track.name - String
result.track.text - String
result.track.lang - Object
result.track.lang.code - String
result.track.lang.name - String
result.copyright - Object
result.copyright.notice - String
result.copyright.artist - String
result.copyright.text - String
```

Example Response 

```json
{
  "result": {
    "artist": {
      "name": "artist name here"
    },
    "track": {
      "name": "track name jere",
      "text": "lyrics here separeted\nby newline characters with unexcaped single quo'tes",
      "lang": {
        "code": "en",
        "name": "English"
      }
    },
    "copyright": {
      "notice": " lyrics are property and copyright of their owners. Commercial use is not allowed.",
      "artist": "Copyright ",
      "text": "All lyrics provided for educational purposes and personal use only."
    },
    "probability": "NaN",
    "similarity": 1
  }
}
```
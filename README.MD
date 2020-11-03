# PPKWU - ZADANIE 2 - STRING API

## Details

The API checks if the given string contains uppercase letters, lowercase letters, digits or special characters and counts them

## Endpoint

`GET /check/<string_to_check>`

where `<string_to_check>` is the string to analize

## Response

```
{
  "containsUppercase": <boolean>,
  "containsLowercase": <boolean>,
  "containsDigits":    <boolean>,
  "containsSpecial":   <boolean>,
  "uppercaseCount":    <number>,
  "lowercaseCount":    <number>,
  "digitsCount":       <number>,
  "specialCount":      <number>
}
```

- `<boolean>` is logic value, `true` or `false`
- `<number>` is positive numeric value

## Example

### Request

`GET /check/ASDqwerty1234`

### Response

```json
{
  "containsUppercase": true,
  "containsLowercase": true,
  "containsDigits": true,
  "containsSpecial": false,
  "uppercaseCount": 3,
  "lowercaseCount": 6,
  "digitsCount": 4,
  "specialCount": 0
}
```
